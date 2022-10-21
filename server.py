from socket import *
from datatypes import Package

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    package_list = []
    try :
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            print(pieces)
            package = Package.read_json(pieces[0])
            if package.request == "POST":
                package_list.append(package)
                clientsocket.shutdown(SHUT_WR)

            if package.request == "GET":
                for p in range(len(package_list)):
                    if (package.name != package_list[p].name) and (package.name not in package_list[p].recievers) and (package_list[p].request == "POST"):
                        package_list[p].recievers.append(package.name)
                        data = package_list[p].to_json() + "\r\n\r\n"
                        clientsocket.sendall(data.encode())
                        clientsocket.shutdown(SHUT_WR)
                        break
            #data = "HTTP/1.1 200 OK\r\n"
            #data += "Content-Type: text/html; charset=utf-8\r\n"
            #data += "\r\n"
            #data += "<html><body>Hello World</body></html>\r\n\r\n"
            #clientsocket.sendall(data.encode())

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()

print(gethostbyname(gethostname()),gethostname(),9000)
createServer()
