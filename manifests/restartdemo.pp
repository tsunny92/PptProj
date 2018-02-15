service { 'ntp':
        ensure => running,
        enable => true,
        harestart => true,
}
