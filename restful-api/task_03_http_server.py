import http.server
import json


class Handler(http.server.BaseHTTPRequestHandler):
    """Handles HTTP requests for different endpoints."""
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {
                "name": "John Doe",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_info = json.dumps(info)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_info.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def run(server_class=http.server.HTTPServer, handler_class=Handler):
    """Starts the HTTP server."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
