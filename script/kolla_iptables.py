# (<port>, <source>, <procotol>, <desc>)
rules = {
    "basic": [
        ('22', '0.0.0.0/0', 'tcp', 'ssh'),
        ('53', '', 'tcp', 'dnsmasq'),
        ('53', '', 'udp', 'dnsmasq'),
        ('873', '', 'tcp', 'rsync'),
        ('3260', '', 'tcp', 'iscsi'),
        ('4000', '', 'tcp', 'kolla registry'),
        ('3306', '', 'tcp', 'mariadb'),
        ('4567', '', 'tcp', 'mariadb'),
        ('4568', '', 'tcp', 'mariadb'),
        ('4444', '', 'tcp', 'mariadb'),
        ('11211', '', 'tcp', 'memcached'),
        ('11211', '', 'udp', 'memcached'),
        ('5672', '', 'tcp', 'rabbitmq'),
        ('15672', '0.0.0.0/0', 'tcp', 'rabbitmq'),
        ('25672', '0.0.0.0/0', 'tcp', 'rabbitmq'),
        ('4369', '0.0.0.0/0', 'tcp', 'rabbitmq'),
        ('5140', '', 'udp', 'fluentd'),
        ('1984', '', 'tcp', 'haproxy-stats'),
    ],
    "keystone": [
        ('5000', '', 'tcp', 'keystone'),
        ('35357', '', 'tcp', 'keystone'),
    ],
    "murano": [
        # ('8082', '', 'tcp', 'murano'),
    ],
    "aodh": [
        # ('8042', '', 'tcp', 'aodh'),
    ],
    "nova": [
        ('8773:8775', '', 'tcp', 'nova-compute'),
        ('8780', '', 'tcp', 'placement_api'),
        ('49152:49215', '', 'tcp', 'libvirt_migration'),
        ('6080:6082', '', 'tcp', 'nova-console'),
        ('5900:6900', '', 'tcp', 'nova-vnc'),
        ('16509', '', 'tcp', 'libvirt'),
    ],
    "sahara": [
        # ('8386', '', 'tcp', 'sahara'),
    ],
    "trove": [
        ('8779', '0.0.0.0/0', 'tcp', 'trove_api'),
    ],
    "horizon": [
        ('80', '', 'tcp', 'horizon'),
        ('443', '', 'tcp', 'horizon'),
        ('8080', '', 'tcp', 'kycloudui'),
    ],
    "neutron": [
        ('9696', '', 'tcp', 'neutron-api'),
        ('58882', '', 'tcp', 'openvswitch-db'),
        ('4789', '', 'udp', 'vxlan-udp'),
        ('6640', '0.0.0.0/0', 'tcp', 'ovsdb-server'),
        ('6633', '0.0.0.0/0', 'tcp', 'neutron_openvswitch_agent'),
    ],
    "glance": [
        ('9191', '', 'tcp', 'glance'),
        ('9292', '', 'tcp', 'glance'),
    ],
    "cinder": [
        ('8776', '', 'tcp', 'cinder'),
    ],
    "ceilometer": [
        ('8777', '', 'tcp', 'ceilometer'),
    ],
    "heat": [
        ('8000', '', 'tcp', 'heat'),
        ('8003', '', 'tcp', 'heat'),
        ('8004', '', 'tcp', 'heat'),
    ],
    "swift": [
        ('6000:6002', '', 'tcp', 'swift'),
    ],
    "ceph": [
        ('6789', '', 'tcp', 'ceph_mon'),
        ('6800:7100', '', 'tcp', 'ceph_osd'),
        ('7480', '', 'tcp', 'radosgw'),
        ('6780', '', 'tcp', 'ceph_rgw'),
    ],
    "gnocchi": [
        ('8041', '', 'tcp', 'gnocchi_api'),
        ('8125', '', 'udp', 'gnocchi'),
    ],
    "grafana": [
        ('3000', '', 'tcp', 'grafana'),
    ],
    "panko": [
        ('8977', '', 'tcp', 'panko_api'),
    ],
}
rule_str = "-A INPUT -s {source} -p {protocol} --dport {port} -m comment --comment \"{desc} {protocol} {port}\" -j ACCEPT"
# rule_str1 = "-A INPUT -m iprange --src-range {source} -p {protocol} --dport {port} -m comment --comment \"{desc} {protocol} {port}\" -j ACCEPT"

sources = [
    '192.168.110.0/24',
]

# _s = [
#     '192.168.110.1-192.168.110.3',
# ]


def main():
    for cata, cata_values in rules.items():
        for r in cata_values:
            port = r[0]
            source = r[1]
            protocol = r[2]
            desc = r[3]
            if source:
                print rule_str.format(
                    port=port, protocol=protocol, desc=desc, source=source)
            for s in sources:
                print rule_str.format(
                    port=port, protocol=protocol, desc=desc, source=s)

    # keepalived
    print "-A INPUT -p vrrp -j ACCEPT"


if __name__ == '__main__':
    main()
