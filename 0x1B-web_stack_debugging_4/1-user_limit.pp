# Upgrade holberton user limits
exec { 'upgrade hard-limits':
  command => "sed -iE 's/^holberton hard nofile 5/holberton hard nofile 10000/' /etc/security/limits.conf",
  path    => '/bin:/usr/sbin:/usr/bin',
}

exec { 'upgrade soft-limits':
  command => "sed -iE 's/^holberton soft nofile 4/holberton soft nofile 10000/' /etc/security/limits.conf",
  path    => '/bin:/usr/sbin:/usr/bin',
}
