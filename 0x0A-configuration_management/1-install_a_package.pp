# Description: Puppet manifest to install Flask using pip3

# Define a package resource for flask with a specific version
package { 'flask':
  ensure  => '2.1.0',
  provide => 'pip3',
}
