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
file_line { 'X-Served-By':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen [::]:80 default_server;',
  line    => 'add_header X-Served-By $HOSTNAME;',
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure   => 'running',
  provider => 'service',
}
