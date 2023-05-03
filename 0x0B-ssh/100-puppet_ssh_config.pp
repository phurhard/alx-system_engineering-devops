# This puppet file set the configuration of the ssh
file { '/etc/ssh/ssh_config/':
  ensure => file,
  content => 'Host *
        PasswordAuthentication no
        IdentityFile ~/.ssh/school',
}
