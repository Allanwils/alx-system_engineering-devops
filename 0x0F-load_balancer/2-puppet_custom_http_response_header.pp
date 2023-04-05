#!/usr/bin/env bash

# Adds a stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# updates software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# installs nginx
package { 'nginx':
  ensure     => 'installed',
}

# creates a custom header configuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => "add_header X-Served-By 102967-web-02;",
}

# removes default nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# adds a redirection and error page
file { 'Nginx custom config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/custom_config',
  content =>
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    # Includes a custom header configuration file
    include /etc/nginx/conf.d/custom_header.conf;

    location / {
        try_files \$uri \$uri/ =404;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}",
}

# restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start service nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
