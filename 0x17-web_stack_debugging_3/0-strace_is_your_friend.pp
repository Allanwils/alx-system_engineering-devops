exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/' /var/www/html/wp_test.php",
  path    => '/usr/local/bin/:/bin/',
}
