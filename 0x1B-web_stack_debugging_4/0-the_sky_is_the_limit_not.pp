# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server settings
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "# Nginx Configuration File
worker_processes auto;
events {
  worker_connections 1024;
}
http {
  client_max_body_size 10M;
  keepalive_timeout 65;
  sendfile on;
  server {
    listen 80;
    server_name localhost;
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    location / {
      proxy_pass http://backend;
    }
  }
}
",
}

# Create logging directory
file { '/var/log/nginx':
  ensure => directory,
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

# Run ApacheBench to simulate HTTP requests
exec { 'benchmark':
  command => 'ab -n 2000 -c 100 http://localhost/',
  path    => '/usr/bin',
  require => Service['nginx'],
}
