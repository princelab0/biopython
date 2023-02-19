from PySide2.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout

class EditorSetting(QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QVBoxLayout()

        # combo init
        self.styleBox = ComboBox("style", ["cartoon", "stick", "line"])
        self.colorBox = ComboBox("color", ["spectrum", "black", "red", "green", "blue"])
        self.colorScheme = ComboBox("colorscheme", ["rainbow", "chain", "ssPyMol", "ssJmol"])


        # adding widgets
        self._layout.addLayout(self.styleBox)
        self._layout.addLayout(self.colorBox)
        self._layout.addLayout(self.colorScheme)

        self.setLayout(self._layout)

    def getSettings(self):
        temp = {
            "style" : self.styleBox.currentText(),
            "color" : self.colorBox.currentText(),
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