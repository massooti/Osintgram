import argparse
import os
from src import printcolors as pc



def initialLogin():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()
    settings_file = "config/settings.json"
    if not os.path.isfile(settings_file):
        with open('config/credentials.ini', 'r+') as file:
            data = file.read()
            file.seek(14)
            file.write('username= ' + args.username + '\n' + 'password = '+ args.password)
            file.truncate()

    elif os.path.isfile(settings_file):
        os.remove(settings_file)
        with open('config/credentials.ini', 'r+') as file:
            data = file.read()
            file.seek(14)
            file.write('username= ' + args.username + '\n' + 'password = '+ args.password)
            file.truncate()

    pc.printout("your username and password is set now try to login...")



initialLogin()
