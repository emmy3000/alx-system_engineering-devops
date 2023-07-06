# Puppet manifest to configure Nginx with a custom response header

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define the custom response header
file { '/etc/nginx/conf.d/custom_response_header.conf':
  ensure  => present,
  content => "add_header X-Served-By ${::hostname};\n",
  notify  => Service['nginx'],
  audit   => 'content',
}

# Configure the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_response_header.conf'],
}
