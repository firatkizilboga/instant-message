import socket
from datatypes import Package
from time import sleep
name = input("name: ")
package_list = []
while (1):
    sleep(0.2)
    p=Package(name,"GET","")
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('localhost', 9000))
    cmd = f'{p.to_json()} \r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        package_list.append(Package.read_json(data.decode()))
    if package_list:
        print(package_list[-1].name+": ",package_list[-1].text)
        package_list=[]
    mysock.close()
