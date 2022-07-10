import os
import glob

INVENTORY_VERSION_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/inventories/version.txt"


def create_versions(password):
    playbook_path = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/playbooks/version.yml"
    ansible_command = "ansible-playbook " + playbook_path + " -i " + INVENTORY_VERSION_PATH + " " + "--extra-vars " + \
        '"' + 'ansible_sudo_pass=' + \
        str(password) + '"'
    ansible_result = os.popen(ansible_command).read()


def build_inventory(hostname, ansible_password, ansible_user):
    inventory = hostname + " " + "ansible_ssh_pass=" + \
        ansible_password + " " + "ansible_ssh_user=" + ansible_user + "\n"
    with open(INVENTORY_VERSION_PATH, "a") as f:
        f.write(inventory)


def get_hosts():
    myhosts = []
    with open(INVENTORY_VERSION_PATH, "r") as f:
        mylines = f.readlines()
        for line in mylines:
            myhosts.append(line.split(' ')[0])
    return myhosts


def delete_inventory():
    if os.path.exists(INVENTORY_VERSION_PATH):
        os.remove(INVENTORY_VERSION_PATH)


def remove_version_files():
    for filename in glob.glob("/tmp/version-*"):
        os.remove(filename)


def get_version_logs(hostname):
    mypath = "/tmp/version-" + str(hostname)
    mydata = list()
    if os.path.exists(mypath):
        with open(mypath, 'r') as file:
            data = file.readlines()
            for d in data:
                mydata.append(d.strip())

    return mydata
