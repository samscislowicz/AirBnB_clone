#!/usr/bin/env bash
# This sets up a web server to the project requirements
# First install nginx 
sudo apt-get update
sudo apt-get install -y nginx
# Makes folders if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
# Creates a fake HTML file
echo -e '<html><head></head><body>Holberton School</body></html>' | sudo tee /data/web_static/releases/test/index.html
# Creates a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Gives ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "39i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-enabled/default
# Restart nginx
sudo service nginx restart