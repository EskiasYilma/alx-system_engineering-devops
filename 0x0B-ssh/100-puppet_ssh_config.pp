# Sets up a client SSH configuration file so that you can connect to a server without typing a password.
file { '/etc/ssh/ssh_config':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "PasswordAuthentication no\nPubkeyAuthentication yes\nIdentityFile ~/.ssh/school\n",
}
