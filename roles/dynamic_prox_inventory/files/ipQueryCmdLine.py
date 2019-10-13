#!/usr/bin/python2

from proxmoxer import ProxmoxAPI
from argparse import ArgumentParser


def find_ip(proxmox_connection, node_name, vm_id):
    agent_status = proxmox_connection.nodes(node_name).qemu(vm_id).config.get()
    try:
        if (agent_status['agent']):
            ip = (proxmox.nodes(node_name).qemu(vm_id).agent.
                  create(command='network-get-interfaces'))
            for i in range(len(ip['result'])):
                for n in range(len(ip['result'][i]['ip-addresses'])):
                    if '192.' in (ip['result'][i]['ip-addresses']
                                  [n]['ip-address']):
                        return(ip['result'][i]['ip-addresses']
                               [n]['ip-address'])
    except:
        pass


if __name__ == '__main__':
    proxmox = ProxmoxAPI('node2.du.nn', user='root@pam',
                         password='Turtles2prox', verify_ssl=False)
    parser = ArgumentParser(description='Find VM IP')
    parser.add_argument('-n', '--node', required=True,
                        help='Node VM resides on currently')
    parser.add_argument('-v', '--vmid', required=True,
                        help='VM id')
    args = parser.parse_args()
    print(find_ip(proxmox, args.node, args.vmid))