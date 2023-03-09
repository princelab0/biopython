import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

from visualizer_template_generator.generator import ViewGenerator

from settingWidget.editorSettings import EditorSetting
from settingWidget.fileSettings   import FileSettings

import backend
from backend.Viewer import Viewer
import time

class Main(QWidget):
    def __init__(self):
        super().__init__()
        # all components
        self.generator = ViewGenerator()
        self.editorSetting = EditorSetting()
        self.fileSetting = FileSettings()

        # Viewer Widget
        self.visualizer = Viewer(backend.PORT)
        self.tempButton = QPushButton("click")
        # initialize
        self.generator.changeSettings(self.editorSetting.getSettings())
        backend.nbWriter.addCode(self.generator.getCode())

        # main wrapper
        self.layoutManager = QHBoxLayout()
        #left-wrapper
        self.leftWrapper = QVBoxLayout()
        self.leftWrapper.addWidget(self.visualizer)

        # right-wrapper
        self.rightWrapper = QVBoxLayout()
        self.rightWrapper.addWidget(self.fileSetting)
        self.rightWrapper.addWidget(self.editorSetting)


        self.layoutManager.addLayout(self.leftWrapper)
        self.layoutManager.addLayout(self.rightWrapper)
        # event listeners
        self.editorSetting.setShowFunction(self.actionListenerFromEditor)
        self.setLayout(self.layoutManager)
        # self.setLayout(self.leftWrapper)
        backend.voilaRunner.start()
        self.visualizer.loadUrl()

        

    def update(self):
        backend.nbWriter.addCode(self.generator.getCode())
        # backend.voilaRunner.start()
        self.visualizer.reload()
        # self.visualizer.clear()
        # self.visualizer.add_notebook_cell(code=self.generator.getCode(), cell_type='code')
        # self.visualizer.run_voila()

    def actionListenerFromEditor(self):
        self.generator.changeSettings(self.editorSetting.getSettings())
        self.update()

def on_close():
    pass

if __name__=="__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(100, 100, 700, 500)

    pdbWidget = Main()
    window.setCentralWidget(pdbWidget)

    window.show()

    app.aboutToQuit.connect(backend.voilaRunner.killExistingProcesses)
    app.exec_()