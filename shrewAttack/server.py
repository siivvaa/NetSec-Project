import socket

def Main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind and listen
    serverSocket.bind(("127.0.0.1", 9000))
    serverSocket.listen()
    while True:
        (clientConnected, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))
        dataFromClient = clientConnected.recv(1024)
        print("Message received")
            
Main()