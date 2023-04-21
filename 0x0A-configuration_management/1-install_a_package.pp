# Installes flask from pip3
package { 'python3-pip':
  ensure => 'installed',
}

file { '/tmp/requirements.txt':
  ensure => file,
  content => "flask==2.1.0\n",
}

exec { 'install_flask':
  command => 'pip3 install -r /tmp/requirements.txt',
  path    => ['/usr/bin', '/usr/sbin'],
}
