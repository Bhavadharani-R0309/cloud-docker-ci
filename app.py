from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            b"<h1>Cloud Computing Experiment</h1>"
            b"<h2>Docker Container Running Successfully!</h2>"
        )

server = HTTPServer(("0.0.0.0", 8000), MyHandler)

print("Server running on port 8000")

server.serve_forever()