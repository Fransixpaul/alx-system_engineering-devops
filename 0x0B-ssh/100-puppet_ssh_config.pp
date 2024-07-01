#!/usr/bin/env bash
# Puppet to make changes to our configuration file
file {'/etc/ssh/shh_config':
	ensure	=> 'present',
}
file_line {'Turn off passwd auth':
	path	=> '/etc/ssh/shh_config',
	line	=> 'PasswordAuthentication no',
	match	=> 'PasswordAuthentication yes',
	replace => 'true',
}
file_line {'Declare identity file':
	path	=> '/etc/ssh/shh_config',
	line	=> 'IdentityFile ~/.ssh/school',
	match	=> 'Identityfile',
	ensure	=> 'present',
}
