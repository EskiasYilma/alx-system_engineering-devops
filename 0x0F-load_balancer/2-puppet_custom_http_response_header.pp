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

# html directory
file { '/var/www/html':
  ensure => 'directory',
  mode   => '0755',
  owner  => 'root',
  group  => 'root',
}

# index.html content
file { '/var/www/html/index.html':
  ensure  => 'file',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Hello World!',
  require => File['/var/www/html'],
}

# 404.html content
file { '/var/www/html/404.html':
  ensure  => 'file',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Ceci n'est pas une page',
  require => File['/var/www/html'],
}

# 404 Error
file_line { 'error':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'server_name _;',
  line    => 'error_page 404 /404.html;',
  require => Package['nginx'],
}

# X-Served-By
file_line { 'X-Served-By':
  ensure  => 'present',
  path    => '/etc/nginx/nginx.conf',
  after   => '# server_name_in_redirect off;',
  line    => 'add_header X-Served-By $HOSTNAME;',
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure   => 'running',
  provider => 'service',
}
