from PySide2.QtWidgets import QFileDialog
from PySide2.QtWebEngineWidgets import QWebEngineView

import py3Dmol



class PDBVisualizer(QWebEngineView):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.setMinimumSize(self.width+20, self.height+20)

        self.pdbPath = ""
        self.fileName = ""

        self.system = None

        self.view = py3Dmol.view(width=self.width, height=self.height)

    def setupView(self):
        self.parseSystem()
        self.view.clear()   # clear cache
        self.view = py3Dmol.view(width=self.width, height=self.height)

        self.view.addModelsAsFrames(self.system)
        self.view.setStyle({'model': -1}, {"cartoon": {'color': 'spectrum'}})
        self.view.zoomTo()
        # from py3Dmol.view.show
        self.view.updatejs = ''
        self.setHtml(self.view._make_html())

    def parseSystem(self):
        with open(self.pdbPath) as ifile:
            self.system = "".join([x for x in ifile])

    def changeFile(self):
        self.fileName = QFileDialog.getOpenFileName()[0]

    def showFile(self):
        if not self.fileName: return
        print(self.fileName, self.pdbPath)
        self.pdbPath = self.fileName
        print(self.fileName, self.pdbPath)

        self.setupView()

