from http.server import *

# inherit class BaseHTTPRequestHadler

class myServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        #successful response 
        self.send_response(200)
        
        # set a type of the server
        self.send_header('content-type', 'text/html')
        # end of http
        self.end_headers()
        
        #write text to be displayed on the web page
        self.wfile.write('<h1> Hello MUM </h1>'.encode())

        
# object which take a port and server's name
port = HTTPServer(('', 5555), myServer)

# makes the server run forever
port.serve_forever()


    
