service { 'ntp':
        ensure => running,
        enable => true,
        restart => 'systemctl restart ntpd',
}
