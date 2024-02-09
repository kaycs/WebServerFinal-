import socketserver
# LO2 Goal - respond to various MIME types

# router.function name - to retrurn to server.py
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

       # Router(respond, self)
           # return(respond(recevied_data))


def respond(self):
    # PARSING INDEX HTML FILE
    # TEXT FILES
    if self.path == "/":
        # b' ?
        # change HTML bc lib in python
        with open("index.html", "rb") as indexh:
            byt = indexh.read()
            bytehtml = len(byt)
        # how exaclty to I put that numerical value into the request?
            self.request.sendall(f"HTTP/1.1 200 OK\r\nContent-Length: {bytehtml}\r\nX-Content-Type-Options: nosniff ; Content-Type: text/html; charset=utf-8 \r\n\r\n". encode())

    # conditional for path (?)
        with open("style.css,", "rb") as ByteArrCSS:
            css = ByteArrCSS.read()
            cssby = len(css)
    #CSS Request- /path/public/style.css
            self.request.sendall(F"HTTP/1.1 200 OK /public/style.css\r\nContent-Length:{cssby} \r\nX-Content-Type-Options: nosniff; Content-Type: text/css;charset=utf-8 \r\n\r\n".encode())
    #Content-Type: text/css
    #404 error  (!!!!!!!!!!!!!!!!!!!!!!!!!!!)
    # whats the conditional and check 404 in message
    #     self.path = Path
    #   if self.path == Exception:
    #     self.request.sendall("HTTP/1.1 Not Found\r\nContent-Length:36\r\nContent-Type text/css; charset=utf-8 \r\n\r\n.encode())")
    #  #                  "The requested content does not exist".encode())
    #
    # # f - formatting
    # encode REQUEST LINE (SLAPPING BYTES AT END) uNELSS DATA ALREADY IN BYTES - IMG, VIDEOS
    if self.path == "/public/image/eagel.jpg":
        with open("eagle.jpg","rb") as Eagle:
            self.request.sendall(f"HTTP/1.1 200 OK /public/image/eagle.jpg\r\nContent-Length:{Eagle}\r\nX-Content-Type-Options: nosniff; Content-Type: img/jpg\r\n\r\n")
        # follow logic for other picture
    # responding to images -or if Cotent-Type == "image/png"
    elif self.path == "/public/image/kitten.jpg":
        with open("cat.jpg", "rb" ) as Cat:
            self.request.sendall(f"HTTP/1.1 200 OK /public/image/kitten.jpg\r\nContent-Length:{Cat}\r\nX-Content-Type-Options: nosniff; Content-Type: img/jpg\r\n\r\n")
    elif self.path == "/public/image/dog.jpg":
        with open("dog.jpg","rb") as Dogby:
            self.request.sendall(f"HTTP 200 OK  /public/image/dog.jpg\r\nContent-Length:{Dogby}\r\nX-Content-Type-Options: nosniff ; Content-Type: img/jpg \r\n\r\n")
        # follow logic for other picture
    elif self.path == "/public/image/elephant-small.jpg":
        with open("elephant-small.png", "rb") as smelepby :
            self.request.sendall(f"HTTP 200 OK  /public/image/elephant-small.jpg\r\nContent-Length:{smelepby}\r\nX-Content-Type-Options: nosniff ;Content-Type: img/jpg\r\n\r\n")
    if self.path == "/public/image/eagel.jpg":
        with open("flamingo.jpg","rb") as flagby:
            self.request.sendall(f"HTTP 200 OK  /public/image/flamingo.jpg\r\nContent-Length:{flagby}\r\nX-Content-Type-Options: nosniff ; Content-Type: img/jpg \r\n\r\n")
    # follow logic for other picture




# LO3 - Guest Chat and Database Storage
























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
