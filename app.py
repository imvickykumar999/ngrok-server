#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
import logging, ngrok
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        root = os.path.dirname(os.path.abspath(__file__))
        if self.path == "/":
            file_path = os.path.join(root, "index.html")
        else:
            file_path = os.path.join(root, self.path[1:])
        
        if os.path.exists(file_path) and not os.path.isdir(file_path):
            self.send_response(200)
            if file_path.endswith(".html"):
                self.send_header("Content-Type", "text/html")
            elif file_path.endswith(".css"):
                self.send_header("Content-Type", "text/css")
            elif file_path.endswith(".js"):
                self.send_header("Content-Type", "application/javascript")
            elif file_path.endswith(".png"):
                self.send_header("Content-Type", "image/png")
            elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                self.send_header("Content-Type", "image/jpeg")
            else:
                self.send_header("Content-Type", "application/octet-stream")
            self.end_headers()
            with open(file_path, "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "File not found")

logging.basicConfig(level=logging.INFO)
server = HTTPServer(("localhost", 0), MyHandler)
ngrok.listen(server)
server.serve_forever()
