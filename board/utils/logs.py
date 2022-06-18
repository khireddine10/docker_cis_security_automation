import os


def read_log(log_files):
    my_checks_db = dict()
    List = []
    for log in log_files:
        file = str(log)
        if os.path.exists(file):
            with open(file, 'r') as file:
                data = file.read().split("*******", 20)
                i = 1
                while i < len(data):
                    List.append(data[i].replace("\033[1;34m", "").replace("\033[1;31m", "").replace(
                        "\033[1;32m", "").replace("\033[1;31m", "").replace("\033[0m", "").replace("[0;32m", "").replace("[0;31m", "").replace("[0;33m", ""))

                    i += 1
            my_checks_db[get_host_from_log(log)] = {}
            for line in range(0, len(List)-1, 2):
                my_checks_db[get_host_from_log(log)][List[line]] = List[line+1]
    return my_checks_db


def get_host_logs(hostname):
    list_of_logs = []
    for filename in os.listdir("/tmp"):
        f = os.path.join("/tmp", filename)
    # checking if it is a file
        if hostname in str(f):
            list_of_logs.append(str(f))
    return list_of_logs


def get_host_from_log(file):
    return file.split('-')[1]
