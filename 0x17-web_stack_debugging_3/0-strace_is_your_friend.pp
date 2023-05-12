# Corrects bad `phpp` extensions to `php` in wp file `wp_test.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp_test.php',
  path    => '/usr/local/bin/:/bin/'
}
