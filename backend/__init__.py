import psutil

from subprocess import Popen
import nbformat as nbf

import socket
from .NBWriter import NBWriter
from .VoilaRunner import VoilaRunner

def get_free_port():
    # Bind to a range of port numbers
    for port in range(8000, 9000):
        try:
            # Try to bind to the port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
            # If successful, return the port number
            return port
        except socket.error:
            # If the port is already in use, try the next one
            pass
    # If no free port is found, raise an exception
    raise Exception("No free port found in range")


# temp notebook path
NOTEBOOK_PATH = './tempFiles/temp_notebook.ipynb'
PORT = get_free_port()

# VoilaRunner setup
voilaRunner = VoilaRunner(NOTEBOOK_PATH, PORT)
nbWriter    = NBWriter(NOTEBOOK_PATH)