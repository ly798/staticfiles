#!/usr/bin/env python
# coding: utf8
import time
import os
import shutil

nic_relationships = [
    # (<bond_name>, [<physical_name>,<>] , <ip>, <netmask>, <gateway>(只能有一张网卡带有gateway))
    ('bond0', ['eth0', 'eth1'], '192.168.1.10', '255.255.255.0',
     '192.168.1.1'),
    ('bond1', ['eth2', 'eth3'], '192.168.2.10', '255.255.255.0', ''),
    ('bond2', ['eth4', 'eth5'], '192.168.3.10', '255.255.255.0', ''),
    ('bond3', ['eth6', 'eth7'], '192.168.4.10', '255.255.255.0', ''),
]

physical_nic_template = """
DEVICE={physical_nic_name}
NAME={physical_nic_name}
TYPE=Ethernet
BOOTPROTO=none
ONBOOT=yes
MASTER={bond_nic_name}
SLAVE=yes
"""

bond_nic_template = """
DEVICE={bond_nic_name}
NAME={bond_nic_name}
TYPE=Bond
BONDING_MASTER=yes
BOOTPROTO=none
BONDING_OPTS="mode=1 miimon=100"
ONBOOT=yes
IPADDR={ip}
NETMASK={netmask}
"""

bond_nic_with_gateway_template = "%sgateway={gateway}" % bond_nic_template


def backup_nic_cfg_file(nic_name):
    backup_folder = '/etc/sysconfig/network-scripts/nic_backups'
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    source_file = '/etc/sysconfig/network-scripts/ifcfg-%s' % nic_name
    if not os.path.exists(source_file):
        return
    dist_path = os.path.join(backup_folder, 'ifcfg-%s.%s' %
                             (nic_name,
                              time.strftime("%Y%m%d%H%M%S", time.localtime())))
    print('move %s to %s' % (source_file, dist_path))
    shutil.move(source_file, dist_path)


def main():
    for relationship in nic_relationships:
        bond_nic_name, physical_nic_names, ip, netmask, gateway = relationship
        print(bond_nic_name, physical_nic_names, ip, netmask, gateway)
        # backup
        backup_nic_cfg_file(bond_nic_name)
        for physical_nic_name in physical_nic_names:
            backup_nic_cfg_file(physical_nic_name)
        # write new config
        for physical_nic_name in physical_nic_names:
            dist_path = '/etc/sysconfig/network-scripts/ifcfg-%s' % physical_nic_name
            print('generate %s...' % dist_path)
            with open(dist_path, 'w') as f:
                f.write(
                    physical_nic_template.format(
                        physical_nic_name=physical_nic_name,
                        bond_nic_name=bond_nic_name))

        bond_dist_path = '/etc/sysconfig/network-scripts/ifcfg-%s' % bond_nic_name
        print('generate %s...' % bond_dist_path)
        with open(bond_dist_path, 'w') as f:
            if gateway:
                f.write(
                    bond_nic_with_gateway_template.format(
                        bond_nic_name=bond_nic_name,
                        ip=ip,
                        netmask=netmask,
                        gateway=gateway))
            else:
                f.write(
                    bond_nic_template.format(
                        bond_nic_name=bond_nic_name,
                        ip=ip,
                        netmask=netmask,
                        gateway=gateway))

    os.system('systemctl restart network')
    os.system('systemctl status network')


if __name__ == '__main__':
    main()
