# Installes flask from pip3
package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure => '2.1.0',
  name => 'flask',
  provider => 'pip3',
}
