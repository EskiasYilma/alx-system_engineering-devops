# Installes flask from pip3
package { 'flask':
  ensure => '2.1.0',
  provider => 'python3 -m pip',
}
