# This script Installs Nginx and configures a custom HTTP response header
class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html;

      server_name _;

      add_header X-Served-By ${::hostname};

      location / {
        try_files \$uri \$uri/ =404;
      }
    }",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

include nginx_custom_header
