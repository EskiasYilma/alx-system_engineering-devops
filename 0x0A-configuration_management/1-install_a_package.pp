# Installes flask from pip3
package { 'flask':
  provider => 'pip3',
  install_options => ['flask==2.1.0'],
}
