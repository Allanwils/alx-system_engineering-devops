#!/bin/env bash

# Automates a custom HTTP header response but with Puppet
apt-get -y update
apt-get -y install nginx

sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default

# Restarts nginx service
service nginx restart
