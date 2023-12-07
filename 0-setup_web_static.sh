#!/usr/bin/env bash
# Sets up web servers for the deployment of `web_static`

# Verify nginx is present
if command -v nginx &> /dev/null; then
  echo "Nginx already installed."
else
  apt-get update
  apt install -y nginx

  # Create necessary files
  mkdir -p /data/web_static/shared
  mkdir -p /data/web_static/releases/test
  echo "Hello nginx" > /data/web_static/releases/test/index.html

  # Create sym links to test folder
  ln -s /data/web_static/releases/test/ /data/web_static/current

  # Give permissions to user and group `ubuntu`
  chown -R ubuntu:ubuntu /data/

  # Update nginx to serve content correctly
  sed -i '/server_name _;/a \
	location /hbnb_static {\
		alias /data/web_static/current/;\
		index index.html index.htm;\n\t}' /etc/nginx/sites-available/default
  # Restart nginx
  service nginx restart
fi
