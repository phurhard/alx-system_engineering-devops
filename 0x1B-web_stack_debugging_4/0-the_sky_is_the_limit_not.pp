# Modifies the nginx default file descriptor
$file_path = '/etc/default/nginx'  # Specify the path to the file you want to modify

# Backup the original file
file { "${file_path}.bak":
  ensure => 'file',
  source => $file_path,
}

# Replace the line with the desired value
file { $file_path:
  ensure  => 'file',
  replace => 'true',
  content => 'ULIMIT="-n 4096"',
  notify  => Exec['reload_service'],
}

exec { 'reload_service':
  command     => 'service nginx restart',
  refreshonly => true,
}
