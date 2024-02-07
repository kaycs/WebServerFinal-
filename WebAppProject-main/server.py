import socketserver
# LO2 Goal -


#ref : http:// docs.python/org/3/library/socketserver.html?hgihlight=requestthan


class MyTCPHandler(socketserver.BaseRequestHandler):
# Override Handle method - New TCP connections
    def handle(self):
        # get message form client - what they send us in bytes
        # we do deal with data

        received_data = self.request.recv(2048)

        #client_id = self.client_address[0] + ":" + str(self_client_address[1])
        #print(client_id + "is sending data:")
        print(len(received_data))
        print(self.client_address)
        print("--- received data ---")
        print(received_data)
        print("--- end of data ---\n\n")
        #request = Request(received_data)
    #.decode() - string .encode() - bytes
# CONCATENATE THE RECIEVED DAT YOU GOT - RESPONSE FORMAT


# HTTP Method + Number Type Message CRLD Content-Length + CRLF + Content-Type + 2X CRFL
#and message

        Router(request, self)

























def __init__(self):
    Host = "0.0.0.0"
    # Listen for connections (IP) Local Host - Docker Access
    Port = 8000
    # Docker/Docker Compose HW - 8080


# Set up TCP handshake
    Server = socketserver.ThreadingTCPServer(Host,Port, MyTCPHandler)
    Server.serve_forever()










def main():
    host = "0.0.0.0"
    port = 8080

    socketserver.TCPServer.allow_reuse_address = True

    server = socketserver.TCPServer((host, port), MyTCPHandler)

    print("Listening on port " + str(port))

    server.serve_forever()


if __name__ == "__main__":
    main()
