from socket import *
import time
serverName = 'www.ipb.uni-bonn.de'
serverPort = 80
destAddress = (serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(destAddress)
sentence = "GET / HTTP/1.1\r\nHost:" + serverName + "\r\n\r\n"
start_time = time.time()
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
end_time = time.time()
print (modifiedSentence)
print("computational time = ", end_time - start_time);
clientSocket.close()
