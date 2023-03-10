from PySide2.QtWebEngineWidgets import QWebEngineView

class Viewer(QWebEngineView):
    def __init__(self, port):
        super().__init__()
        self.port = port
        
    def loadUrl(self):
        self.load(f"http://localhost:{self.port}/")

