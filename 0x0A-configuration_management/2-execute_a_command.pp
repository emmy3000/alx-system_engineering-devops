# Description: Puppet manifest to kill a process named `killmenow` using pkill.

# Define an exec resource to execute the pkill command.
exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}
