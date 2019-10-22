from socket import *

serverPort = 12000 # Port number of your server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive!")

while True:
    print ('-----------------------')
    receivedMessage,clientAddress = serverSocket.recvfrom(2048)
    msg_split = str(receivedMessage).split(":")
    print ('Received message: ' + msg_split[1])
    print('sequence number: ' + msg_split[0])
    print("Source name: " +  str(clientAddress[0]))
    print("Source port: " +  str(serverPort)) #clientAddress[1]
    modifiedMessage = msg_split[1].upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print ('Sent message: ' + str(modifiedMessage))

    
