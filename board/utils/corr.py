import os


INVENTORY_CORR_PATH = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/inventories/corr.txt"


def build_inventory(hostname, ansible_password, ansible_user):
    inventory = hostname + " " + "ansible_ssh_pass=" + \
        ansible_password + " " + "ansible_ssh_user=" + ansible_user + "\n"
    with open(INVENTORY_CORR_PATH, "a") as f:
        f.write(inventory)


def delete_inventory():
    if os.path.exists(INVENTORY_CORR_PATH):
        os.remove(INVENTORY_CORR_PATH)


def run_corr(corr_number, password):
    playbook_path = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/playbooks/correction.yml"
    correction_paths = "/home/khirou/Desktop/pfe/dashboard/dashboard/board/utils/corrections/"
    ansible_command = "ansible-playbook " + playbook_path + " -i " + INVENTORY_CORR_PATH + " " + "--extra-vars " + \
        '"' + 'ansible_sudo_pass=' + \
        str(password) + ' name=' + corr_number + '"'
    print(ansible_command)
    ansible_result = os.popen(ansible_command).read()
