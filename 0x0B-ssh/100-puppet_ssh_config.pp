# This Puppet manifest sets up SSH client configuration to use the private key
# ~/.ssh/school and refuse authentication using a password.

# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => file,
}

# Add the private key identity file to the client configuration file
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

# Turn off password authentication in the client configuration file
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
