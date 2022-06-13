import os
import sys


INVENTORY_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/inventories/check.txt"
PLAYBOOKS_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/playbooks/"


def build_inventory(hostname, ansible_password, ansible_user):
    inventory = hostname + " " + "ansible_ssh_pass=" + \
        ansible_password + " " + "ansible_ssh_user=" + ansible_user + "\n"
    with open(INVENTORY_PATH, "a") as f:
        f.write(inventory)


def delete_inventory():
    if os.path.exists(INVENTORY_PATH):
        os.remove(INVENTORY_PATH)


def remove_log_files():
    for i in range(1, 8):
        file = "/tmp/log" + str(i)
        if os.path.exists(file):
            os.remove(file)


def runcheck(checkNum, ansible_user, ansible_password, log_file):
    checkPlay = PLAYBOOKS_PATH + str(checkNum) + ".yml"
    ansible_command = "ansible-playbook" + " " + checkPlay + " -i " + INVENTORY_PATH + \
        " --extra-vars " + '"' + \
        "ansible_sudo_pass=" + ansible_password + '"'
    ansible_result = os.popen(ansible_command).read()
