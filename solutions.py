import os
import subprocess
import paramiko
from paramiko import RSAKey
from base64 import decodebytes

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def check_key_validity(key_path):
    try:
        key_path = os.path.expanduser(key_path)
        key= RSAKey.from_private_key_file(key_path)
        paramiko.RSAKey(data=key.asbytes())
        return True
    except (IOError, paramiko.SSHException) as e:
        return False

def main():
    path = os.path.expanduser("~/.ssh/id_rsa.pub")

    if os.path.isfile(path) == False :
        print(RED + f"il file {path} non esiste" + RESET)
        exit()

    if check_key_validity(path):
        print(GREEN + "chiave valida" + RESET)
        # cambiare il nome
        new_folder_path = "../Octocat/"

        # cambiare la repo
        url_repository = "https://github.com/giacominho3/Octocat.git"

        print(GREEN + "\nHINT: ricorda l'ordine dei calcoli e delle operazioni :)" + "\n" + RESET)
        try:
            comando_clone = ["git", "clone", url_repository, new_folder_path]
            subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(GREEN + "Livello completato con successo!" + RESET)
            print("Troverai il prossimo livello in " + MAGENTA + new_folder_path + RESET)
        except subprocess.CalledProcessError as e:
            print(RED + "Errore durante il cloning del repository: " + e + RESET)
    else:
        print(RED + "chiave non valida" + RESET)

if __name__ == "__main__":
    main()