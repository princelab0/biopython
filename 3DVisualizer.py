import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox
from PDBVisualizerSubWidget import PDBVisualizer
from PySide2.QtWidgets import QFileDialog, QProgressBar

from pdbDownloader import PDBDownloader

import pypdb.clients.pdb.pdb_client

class Visualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.downloader = PDBDownloader()

        self.container = QHBoxLayout()
        self.buttonsContainer = QVBoxLayout()

        # --------------------- Widget definitions --------------------------#
        self.pdbVisualizer= PDBVisualizer(500, 500)
        self.searchBar    = QLineEdit()
        self.selectButton = QPushButton(text="Select")
        self.downloadProgressBar = QProgressBar() 
        self.showButton   = QPushButton(text="Show")
        self.downloadButton = QPushButton(text="download")
        self.comboBox     = QComboBox()
        # -------------------------------------------------------------------#
        self.comboBox.addItem("Search...")
        self.searchBar.setPlaceholderText("Search")
        # self.comboBox.setEditable(True)

        self.downloadProgressBar.setValue(0)

        # --------------------- EVENT LISTENERS ------------------------------#
        # self.comboBox.activated.connect(self.downloadPDB)
        self.searchBar.returnPressed.connect(self.updateComboBox)
        self.searchBar.returnPressed.connect(self.comboBox.showPopup)
        self.selectButton.clicked.connect(self.changeFile)
        self.downloadButton.clicked.connect(lambda: self.downloadPDB())
        self.showButton.clicked.connect(self.pdbVisualizer.showFile)
        # --------------------------------------------------------------------#

        # left container
        self.container.addWidget(self.pdbVisualizer)

        # right container
        self.buttonsContainer.addWidget(self.searchBar)
        self.buttonsContainer.addWidget(self.comboBox)
        self.buttonsContainer.addWidget(self.downloadButton)
        self.buttonsContainer.addWidget(self.downloadProgressBar)
        self.buttonsContainer.addWidget(self.selectButton)
        self.buttonsContainer.addWidget(self.showButton)
        self.buttonsContainer.addStretch(1)  # padding-bottom: max;

        # right container
        self.container.addLayout(self.buttonsContainer)

        self.setLayout(self.container)

    
    def updateComboBox(self):
        # query = self.searchBar.currentText()
        query = self.searchBar.text()
        if not query:
            self.comboBox.hide()
            return

        self.comboBox.clear()

        for i in (temp:=self.getSearchList(query)):
            self.comboBox.addItem(i)

        self.comboBox.show()


    def downloadPDB(self, name="temp"):
        pdb_id = self.comboBox.currentText()

        self.downloader.download(pdb_id, self.downloadProgressBar.setValue)

        self.pdbVisualizer.fileName = name+".pdb"
        self.selectedButtonText(pdb_id)
        
            
    def getSearchList(self, query, max_length=10):
        temp = pypdb.Query(query).search()
        if len(temp) >= 10: return temp[:max_length]
        return temp
    
    def selectedButtonText(self, name):
        if not name: return
        self.selectButton.setText(name)
    
    def changeFile(self):
        self.pdbVisualizer.fileName = QFileDialog.getOpenFileName()[0]
        self.selectedButtonText(self.pdbVisualizer.fileName.split(".")[0].split('/')[-1])


app = QApplication(sys.argv)

window = QMainWindow()
window.setGeometry(100, 100, 700, 500)

pdbWidget = Visualizer()
window.setCentralWidget(pdbWidget)

window.show()

app.exec_()