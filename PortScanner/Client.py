import socket
import sys


def search(start_port, end_port, target_ip):
    try:
        for p in range(start_port, end_port):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res1 = client_socket.connect_ex((target_ip, p))

            if res1 == 0:
                print("[+] Open port with number: " + str(p))
                open_ports.append(str(p))

            client_socket.close()

    except socket.error:
        print("[!] There was an Error with the connection")
        sys.exit()


target = input("[+] Enter target IP Adress: ")
start_port = int(input("[+] Enter start port: "))
end_port = int(input("[+] Enter end port: "))

target_ip = socket.gethostbyname(target)
open_ports = []

print("\n[+] Start searching for open ports...")
print("[+] Host " + target + " | IPAdress " + target_ip + "\n\n")

search(start_port, end_port, target_ip)

print("\n\n[+] Done!")
print("[+] Open ports: " + str(open_ports))