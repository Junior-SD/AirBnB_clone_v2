#!/usr/bin/env bash
# bash script that prepares a web server

sudo apt update
sudo apt install nginx -y
sudo apt upgrade nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# touch /data/web_static/releases/test/index.html
echo "test page" | sudo tee /data/web_static/releases/test/index.html > /dev/null

if [ -L /data/web_static/current ]; then # delte symbolic link
	sudo rm /data/web_static/current
fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
