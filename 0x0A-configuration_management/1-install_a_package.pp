# Description: Puppet manifest to install Flask using pip3.

# Define a package resource for Flask with a specific version.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
