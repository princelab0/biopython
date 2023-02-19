from PySide2.QtWebEngineWidgets import QWebEngineView

import py3Dmol
import os



class PDBVisualizer(QWebEngineView):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.setMinimumSize(self.width+20, self.height+20)

        self.pdbPath = ""
        self.fileName = ""

        self.system = None
        self.setting = {}

        self.view = py3Dmol.view(width=self.width, height=self.height)

    def setupView(self):
        self.parseSystem()
        self.view.clear()   # clear cache
        # self.view = py3Dmol.view(width=self.width, height=self.height)

        self.view.addModelsAsFrames(self.system)
        self.view.setStyle({'model': -1}, {self.setting["style"]: {'color': self.setting["color"]}})
        self.view.zoomTo()
        # from py3Dmol.view.show
        self.view.updatejs = ''
        temp = self.view._make_html()
        # saving html to a file
        with open("temp.html", "w") as file:
            file.write(temp)
        path =(os.path.dirname(os.path.realpath(__file__)) + "\\temp.html").replace("\\","/")
        # loading the saved html
        self.load(path)

    def parseSystem(self):
        with open(self.pdbPath) as ifile:
            self.system = "".join([x for x in ifile])

    def showFile(self):
        if not self.fileName: return
        self.pdbPath = self.fileName

        self.setupView()

    def changeSetting(self, setting):
        self.setting = setting