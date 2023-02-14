import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from PySide2.QtWebEngineWidgets import QWebEngineView

import py3Dmol

class PDBVisualizer(QWebEngineView):
    def __init__(self, width, height, pdbPath):
        super().__init__()

        self.width = width
        self.height = height
        self.setFixedSize(self.width+20, self.height+20)

        self.pdbPath = pdbPath
        self.fileName = ""

        self.system = None

        self.view = py3Dmol.view(width=self.width, height=self.height)

    def setupView(self):
        self.parseSystem()
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
        print(self.fileName)

    def showFile(self):
        print(self.fileName, self.pdbPath)
        if not self.fileName: return
        self.pdbPath = self.fileName
        print(self.fileName, self.pdbPath)

        self.setupView()



class Visualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.container = QHBoxLayout()
        self.buttonsContainer = QVBoxLayout()


        self.pdbVisualizer = PDBVisualizer(500, 500, "")
        self.selectButton = QPushButton(text="Select")
        self.showButton   = QPushButton(text="Show")

        self.selectButton.clicked.connect(self.pdbVisualizer.changeFile)
        self.showButton.clicked.connect(self.pdbVisualizer.showFile)

        self.container.addWidget(self.pdbVisualizer)

        self.buttonsContainer.addWidget(self.selectButton)
        self.buttonsContainer.addWidget(self.showButton)
        self.buttonsContainer.addStretch(1)

        self.container.addLayout(self.buttonsContainer)

        self.setLayout(self.container)


app = QApplication(sys.argv)

window = QMainWindow()
window.setGeometry(100, 100, 700, 500)

pdbWidget = Visualizer()
window.setCentralWidget(pdbWidget)

window.show()

app.exec_()