cron { 'run-puppet':
command => '/usr/local/bin/run-puppet',
hour => '*',
minute => '*/15',
}
