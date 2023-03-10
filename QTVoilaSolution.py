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
        
        code = """import nglview
view=nglview.demo()
view.layout.width = "500px"
view.layout.height = "500px"
view.layout.resizable = False
view"""
#         code = """
# import matplotlib.pyplot as plt

# # Data for x-axis
# x = [1, 2, 3, 4, 5]

# # Data for y-axis
# y = [1, 4, 9, 16, 25]

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Plot the data
# ax.plot(x, y)

# # Set the labels for the x and y axis
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')

# # Set the title of the plot
# ax.set_title('Simple Line Graph')

# # Show the plot
# plt.show()
# """
#         code = """
# import py3Dmol

# with open("./example-pdb/structure.pdb") as ifile:
#     system = "".join([x for x in ifile])

# view = py3Dmol.view(width=400, height=300)
# view.addModelsAsFrames(system)
# view.setStyle({'model': -1}, {"line": {'color': 'chain', "colorscheme": "greenCarbon"}})
# view.zoomTo()
# view.show()

# """
        self.voila_widget.add_notebook_cell(code=code, cell_type='code')

        self.setCentralWidget(self.voila_widget)

        self.voila_widget.run_voila()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Main()
    sys.exit(app.exec_())
