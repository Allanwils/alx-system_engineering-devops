# The scripts add a stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# The script updates software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec['add nginx stable repo'],
}

# installs nginx
package { 'nginx':
  ensure     => 'installed',
  require    => Exec['update packages'],
}

# allows HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
  require => Package['nginx'],
}

# changes folder rights
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# creates an index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
  require => Exec['chmod www folder'],
}

# creates a  404 error page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
  require => Exec['chmod www folder'],
}

# adds redirection and error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        add_header X-Served-By $hostname;

        location / {
            try_files \$uri \$uri/ =404;
        }
        
        location = /404.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=msSc7Mv0QHY permanent;
        }
}
",
  require => [File['/var/www/html/index.html'], File['/var/www/html/404.html']],
}

# restarts nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['nginx'],
}

# starts service nginx
service { 'nginx':
  ensure  => running,
  require => Exec['restart service'],
}
