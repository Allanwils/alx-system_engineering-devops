#!/usr/bin/env bash

# create custom HTTP header file
# configure web-02 to be identical to web-01
# enable custom HTTP header file

sudo apt-get update
sudo apt-get install -y nginx

echo "add_header X-Served-By \$hostname;" | sudo tee /etc/nginx/conf.d/custom-http-header.conf > /dev/null

sudo ln -s /etc/nginx/conf.d/custom-http-header.conf /etc/nginx/conf.d/

# Restart Nginx to apply new configuration
sudo systemctl restart nginx
