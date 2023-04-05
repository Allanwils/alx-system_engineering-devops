# The script adds a stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Updates software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Installs nginx
package { 'nginx':
  ensure     => 'installed',
}

# Allows HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# Changes folder permissions
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Creates a  index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Creates a  404 file
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Adds a custom HTTP header and error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By \$hostname;
    location / {
        try_files \$uri \$uri/ =404;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://youtube.com permanent;
    }
}
",
}

# Restarts nginx service
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# Starts nginx service
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
