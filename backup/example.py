#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
from pyngrok import ngrok
import urllib.parse

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        try:
            with open("index.html", "rb") as file:  # Open the HTML file
                body = file.read()  # Read the HTML file content
            self.send_header("Content-Length", len(body))
            self.end_headers()
            self.wfile.write(body)  # Send the HTML content
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(bytes(f"Error: {str(e)}", "utf-8"))

    def do_POST(self):
        self.protocol_version = "HTTP/1.1"
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode('utf-8'))
        
        name = data.get('name', [''])[0]

        response = f"Hello, {name}!"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(bytes(response, "utf-8"))

logging.basicConfig(level=logging.INFO)
server = HTTPServer(("localhost", 8000), HelloHandler)

# Open a ngrok tunnel to the HTTP server
http_tunnel = ngrok.connect(8000)
print("ngrok tunnel \"{}\" -> \"http://localhost:8000\"".format(http_tunnel.public_url))

server.serve_forever()

