from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12000
destAddress = (serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(destAddress)
while True:
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print (modifiedSentence)
clientSocket.close()
