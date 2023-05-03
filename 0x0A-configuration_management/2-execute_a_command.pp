#This script kils a process named killlmenow
exec {'kill':
  command => '/usr/bin/pkill -f killmenow',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
