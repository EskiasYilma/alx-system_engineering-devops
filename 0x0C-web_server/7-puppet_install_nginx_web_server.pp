# Update apt
exec { 'update apt':
  command => 'apt update',
  path    => ['/usr/bin', '/usr/sbin'],
}

# Install Nginx
package { 'Install Nginx'
  ensure          => 'installed',
  name            => 'nginx',
  provider        => 'apt',
  install_options => ['-y']
}

# Start Nginx
exec { 'Start Nginx':
  command => 'service nginx start',
  path    => ['/usr/bin', '/usr/sbin'],
}

# index.html content
$index_content = "Hello World!\n"
file { '/var/www/html/index.html':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  content => $index_content,
}

# 404.html content
$404_content = "Ceci n'est pas une page\n"
file { '/var/www/html/404.html':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  content => $404_content,
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

        # SSL configuration
        #
        # listen 443 ssl default_server;
        # listen [::]:443 ssl default_server;
        #
        # Note: You should disable gzip for SSL traffic.
        # See: https://bugs.debian.org/773332
        #
        # Read up on ssl_ciphers to ensure a secure configuration.
        # See: https://bugs.debian.org/765782
        #
        # Self signed certs generated by the ssl-cert package
        # Don't use them in a production server!
        #
        # include snippets/snakeoil.conf;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
          # First attempt to serve request as file, then
          # as directory, then fall back to displaying a 404.
          try_files $uri $uri/ =404;
        }
        rewrite ^/redirect_me http://bachmanity.tech permanent;
        error_page 404 /404.html;

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
  }",
}

# Restart Nginx
exec { 'Restart Nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/usr/sbin'],
}
