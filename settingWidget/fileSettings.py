from PySide2.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QColorDialog, QPushButton, QLineEdit, QProgressBar, QFileDialog

from pdbDownloader import PDBDownloader
import pypdb.clients.pdb.pdb_client

class FileSettings(QWidget):
    def __init__(self, path=""):
        super().__init__()
        self.path = path
        self._layout = QVBoxLayout()
        self.color = "#fff"     # default color is black
        self.showFunction = lambda : 0  # temp function

        
        self.downloader = PDBDownloader()
        # -------------------- widgets ---------------------- #
        self.searchBar           = QLineEdit()
        self.selectButton        = QPushButton(text="Select")
        self.downloadProgressBar = QProgressBar()
        self.downloadButton      = QPushButton(text="download")
        self.comboBox            = QComboBox()
        # --------------------------------------------------- #

        self.comboBox.addItem("Search...")
        self.searchBar.setPlaceholderText("Search")

        # --------------------- EVENT LISTENERS ------------------------------#
        self.searchBar.returnPressed.connect(self.updateComboBox)
        self.searchBar.returnPressed.connect(self.comboBox.showPopup)
        self.selectButton.clicked.connect(self.changeFile)
        self.downloadButton.clicked.connect(lambda: self.downloadPDB())
        # --------------------------------------------------------------------#

        # -------------------- adding widgets  ---------------------- #
        self._layout.addWidget(self.searchBar)
        self._layout.addWidget(self.comboBox)
        self._layout.addWidget(self.downloadButton)
        self._layout.addWidget(self.downloadProgressBar)
        self._layout.addWidget(self.selectButton)
        self._layout.addStretch(1)  # padding-bottom: max;
        # ----------------------------------------------------------- #


        self.downloadProgressBar.setValue(0)

        self.setLayout(self._layout)


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
    def downloadPDB(self):
        pdb_id = self.comboBox.currentText()
        # self.path = path

        self.downloader.download(pdb_id, self.downloadProgressBar.setValue, directory=self.path)

        self.selectedButtonText(pdb_id)
        self.showFunction()
        
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
        self.temppath = QFileDialog.getOpenFileName()[0]

        with open("./tempFiles/temp.pdb", "w") as fp:
            fp.write(open(self.temppath, "r").read())

        self.selectedButtonText(self.path.split(".")[0].split('/')[-1])
        self.showFunction()

    def setShowFunction(self, func):
        self.showFunction = func