import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox
from PySide2.QtWidgets import QFileDialog, QProgressBar

from PDBVisualizerSubWidget import PDBVisualizer
from pdbDownloader import PDBDownloader
from editorSettings import EditorSetting

import pypdb.clients.pdb.pdb_client


class Visualizer(QWidget):
    def __init__(self):

        self.SAVE_FILE_LOCATION = "tempFiles/"

        super().__init__()
        self.downloader = PDBDownloader()

        self.container        = QHBoxLayout()              # main container
        self.rightWrapper     = QVBoxLayout()              # right container
        self.buttonsContainer = QVBoxLayout()              # right-top container
        self.editor           = EditorSetting()            # right-bottom container
        self.editor.setShowFunction(self.showVisual)

        # --------------------- Widget definitions --------------------------#
        self.pdbVisualizer      = PDBVisualizer(500, 500)
        self.searchBar          = QLineEdit()
        self.selectButton       = QPushButton(text="Select")
        self.downloadProgressBar= QProgressBar() 
        # self.showButton         = QPushButton(text="Show")
        self.downloadButton     = QPushButton(text="download")
        self.comboBox           = QComboBox()
        # -------------------------------------------------------------------#

        self.comboBox.addItem("Search...")
        self.searchBar.setPlaceholderText("Search")


        self.downloadProgressBar.setValue(0)

        # --------------------- EVENT LISTENERS ------------------------------#
        self.searchBar.returnPressed.connect(self.updateComboBox)
        self.searchBar.returnPressed.connect(self.comboBox.showPopup)
        self.selectButton.clicked.connect(self.changeFile)
        self.downloadButton.clicked.connect(lambda: self.downloadPDB())
        # self.showButton.clicked.connect(self.showVisual)
        # --------------------------------------------------------------------#

        # left container

        # right-top container
        self.buttonsContainer.addWidget(self.searchBar)
        self.buttonsContainer.addWidget(self.comboBox)
        self.buttonsContainer.addWidget(self.downloadButton)
        self.buttonsContainer.addWidget(self.downloadProgressBar)
        self.buttonsContainer.addWidget(self.selectButton)
        # self.buttonsContainer.addWidget(self.showButton)
        self.buttonsContainer.addStretch(1)  # padding-bottom: max;

        # right wrapper
        self.rightWrapper.addLayout(self.buttonsContainer)   # right-top
        self.rightWrapper.addWidget(self.editor)             # right-bottom

        # left and right containers
        self.container.addWidget(self.pdbVisualizer)
        self.container.addLayout(self.rightWrapper)

        # adding main container
        self.setLayout(self.container)

        # setting 
        self.editor.colorSchemeChanged(0)
    



    # change setting and render the file
    def showVisual(self):
        self.pdbVisualizer.changeSetting(self.editor.getSettings())
        self.pdbVisualizer.showFile(directory=self.SAVE_FILE_LOCATION)
    
    # show search result id in combobox
    def updateComboBox(self):
        query = self.searchBar.text()
        if not query:
            self.comboBox.hide()
            return

        self.comboBox.clear()

        for i in self.getSearchList(query):
            self.comboBox.addItem(i)

        self.comboBox.show()

    # downloads PDB
    def downloadPDB(self, name="temp"):
        pdb_id = self.comboBox.currentText()
        self.pdbVisualizer.fileName = self.SAVE_FILE_LOCATION + name+".pdb"

        self.downloader.download(pdb_id, self.downloadProgressBar.setValue, directory=self.SAVE_FILE_LOCATION)

        self.selectedButtonText(pdb_id)
        self.showVisual()
        
    # search and returns list of ids
    def getSearchList(self, query, max_length=10):
        temp = pypdb.Query(query).search()
        if len(temp) >= 10: return temp[:max_length]
        return temp
    
    # changes text of select button to mark selected file
    def selectedButtonText(self, name):
        if not name: return
        self.selectButton.setText(name)
    
    # open file name dialogue
    def changeFile(self):
        self.pdbVisualizer.fileName = QFileDialog.getOpenFileName()[0]
        self.selectedButtonText(self.pdbVisualizer.fileName.split(".")[0].split('/')[-1])
        self.showVisual()


if __name__=="__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(100, 100, 700, 500)

    pdbWidget = Visualizer()
    window.setCentralWidget(pdbWidget)

    window.show()

    app.exec_()