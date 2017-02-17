import http.server


class MyHTTPServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write("test.... Hi!".encode("utf-8"))


def start():
    server_address = ('localhost', 8000)
    httpd = \
        http.server.HTTPServer(server_address, MyHTTPServerHandler)
    httpd.serve_forever()
