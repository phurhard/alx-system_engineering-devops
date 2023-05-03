# This puppet script install flask version 2.1.0
package { 'python':
  ensure => 'installed',
}

package { 'python3-pip':
  ensure => installed,
}

package { 'build-essential':
  ensure => installed,
}

package { 'libssl-dev':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  creates => '/usr/local/bin/flask',
}
