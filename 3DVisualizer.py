import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PySide2.QtWebEngineWidgets import QWebEngineView

import py3Dmol

class PDBVisualizer(QWebEngineView):
    def __init__(self, width, height, pdbPath):
        super().__init__()

        self.width = width
        self.height = height
        self.setGeometry(100, 100, self.width+20, self.height+20)

        self.pdbPath = pdbPath

        self.system = None
        self.parseSystem()

        self.view = None
        self.setupView()

        self.setHtml(self.view._make_html())



    def setupView(self):
        self.view = py3Dmol.view(width=self.width, height=self.height)
        self.view.addModelsAsFrames(self.system)
        self.view.setStyle({'model': -1}, {"cartoon": {'color': 'spectrum'}})
        self.view.zoomTo()
        # from py3Dmol.view.show
        self.view.updatejs = ''


    def parseSystem(self):
        with open(self.pdbPath) as ifile:
            self.system = "".join([x for x in ifile])



app = QApplication(sys.argv)

window = QMainWindow()
pdbWidget = PDBVisualizer(500, 500, "covid.pdb")
window.setCentralWidget(pdbWidget)

window.show()

app.exec_()