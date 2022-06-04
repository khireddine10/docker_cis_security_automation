import os
import sys


INVENTORY_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/inventories/connect.txt"


def build_inventory(hostname, ansible_password, ansible_user):
    inventory = hostname + " " + "ansible_ssh_pass=" + \
        ansible_password + " " + "ansible_ssh_user=" + ansible_user

    if os.path.exists(INVENTORY_PATH):
        os.remove(INVENTORY_PATH)
    with open(INVENTORY_PATH, "a") as f:
        f.write(inventory)


def test_connectivity(hostname, ansible_password, ansible_user):
    build_inventory(hostname, ansible_password, ansible_user)
    ansible_command = "ansible all -m ping -i " + INVENTORY_PATH
    ansible_result = os.popen(ansible_command).read()
    if "SUCCESS" in ansible_result:
        return True
    else:
        return False
