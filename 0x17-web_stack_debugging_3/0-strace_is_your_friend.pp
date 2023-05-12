# Fix Apache 500 error
class apache {
  exec { 'fix-apache':
    command => '/usr/local/bin/fix-apache',
    onlyif  => 'test $(curl -s -o /dev/null -w "%{http_code}" http://localhost) = 200',
  }

  service { 'apache2':
    ensure => running,
  }
}
include apache
