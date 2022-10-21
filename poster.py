import socket
from datatypes import Package
name = input("name: ")
while True:
    text = input("text: ")
    p=Package(name,"POST",text)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('localhost', 9000))
    cmd = f'{p.to_json()} \r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()