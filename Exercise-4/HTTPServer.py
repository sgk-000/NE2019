from socket import *
import sys


serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverAddr = '127.0.0.1'

# Bind the socket to server address and server port, then listen
serverSocket.bind((serverAddr, serverPort))
serverSocket.listen(1)


while True:
    print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, clientAddress = serverSocket.accept()

    try:
        # Receives the request message from the client
        # should have .decode()
        message = (connectionSocket.recv(1024)).decode()
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 	# Store the file in a temporary buffer
        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            # each time send outputdata[i]
            connectionSocket.send(outputdata[i])

        connectionSocket.send("\r\n")
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><body><center><h1>Error 404: File not found</h1></center><p>Head back to <a href=\"/\">dry land</a>.</p></body></html>")
        print('HTTP/1.1 404 Not Found\r\n')
        print("Server Address:", serverAddr)
        print("client Address:", clientAddress)
        print("Port number:", serverPort)
        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data
