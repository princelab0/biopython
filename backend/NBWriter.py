import nbformat as nbf

class NBWriter:
    def __init__(self, path=""):
        self.path = path
        self.nb = nbf.v4.new_notebook()

    def addCode(self, code):
        cell = nbf.v4.new_code_cell(source=code)
        self.nb['cells'] = [cell]

        self.save()
    
    def save(self):
        nbf.write(self.nb, 'my_notebook.ipynb')
