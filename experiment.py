import psutil

from subprocess import Popen
import nbformat as nbf

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide2.QtWebEngineWidgets import QWebEngineView
from visualizer_template_generator.generator import ViewGenerator

import socket


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


def kill():
    # Get all running processes
    for proc in psutil.process_iter():
        try:
            # Get the process name
            process_name = proc.name()
            
            # Check if the process is a subprocess
            if process_name == "python":
                # Kill the subprocess
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


class View(QWebEngineView):
    def __init__(self, port):
        super().__init__()
        self.port = port
    
    def loadUrl(self):
        self.load(f"http://localhost:{self.port}/")


class NBWriter:
    def __init__(self, path=""):
        self.path = path
        self.nb = nbf.v4.new_notebook()

    def addCode(self, code):
        cell = nbf.v4.new_code_cell(source=code)
        self.nb['cells'] = [cell]
    
    def save(self):
        nbf.write(self.nb, 'my_notebook.ipynb')


class VoilaRunner:
    def __init__(self, nbPath, port):
        self.nbPath = nbPath
        self.port = port
        self.command = f'voila {self.nbPath} --no-browser --port={self.port}'
    
    def start(self):
        Popen(self.command.split())


notebook_path = './tempFiles/temp_notebook.ipynb'
port = get_free_port()
nbwriter = NBWriter(notebook_path)
voilaRunner = VoilaRunner(notebook_path, port)
gen = ViewGenerator()

def buttonClick():
    gen.changeColor("red")
    nbwriter.addCode(gen.getCode())
    nbwriter.save()
    kill()
    voilaRunner.start()

if __name__=="__main__":

    voilaRunner.start()
    
    
    app = QApplication([])
    window = QMainWindow()
    window.setGeometry(100, 100, 700, 500)
    pdbWidget = View(port)
    button = QPushButton("click")

    button.clicked.connect(buttonClick)
    
    layout = QVBoxLayout()
    temp = QWidget()
    layout.addWidget(pdbWidget)
    layout.addWidget(button)
    
    temp.setLayout(layout)
    window.setCentralWidget(temp)
    window.show()

    pdbWidget.loadUrl()
    app.exec_()