# File: 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html index.htm;
  
      location / {
        return 200 'Hello World!';
      }
  
      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
  
      error_page 404 /404.html;
      location = /404.html {
        internal;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Remove the default Nginx welcome page
file { '/var/www/html/index.html':
  ensure => 'absent',
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
