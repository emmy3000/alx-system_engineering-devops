# Define a file resource for /tmp/school with specific permission and content

file { 'tmp/school':
  ensure => file,
  mode   => '0744',
  owner  => 'www-data',
  group  => 'I love Puppet',
}
