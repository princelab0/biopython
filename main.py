import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

from qtvoila import QtVoila
from visualizer_template_generator.generator import ViewGenerator

from settingWidget.editorSettings import EditorSetting
from settingWidget.fileSettings   import FileSettings

class Main(QWidget):
    def __init__(self):
        super().__init__()
        # all components
        self.generator = ViewGenerator()
        self.editorSetting = EditorSetting()
        self.fileSetting = FileSettings()

        self.visualizer = QtVoila(
            parent=None,
            temp_dir="./tempFiles",
            external_notebook=None,
            strip_sources=True
        )

        self.visualizer.add_notebook_cell(code=self.generator.getCode(), cell_type='code')

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

        self.visualizer.run_voila()

        

    def update(self):
        self.visualizer.clear()
        self.visualizer.add_notebook_cell(code=self.generator.getCode(), cell_type='code')
        self.visualizer.run_voila()

    def actionListenerFromEditor(self):
        self.generator.changeColor(self.editorSetting.color)
        self.generator.changeSettings(self.editorSetting.getSettings())
        self.update()


if __name__=="__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(100, 100, 700, 500)

    pdbWidget = Main()
    window.setCentralWidget(pdbWidget)

    window.show()

    app.exec_()