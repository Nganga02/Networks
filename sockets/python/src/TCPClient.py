from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)# the SOCK_STREAM is to indicate that the connection is a TCP connection
clientSocket.connect((serverName, serverPort))

sentence = input("input lowercase sentence: ")

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print(f"From server: {modifiedSentence.decode()}")
clientSocket.close()