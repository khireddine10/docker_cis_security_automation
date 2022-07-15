import os
import sys
import glob


INVENTORY_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/inventories/check.txt"
PLAYBOOKS_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/playbooks/"


def build_inventory(hostname, ansible_password, ansible_user):
    inventory = hostname + " " + "ansible_ssh_pass=" + \
        ansible_password + " " + "ansible_ssh_user=" + ansible_user + " " \
        + "ansible_sudo_pass=" + ansible_password + "\n"
    with open(INVENTORY_PATH, "a") as f:
        f.write(inventory)


def delete_inventory():
    if os.path.exists(INVENTORY_PATH):
        os.remove(INVENTORY_PATH)


def remove_log_files():
    for filename in glob.glob("/tmp/log*"):
        os.remove(filename)


def runcheck(checkNum, ansible_user, ansible_password):
    checkPlay = PLAYBOOKS_PATH + str(checkNum) + ".yml"
    ansible_command = "ansible-playbook" + " " + checkPlay + " -i " + INVENTORY_PATH
    ansible_result = os.popen(ansible_command).read()
