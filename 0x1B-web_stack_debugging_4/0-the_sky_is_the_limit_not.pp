# Modifies the nginx default file descriptor
exec { 'modify nginx':
  provider => 'shell',
  command     => 'sed -i "s/15/1024/g" /etc/default/nginx; service nginx restart',
}
