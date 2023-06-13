# Update ulimit and restart nginx
exec { 'update-ulimit':
  command => "sed -iE 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => '/bin:/usr/sbin:/usr/bin',
  notify  => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command     => 'service nginx restart',
  refreshonly => true,
  path        => '/bin:/usr/sbin:/usr/bin',
}
