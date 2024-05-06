from http.server import HTTPServer

from .request_handler import WebRequestHandler

HOST = "0.0.0.0"
PORT = 8000
server = HTTPServer((HOST, PORT), WebRequestHandler)
print("Server is running ...")
server.serve_forever()