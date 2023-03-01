# modified qtvoila.py to work with PySide2
from qtvoila import QtVoila
from PySide2.QtWidgets import QMainWindow, QApplication
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.voila_widget = QtVoila(
            parent=None,
            temp_dir="./tempFiles",
            external_notebook=None,
            strip_sources=True
        )      
        
        code = "import nglview\nview=nglview.demo()\nview"

        self.voila_widget.add_notebook_cell(code=code, cell_type='code')

        self.setCentralWidget(self.voila_widget)

        self.voila_widget.run_voila()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Main()
    sys.exit(app.exec_())
