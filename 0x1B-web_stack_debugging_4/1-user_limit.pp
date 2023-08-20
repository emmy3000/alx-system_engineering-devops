# Configure system limits for the 'holberton' user to prevent 'Too many open files' errors.

user { 'holberton':
  ensure     => 'present',
  managehome => true,
  shell      => '/bin/bash',
}

file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => 'holberton - nofile 4096',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Exec['pam_reload'],
}

file { '/etc/security/limits.d/holberton-pam.conf':
  ensure  => file,
  content => 'session required pam_limits.so',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Exec['pam_reload_after'],
}

exec { 'pam_reload':
  command     => 'pam_tally2 -r',
  path        => '/usr/bin',
  refreshonly => true,
}

exec { 'pam_reload_after':
  command     => 'pam_tally2 -r',
  path        => '/usr/bin',
  refreshonly => true,
}
