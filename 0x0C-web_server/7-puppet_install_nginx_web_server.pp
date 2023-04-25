# Update apt
exec { 'update apt':
  command => 'apt update',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
}

# Install Nginx
package { 'nginx'
  ensure => 'installed',
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

# html directory
file { '/var/www/html':
  ensure => 'directory',
  mode   => '0755',
  owner  => 'root',
  group  => 'root',
}

# index.html content
file { '/var/www/html/index.html':
  ensure => 'file',
  mode   => '0644',
  owner  => 'root',
  group  => 'root',
  content => 'Hello World!',
  require => File['/var/www/html'],
}

# Restart Nginx
service { 'nginx':
  ensure   => 'running',
  provider => 'service',
}
