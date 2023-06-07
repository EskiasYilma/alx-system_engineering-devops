# Apache is returning a 500 error Fix
exec { 'apache_fix':
  command => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin:/sbin:/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin'],
}
