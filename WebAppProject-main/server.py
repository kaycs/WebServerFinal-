import socketserver
from util.request import Request
# LO2 Goal -


#ref : http:// docs.python/org/3/library/socketserver.html?hgihlight=requestthan


# Q: Demo from lecture showed the TCP response correct?
# Q: I Need to parse my request properly to be able to respond?
class MyTCPHandler(socketserver.BaseRequestHandler):
# Override Handle method - New TCP connections
    def handle(self):
        # get message form client - what they send us in bytes
        # we do deal with data

        received_data = self.request.recv(2048)
        # client_id = self.client_address[0] + ":" + str(self_client_address[1])
        #print(client_id + "is sending data:")
        print(len(received_data))
        print(self.client_address)
        print("--- received data ---")
        print(received_data)
        print("--- end of data ---\n\n")
        request = Request(received_data)
    #.decode() - string .encode() - bytes
# CONCATENATE THE RECIEVED DAT YOU GOT - RESPONSE FORMAT

#FIRST PART (STRING) - BODY (BYTE) - CONTENT LENGTH IN BYTES

# STRING - BYTES
# request.sendall - response to client
# LO2 Responses - IMG/HTML/PNG,ETC

    print("\n\n")
self.request.sendall("HTTP/1.1 Not Found\r\nContent-Length:36\r\nContent-Type text/css; charset=utf-8 \r\n\r\n"
                     "The requested content does not exist".encode())

# When data received and processed by request - check path and send app repsone based on path
# condtional to know what resposne you want - if your path is .... (Threading)




def __init__(self):
    Host = "0.0.0.0"
    # Listen for connections (IP) Local Host - Docker Access
    Port = 8000
    # Docker/Docker Compose HW - 8080


# Set up TCP handshake
    Server = socketserver.ThreadingTCPServer(Host,Port, MyTCPHandler)
    Server.serve_forever()


    # Q: Does this code go into my server - POST request for html/img? (Extending MYTCPHANDLER)
    # nosniff ; charset=utf-8"r\n\r\n")
    def ReadingFiles(self):
        # Files In Public/ ... (more path )
        with open("style.css,style.css", "rb"):
            ByteArrCSS = style.css.len()
            #CSS Request- /path/public/style.css
    #print( # self.request.sendall("POST /path/public/style.css HTTP/1.1 \r\nContent-Length: ____byte arr \r\nX-Content-Type-Options:
    #Content-Type: text/css


    #HTML request-/ root host
    # Q: Can I Convert to Bytes while opening?
    with open(b'"index.html, index,html"'):
        ByteArrHTML = index.html.len()

#print (
#self.request.sendall("POST / HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r\n")


# Content-Type: text/html- (cat, dog, eagel, elphant, elphant small, flamigo, kitten)

# Image Request- path different - len() bytes
#Content-Type: image/jpg (?)

#print (
#self.request.sendall("POST /public/image/cat.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; (no need)  charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/kitten.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/dog.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/eagle.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/elephant-small.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/flamingo.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \

#Q: For emoji request what is  the path? -  bytes array
#self.request.sendall("POST  HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \








def main():
    host = "0.0.0.0"
    port = 8080

    socketserver.TCPServer.allow_reuse_address = True

    server = socketserver.TCPServer((host, port), MyTCPHandler)

    print("Listening on port " + str(port))

    server.serve_forever()


if __name__ == "__main__":
    main()
