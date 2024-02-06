
class Request:
    # Goal: Parse the HTTP request into it (HTTP) Method, (HTTP) path(including cookies)  ,
    # (HTTP) port,  Headers, and message body (if applicable)
    # Highlight what fileds are in b' or as Strings
    def __init__(self, request: bytes):
#   DONE
        self.body = b""
        #only one in bytes (^^)
# DONE
        self.method = ""
# DONE
        self.path = ""
# DONE
        self.http_version = ""
# DONE
        self.headers = {}
        #str:str
        self.cookies = {}



#    request = Request(b'GET (0)  (1) / (2) HTTP/1.1 (2)
        #    \r\n (2)
        #    (1) Host:
        #    localhost:8080
        #    \r\n (1)
        #    (0) Connection: (PART 1) keep-alive (0)
        #
        #    \r\n\r\n')


        #------------------------------------------
        #request = b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n'[0]
        # hello[1]
        RequestLine = request.split(b"\r\n\r\n",1)
        MessageBody = RequestLine[1]
        MessageBody += self.body
        # THE METHOD AND THE PORT HAVE SPACES INBETWEEN THE PATH
        #request = b'GET / HTTP/1.1   \r\n [0]
        # Host: localhost:8080    \r\n [1]
        # Connection: keep-alive [2]
        Head = RequestLine[0].split(b'"\r\n"')
        Headd = Head.decode()
        HeadersDict = self.headers
        for LHnP in Headd[1].split(":"):
            HeadersDict[LHnP[0]] = HeadersDict[LHnP[1]]
            Headers = Headd[2].decode()
            Cookie = Headd[3].decode()
    #request = b'GET [0]    /[1]    HTTP/1.1[2]     \r\n
            for Line in Head[0].split(" ",2):
                Meth = Line[0].decode()
                Path = Line[1].decode()
                HTTP = Line[2].decode()
                Meth += self.method
                Path += self.path
                HTTP += self.http_version
                for Headerspart in Headers.split(":"):
                    HeadersDict = self.headers
                    HeadersDict[Headerspart[0]] = HeadersDict[Headerspart[1]]
                    for CookiePairs in Cookie.split(";"):
                        for CookieKey in CookiePairs.split("="):
                            HeadersDict[CookieKey[0]] = HeadersDict[CookieKey[1]]





        # MethnPathPortnHeader = RequestLine[0]
        # HTTPMethnPathPortHeader = MethnPathPortnHeader.decode()
        # #HTTPMethnPathPortHeader = MethnPathPortnHeader[0].decode()
        # # for all the headers ? - parse? or is it already defualt
        # Headerlines = HTTPMethnPathPortHeader.split("\r\n",2)
        # HTTPMETHpath = Headerlines[2]
        # Headerparts = Headerlines[0]
        # Parts = Headerparts[0].split(":")
        # DictHeader = self.headers
        # # logic for space/omit - " Content-Length: 5"
        # for DictHeader[Parts[0]] in DictHeader:
        #     DictHeader[Parts[0]] = DictHeader[Parts[1]]
        #     HTTPMeth = HTTPMETHpath.split(" ", 2)
        #     Method = HTTPMeth[0]
        #     Method += self.method
        #     # Q: what if my path consist of query_strings(&) or multiple cookies (=) ?  (loop through)- ask still
        #     pathNcookie = HTTPMeth[1]
        #     # get the path apart -
        #     pathNcookie.split()
        #     Path = pathNcookie[1]
        #     ThePath = self.method
        #     Path += ThePath
        #     # FIX PARSING THE COOKIES(!!!!)
        #     #then split on the cookies
        #
        #     Cookies = pathNcookie.split(";")
        #     #is there something between the cookies and path?
        #     CookieK = Cookies.split("=")
        #     Cook = self.cookies
        #     Cook[CookieK[0]] = Cook[CookieK[1]]
        #      # do you parse the path with or without the cookies?
        #     #split on ; then = (through each value) - add to cookies dict
        #     Portnum = HTTPMeth[2]
        #     Port = self.method
        #     Portnum += Port





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
