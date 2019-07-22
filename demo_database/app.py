#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler


class Handle(BaseHTTPRequestHandler):
    def do_sth_for_GET(self):
        self.send_response(200)
        self.send_header('Content_type', 'text\plain')
        self.end_header()

        self.wfile.write("你好,我是一句话~\n")


if __name__ == "__main__":
    server_address = ('', 9999)
    httpd = HTTPServer(server_address, Handle)
    httpd.serve_forever()
