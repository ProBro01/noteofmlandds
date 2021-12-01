import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.164.14", 1234))
with open("hello.jpg", "wb") as f:
    while True:
        data = client.recv(1024)
        f.write(data)
