#!/bin/bash

# Set the SSH public key to be added to the authorized_keys file
SSH_PUBLIC_KEY=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCxb6hIXgM7dYirx8ST/LFfgGyEl6h4R7zNwymMxwKbPC7sMChbtPNUZcbkFF+LnJ8SpF4+7yTjixMVkw/O1zc8efkqG8URKx8ANjQnoyq07YQMz8x9iYIRGa70QoYGAn5CZzhmZBdCQ3zPbARTFSp28y6yAJ4GUzN8QYKXUDkOQ/V/ToTIaM31NNz3oqJAfwjR02RcndFWwHl092EWX/vRkM65P/Z8rtpGdD4+xGOVzVJFmkXR1LvvVeyh5NH3BTgwwnt/McNgzrLmWmS48ywNug4pqQqpu0tk9N9DN2WBiOo7iHB6Rrwby5IC8g/wzSkdMqS3e4hxW7MN/XXs6aszPRP46CkQolnZsXFYQm/hBc4qqHR7PK9LiIhhiFABsw5I0EsDt0WFWL8jcEfZSCJ9SxQvqr0IqJiAmhP6BTT1pNPqOySeunsQB8LL264WAsjKFxXNgHBSPqhpfPdaQRh71paRkGPJbujpSMRVR2DQ+yYE5MPRoD7U6vL2dVESGE0

# Connect to the server using SSH and add the SSH public key to the authorized_keys file

ssh ubuntu@18.207.1.58 "mkdir -p ~/.ssh && echo $SSH_PUBLIC_KEY >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"

# Test the SSH connection from your remote machine

ssh ubuntu@18.207.1.58
