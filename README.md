# Ansible Proxmox Playbook

## Table of Contents

* [Project Overview](#project-overview)
* [Installation](#installation)
* [Commands](#common-commands)

## Project Overview

This repo consist of my Ansible playbooks that are used to manage my Homelab.

## Installation

1. Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
2. Clone repo: `git clone https://github.com/finish06/playbooks.git`
3. Install [Ansible-Proxmox-Inventory](https://github.com/xezpeleta/Ansible-Proxmox-inventory) on Ansible host
4. Install [Proxmoxer](https://pypi.org/project/proxmoxer/) on cluster node(s)


## Common Commands
### Clone a VM:
1. Update `vars` folder in `clone` role: prox_password (vault optional), node IP/DNS name, clone source template, node cluster name & storage location
2. Move template to node that is performing actions
3. Install Proxmoxer on node performing actions
4. Execute below script: update `__proxmox_node__`, `__####__` & `__vm_name__` as appropriate
5. Remove `-e 'ansible_python_interpreter=/usr/bin/python3'` if **NOT** using python3 interpreter

`ansible-playbook -i "__proxmox_node__," /root/playbooks/new_vm.yml -e 'ansible_python_interpreter=/usr/bin/python3 vm_id=__####__ vm_name=__vm_name__' -u "root" --ask-vault-pass`

### Update VMs/CTs
1. Update `vars` folder in `update` role: password (ssh password - vault optional)
2. Update ssh user as appropriate: `-u root` indicates root ssh user
3. Remove `-e 'ansible_python_interpreter=/usr/bin/python3'` if **NOT** using python3 interpreter
4. Remove `--limit "Update"` unless CT/VM notes contain necessary JSON

`ansible-playbook -i /etc/ansible/proxmox.py /root/playbooks/new_vm.yml --limit "Update" -e 'ansible_python_interpreter=/usr/bin/python3' -u "root" --ask-vault-pass`