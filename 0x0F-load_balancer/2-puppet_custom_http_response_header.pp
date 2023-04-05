class nginx_custom_header {
  $server_name = '102967-web-02'

  file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "add_header X-Served-By ${server_name};\n",
    notify  => Service['nginx'],
  }
}

include nginx_custom_header
