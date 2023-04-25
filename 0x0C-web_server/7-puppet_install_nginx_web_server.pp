# Update apt
exec { 'update apt':
  command => 'apt update',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
}

# Install Nginx
package { 'Install Nginx'
  ensure          => 'installed',
  name            => 'nginx',
  provider        => 'apt',
  install_options => ['-y']
}

# index.html content
file { '/var/www/html/index.html':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  content => "Hello World!\n"
}

# Redirect Config
exec { 'Redirect Config':
  command     => '/bin/echo -e "rewrite ^/redirect_me http://bachmanity.tech permanent;" | sudo sed -i "53a\\$(cat)" /etc/nginx/sites-available/default',
  path        => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default']
}


# Restart Nginx
exec { 'Restart Nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
}
