class ViewGenerator:
    def __init__(self, pdb_path=""):
        self.pdb_path = pdb_path
        self.settings = {
            "style" : "backbone",
            "color" : "white",
            "colorscheme" : "chain"
        }
        self.template = """import nglview"""


    def getCode(self):
        # return "print('hello world')"
#         return """
# """
        return self.getFinalCode()
    
    def setPDB(self, pdb_path):
        self.pdb_path = pdb_path

    def getFinalCode(self):
        code = self.template
        if self.pdb_path:
            code += f"\nview=nglview.show_structure_file('temp.pdb')\n"
        else:
            code += f"\nview=nglview.demo()"
        code += """
view.representations = [
    {'type': '""" + self.settings['style'] + """', 'params': {
        'sele': 'protein', 'color': '"""+ self.settings['color'] + """'
    }}
]
view"""

        return code


    def changeStyle(self, style):
        self.settings["style"] = style
    
    def changeColor(self, color):
        self.settings["color"] = color

    def changeColorScheme(self, colorscheme):
        self.settings["colorscheme"] = colorscheme

    def changeSettings(self, settings):
        if settings['colorscheme']!="none":
            settings['color'] = settings['colorscheme']
        self.settings = settings

    def changePath(self, path):
        self.path = path
