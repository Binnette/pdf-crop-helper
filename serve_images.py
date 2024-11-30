import http.server
import socketserver
import os
import webbrowser
import threading
import time

# Define the port to run the server on
PORT = 8000

# Define the directory to serve (current directory)
DIRECTORY = os.path.dirname(__file__)

# Define the handler for the HTTP server
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Function to start the HTTP server
def start_server(httpd):
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

# Function to open the web browser
def open_browser():
    url = f"http://localhost:{PORT}/index.html"
    webbrowser.open(url)

# Function to stop the server
def stop_server(httpd):
    print("Shutting down the server")
    httpd.shutdown()
    httpd.server_close()

# Create the HTTP server
handler = CustomHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server, args=(httpd,))
server_thread.daemon = True
server_thread.start()

# Open the browser
open_browser()

# Schedule the server to stop after 1 minute (60 seconds)
timeout = 60  # seconds
timer = threading.Timer(timeout, stop_server, args=(httpd,))
timer.start()

# Keep the script running to keep the server alive
try:
    while server_thread.is_alive():
        server_thread.join(1)
except KeyboardInterrupt:
    print("Server stopped manually")
    stop_server(httpd)
