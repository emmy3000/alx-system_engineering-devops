# Puppet manifest to fix the Apache 500 error

# Ensure the Apache service is running and enabled
service { 'apache2':
  ensure => 'running',
  enable => true,
}

# Define the path to the virtual host configuration file
$virtual_host_file = '/etc/apache2/sites-available/your_virtual_host.conf'

# Define the correct content for the virtual host configuration
$correct_config_content = @(
<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/html
    # Add other configuration directives as needed
</VirtualHost>
)

# Ensure the correct configuration is in place
file { $virtual_host_file:
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => $correct_config_content,
  require => Service['apache2'],
  notify  => Exec['reload-apache'],
}

# Reload Apache only if the configuration was changed
exec { 'reload-apache':
  command     => 'service apache2 reload',
  refreshonly => true,
}
