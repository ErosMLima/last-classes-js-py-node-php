#Connecting server

import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

#Output    
#C:\Users\Deltah\PycharmProjects\pythonteste.py\venv\Scripts\python.exe C:/Users/Deltah/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/scratch_16.py
#serving at port 8000
