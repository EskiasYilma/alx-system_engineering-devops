# Update apt
exec { 'update apt':
  command => 'apt update',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
}

# Install Nginx
package { 'nginx':
  ensure          => 'installed',
  provider        => 'apt',
  install_options => ['-y']
}

# Redirect
exec { 'redirect':
  command  => 'sudo sed -i "54i\rewrite ^/redirect_me http://bachmanity.tech permanent;" /etc/nginx/sites-enabled/default',
  provider => 'shell',
}

# X-Served-By
exec { 'X-Served-By':
  command  => 'sudo sed -i "16i\add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
  provider => 'shell',
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
