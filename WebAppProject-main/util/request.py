class Request:

    def __init__(self, request: bytes):
        # TODO: parse the bytes of the request and populate the following instance variables

        self.body = b""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self.headers = {}
        self.cookies = {}
class Request:
    # Goal: Parse the HTTP request into it (HTTP) Method, (HTTP) path(including cookies)  ,
    # (HTTP) port,  Headers, and message body (if applicable)
    # Highlight what fileds are in b' or as Strings
    def __init__(self, request: bytes):

        self.body = b""
        #only one in bytes
        self.method = ""
        self.path = ""
        self.http_version = ""
        self.headers = {}
        #str:str
        self.cookies = {}





        #------------------------------------------
        RequestLine = bytes.split(b"\r\n\r\n")
        # anfdother CRLF after message body?
        if len(RequestLine) > 1:
            MessageBody = RequestLine[1]
            MessageBody += self.body
        else:
        # THE METHOD AND THE PORT HAVE SPACES INBETWEEN THE PATH
            MethnPathPortnHeader = RequestLine[0]
            HTTPMethnPathPortHeader = MethnPathPortnHeader[0].decode()
            Headerlines = HTTPMethnPathPortHeader.split("\r\n")
            HTTPMETHpathjnPort = Headerlines[0]
            Headerparts = Headerlines[1]
            Parts = Headerparts[1].split(":")
            DictHeader = self.headers
        # logic for space/omit - " Content-Length: 5"
            DictHeader["Parts[0]"] = ["Parts[1]"]
            HTTPMeth = HTTPMETHpathjnPort.split(" ",3)
            Method = HTTPMeth[0]
            Method += self.method
            # Q: what if my path consist of query_strings(&) or multiple cookies (=) ?  (loop through)- ask still
            pathNcookie = HTTPMeth[1]
            #Cookies = pathNcookie.split(" ")
            #is there something between the cookies and path?
            ThePath = self.method
            pathNcookie += ThePath
            # do you parse the path with or without the cookies?
            FindingCookies = pathNcookie.split("=")
            TheCookiesyay = FindingCookies[1]
            Cook = self.cookies
            TheCookiesyay += Cook
            Portnum = HTTPMeth[3]
            Port = self.method
            Portnum += Port

# Q: Does this code go into my server - POST request for html/img? (Extending MYTCPHANDLER)
    # nosniff ; charset=utf-8"r\n\r\n")
    def ReadingFiles(self):
       # Files In Public/ ... (more path )
        with open(b'"style.css,style.css"'):
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




def test1():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b""  # There is no body for this request.
    # When parsing POST requests, the body must be in bytes, not str

    # This is the start of a simple way (ie. no external libraries) to test your code.
    # It's recommended that you complete this test and add others, including at least one
    # test using a POST request. Also, ensure that the types of all values are correct


if __name__ == '__main__':
    test1()
