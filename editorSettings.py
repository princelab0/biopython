from PySide2.QtWidgets import QWidget, QComboBox, QVBoxLayout

class EditorSetting(QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QVBoxLayout()

        # buttons initializers
        self.styleBox = QComboBox()
        self.colorBox = QComboBox()

        self.styleBox.addItems(["cartoon", "stick", "line"])
        self.colorBox.addItems(["spectrum", "black", "red", "green", "blue"])

        # adding widgets
        self._layout.addWidget(self.styleBox)
        self._layout.addWidget(self.colorBox)

        self.setLayout(self._layout)

    def getSettings(self):
        temp = {
            "style" : self.styleBox.currentText(),
            "color" : self.colorBox.currentText()
        }
        return temp