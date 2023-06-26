# Configure SSH client to use specific private key and disable password authentication

# Puppet manifest to manage SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => 'IdentitiesOnly yes
              IdentityFile ~/.ssh/school',
}
