# Update apt
exec { 'update apt':
  command => 'apt update',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
}

# Install Nginx
package { 'nginx'
  ensure          => 'installed',
  provider        => 'apt',
  install_options => ['-y']
}

# Start Nginx Service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Firewall access
firewall { 'nginx':
  port   => 80,
  proto  => 'tcp',
  action => 'allow',
}

# X-Served-By
exec { 'X-Served-By':
  command  => 'sudo sed -i "16i\add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
  provider => shell,
}

# Restart Nginx
service { 'nginx':
  ensure   => 'running',
  provider => 'service',
}
