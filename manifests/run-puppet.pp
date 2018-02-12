cron { 'run-puppet':
command => 'sh /root/pupperproj/files/run-puppet.sh',
hour => '*',
minute => '*/15',
}
