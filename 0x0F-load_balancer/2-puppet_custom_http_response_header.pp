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
  content => 'Hello World!\n',
  require => File['/var/www/html'],
}

# 404.html content
file { '/var/www/html/404.html':
  ensure  => 'file',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "Ceci n'est pas une page\n",
  require => File['/var/www/html'],
}

# Redirect
exec { 'redirect':
  command  => 'sudo sed -i "54i\rewrite ^/redirect_me http://bachmanity.tech permanent;" /etc/nginx/sites-enabled/default',
  provider => 'shell',
}

# 404
exec { '404':
  command  => 'sudo sed -i "55i\error_page 404 /404.html;" /etc/nginx/sites-enabled/default',
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
