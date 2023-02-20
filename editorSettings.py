from PySide2.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QColorDialog, QPushButton

class EditorSetting(QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QVBoxLayout()
        self.color = "#000"     # default color is black

        # combo init
        self.styleBox = ComboBox("style", ["cartoon", "stick", "line"])
        # self.colorBox = ComboBox("color", ["spectrum", "black", "red", "green", "blue", "#aabb00"])
        self.colorBox = QPushButton("color")
        self.colorScheme = ComboBox("colorscheme", ["None", "rainbow", "chain", "ssPyMol", "ssJmol", "greenCarbon"])

        # event handlers
        self.colorBox.clicked.connect(self.getColor)
        self.colorScheme.comboBox.currentIndexChanged.connect(self.colorSchemeChanged)

        # adding widgets
        self._layout.addLayout(self.styleBox)
        self._layout.addWidget(self.colorBox)
        self._layout.addLayout(self.colorScheme)

        self.setLayout(self._layout)

        self.colorIndication()      # to change color
        self.colorSchemeChanged(0)


    def colorSchemeChanged(self, t):
        if t==0: self.colorBox.setEnabled(True)
        else:    self.colorBox.setEnabled(False)

    def getColor(self):
        self.color = QColorDialog().getColor().name()
        self.colorIndication()

    
    def colorIndication(self):
        self.colorBox.setStyleSheet(f"background-color: {self.color}")

    def getSettings(self):
        temp = {
            "style" : self.styleBox.currentText(),
            "color" : self.color,
            "colorscheme" : self.colorScheme.currentText()
        }
        return temp
    

class ComboBox(QHBoxLayout):
    def __init__(self, name, options):
        super().__init__()
        self.label = QLabel(name)
        self.comboBox = QComboBox()
        self.comboBox.addItems(options)

        self.addWidget(self.label)
        self.addWidget(self.comboBox)

    def currentText(self):
        return self.comboBox.currentText()