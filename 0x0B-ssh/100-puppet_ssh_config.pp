# Sets up a client SSH configuration file so that you can connect to a server without typing a password.
file { '/home/ubuntu/.ssh/ssh_config':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => '
  Host 100.25.36.86
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  '
}
