from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class SlowHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(3)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"id": 1, "status": "ok"}')

HTTPServer(("127.0.0.1", 8766), SlowHandler).serve_forever()