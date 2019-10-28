import threading
from socket import *

def handleClient(connectionSocket):
    while True:
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
        
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
clients = []
print ('The server is ready to receive')
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    clients.append((connectionSocket, clientAddress))
    curr_thread = threading.Thread(target=handleClient, args=(connectionSocket,), daemon=True) 
    curr_thread.start()
    ############## 
