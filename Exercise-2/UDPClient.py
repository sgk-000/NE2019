from socket import *
import string
serverName = '127.0.0.1' # IP address of your server
serverPort = 12000  # Port number of your server
destAddress=(serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
count = 0;
while True:
    count += 1;
    if(count >= 10):
        break
    print ('-----------------------')
    message = input('Input lowercase sentence:')
    message = str(count) + ':' + message
    clientSocket.sendto(message.encode(),destAddress)
    print ('Sent message: ' + message)

    receivedMessage, serverAddress = clientSocket.recvfrom(2048)
    print ('Received message: ' + str(receivedMessage))
