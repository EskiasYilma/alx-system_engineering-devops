# Update apt
exec { 'update apt':
  command => 'apt update',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}

# Install Nginx
package { 'Install Nginx'
  ensure          => 'installed',
  name            => 'nginx',
  provider        => 'apt',
  install_options => ['-y']
}

# index.html content
file { '/var/www/html/index.html':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  content => "Hello World!\n",
}

# Server Config
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  content =>
  "server {
          listen 80 default_server;
          listen [::]:80 default_server;

          root /var/www/html;

          # Add index.php to the list if you are using PHP
          index index.html index.htm index.nginx-debian.html;

          server_name _;

          location / {try_files $uri $uri/ =404;}
          rewrite ^/redirect_me http://bachmanity.tech permanent;

          # pass PHP scripts to FastCGI server
          #
          #location ~ \.php$ {
          # include snippets/fastcgi-php.conf;
          #
          # # With php-fpm (or other unix sockets):
          # fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
          # # With php-cgi (or other tcp sockets):
          # fastcgi_pass 127.0.0.1:9000;
          #}

          # deny access to .htaccess files, if Apache's document root
          # concurs with nginx's one
          #
          #location ~ /\.ht {
          # deny all;
          #}
  }"
}

# Restart Nginx
exec { 'Restart Nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/usr/sbin'],
}
