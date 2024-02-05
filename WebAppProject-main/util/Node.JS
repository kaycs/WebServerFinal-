/ Can someone help me utlize the Node.JS extension?
/TCP Sokcet Server- NODE.JS VERSION
    const net = required(‘net’);
    console.log(“starting the server”);

/ Create Server
    net.createServer(function (socket) {

/Take a socket

    socket.on( “data”, (function(data) {

        const clientId = socket.remoteAdress + ":”+ socket.remotePort;
    /printing length of data

        console.log('“\n\n*******\n\nfrom” + clientId + “received” + data.length + “bytes”');


    # convert to string
        Console.log(data.toString());
    # respond with Hello and Non-ASCII characters


    # Calling Function buildResponse() (RECCOMENDED Helper Method )
    # takes response code and content type and actual content

    # 		Like Socket.Sendall – Python.

    # Send Information BACK to the client
        Socket.write(buildResponse(“200 OK”, “text/plain; charsetutf-8”, Buffer.from(“Hello こんにちは)));
    # same as .encode() in Python – Str –-> Arr of Bytes (string,img, json string)
        AO1 – IMAGE (Bytes)

    }]

    #Run Server by listening on local host port 800 – same as python (diff syntax)
]}.listen{host: “0.0.0.0”, port: 8000});

# Hadling ALL HTTP stuff – Handle ONE time and update when you extend headers,etc (iterate over headers)

# splice in responseCode and crlfs with content-type and content-length
# Note: Already in Bytes – Hit .length()

Function buildResponse(responseCode, mimeType, content) {
    Let response = “HTTP/1.1” + responseCode + “/r/n”;
    Response += “Content-Type: “ + mimeType + “r\n;

    Response += “Content-Length:  “ + content-length;
    Response += “r\n\r\n”;
# Concating the two byte arrays
# Response is String – Convert to Bytes
    Return Buffer.concat([Buffer.from(response), Buffer.from(content)])
# Uneeded (already in Bytes)





