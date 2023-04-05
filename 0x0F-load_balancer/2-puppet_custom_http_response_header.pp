#!/usr/bin/env bash

# Install Nginx
class { 'nginx':
  manage_repo => true,
}

# Define Nginx virtual host
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By \"$hostname\";
    location / {
      try_files \$uri \$uri/ =404;
    }
    if (\$request_filename ~ redirect_me){
      rewrite ^ https://youtube.com permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
      internal;
    }
  }",
}

# Enable Nginx virtual host
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Create default index and 404 pages
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}
file { '/var/www/html/404.html':
  ensure  => 'file',
  content => 'Ceci n\'est pas une page',
}
