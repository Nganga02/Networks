from socket import *
import time
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input Lowercase sentence: ')
for i in range(0, 10):
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(f"serverAddress: {serverAddress[0]} message: {modifiedMessage.decode()}")
    time.sleep(1)
