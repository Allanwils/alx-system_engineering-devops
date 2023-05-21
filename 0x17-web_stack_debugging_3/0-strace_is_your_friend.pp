exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp_test.php",
  path    => '/usr/local/bin/:/bin/',
  returns => '0',
}
