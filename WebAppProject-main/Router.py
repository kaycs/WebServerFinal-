#import Request
def respond(self):
 # PARSING INDEX HTML FILE
 # TEXT FILES
 if self.path == "/":
     # b' ?
     # change HTML bc lib in python
     with open("index.html", "rb") as html:
         html = html.read()
         bytehtml = len(html)
     # how exaclty to I put that numerical value into the request?
    self.request.sendall(f"HTTP/1.1 200 OK\r\nContent-Length: {bytehtml}\r\nX-Content-Type-Options: nosniff ; Content-Type: text/html; charset=utf-8 \r\n\r\n". encode())
# f - formatting
# encode REQUEST LINE (SLAPPING BYTES AT END) uNELSS DATA ALREADY IN BYTES - IMG, VIDEOS

# Path = self.path
if Path == "/webrtc.js/":
    self.request.sendall("HTTP/1.1 200 OK /webrtc.js/\r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; Content-Type: text/javascript; charset=utf-8 \r\n\r\n")



       # Images= how do you make it generic -"image/png" then specificy?

         # responding to images -or if Cotent-Type == "image/png"
 if self.path == "/public/image/kitten.jpg":
      # with open("cat.png") as Cat:
      #   Cat =
            self.request.sendall("HTTP/1.1 200 OK /public/image/kitten.jpg\r\nContent-Length:  \r\nX-Content-Type-Options: nosniff; Content-Type: img/jpg\r\n\r\n")
 if self.path == "/public/image/eagel.jpg":
    with open("eagle.jpg") as Eagle:
     self.request.sendall("HTTP/1.1 200 OK /public/image/eagle.jpg\r\nContent-Length:  \r\nX-Content-Type-Options: nosniff; Content-Type: img/jpg\r\n\r\n")
# follow logic for other picture
if self.path == "/public/image/elephant-small.png":
    self.request.sendall("POST /public/image/elephant-small.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ;Content-Type:  charset=utf-8 \r\n\r\n")
if self.path = /public/image/dog.
self.request.sendall("POST /public/image/dog.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/cat.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; (no need)  charset=utf-8" \r\n\r \
#self.request.sendall("POST /public/image/flamingo.jpg HTTP/1.1 \r\nContent-Length: \r\nX-Content-Type-Options: nosniff ; charset=utf-8" \r\n\r \

         #--------------------------------------------------------------------
 #check utf-8
# css file
with open("style.css,", "rb") as ByteArrCSS:
    CSS = ByteArrCSS.len()
        #CSS Request- /path/public/style.css
    self.request.sendall("HTTP/1.1 200 OK /public/style.css\r\nContent-Length: \r\nX-Content-Type-Options: nosniff; Content-Type: text/css;charset=utf-8 \r\n\r\n")
    #Content-Type: text/css
# icon
#? if path == ""


#404 error
    # whats the conditional and check 404 in message
#     self.path = Path
# if Path == Exception:
     self.request.sendall("HTTP/1.1 Not Found\r\nContent-Length:36\r\nContent-Type text/css; charset=utf-8 \r\n\r\n")
#                  "The requested content does not exist".encode())

# When data received and processed by request - check path and send app repsone based on path
# condtional to know what resposne you want - if your path is .... (Threading)

#-----------------------------------------------------------------------
#Verify that the HTML (done),(done) CSS, JavaScript, and image were all served through separate HTTP requests
    # Check each HTTP response for the correct MIME type
    # Check each HTTP response for the correct Content-Length
    # Verify that the 2 emoji (non-ASCII characters) display properly
    # Verify that a UB icon is displayed in the tab for the page



