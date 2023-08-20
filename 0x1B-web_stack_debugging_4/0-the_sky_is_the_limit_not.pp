# Puppet Manifest to optimize Nginx configuration for handling high traffic loads.

package { 'nginx':
  ensure => 'installed',
}

$file_content = '
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
  worker_connections 4000;
}

http {
  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  keepalive_timeout 65;
  types_hash_max_size 2048;

  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
  ssl_prefer_server_ciphers on;

  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;

  gzip on;

  include /etc/nginx/conf.d/*.conf;
  include /etc/nginx/sites-enabled/*;
  add_header X-Served-By "221827-web-01";
}
'

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => $file_content,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
