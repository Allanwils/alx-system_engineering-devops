# Automates creation of  a custom HTTP header response, but with Puppet.

file { '/path/to/script.sh':
  mode => '0755',
  content => "#!/bin/bash\n\napt-get -y update\napt-get -y install nginx\nsudo sed -i \"/listen 80 default_server;/a add_header X-Served-By \$HOSTNAME;\" /etc/nginx/sites-available/default\nservice nginx restart\n",
}

exec { 'install_nginx':
  command => '/path/to/script.sh',
  provider => shell,
  require => File['/path/to/script.sh'],
}
