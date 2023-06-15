# Configures holberton user

exec{'holberton hard':
	path => ["/bin"],
	command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 4096/" /etc/security/limits.conf',
}

exec{'soft holberton':
	path => ["/bin"],
	command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4096/" /etc/security/limits.conf',
}
