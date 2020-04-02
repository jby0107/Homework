# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:11:10 2020

@author: jiang
"""

import http.server
import socketserver


Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', 8000), Handler) as httpd:
    print('Serving at port 8000')
    httpd.serve_forever()