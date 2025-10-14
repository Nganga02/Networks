#import socket module
from socket import *
import sys # In order to terminate the program

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    print(f'Ready to serve from')
    connectionSocket, addr = serverSocket.accept()
    print(f"connections from {addr}")
    
    try:
        message = connectionSocket.recv(1028).decode()
        print(f"Method is: {message.split()[0]}")
        if not message:
            connectionSocket.close()
            continue

        filename = message.split()[1]
        print(f"requestedFile: {filename}")


        f = open(filename[1:])
        outputdata = f.read() #reading the file contents
        f. close()

        #Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()

        print("Response sent. Closing server...")
        serverSocket.close()
        sys.exit()

    except IOError:
        #Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
        connectionSocket.close()

        print("File not found. Closing server...")
        serverSocket.close()
        sys.exit()