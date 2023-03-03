class ViewGenerator:
    def __init__(self, pdb_path=""):
        self.pdb_path = pdb_path
        self.settings = {
            "style" : "backbone",
            "color" : "white",
            "colorscheme" : "chain"
        }
        self.template = """import nglview
view=nglview.demo()
"""


    def getCode(self):
        return self.getFinalCode()
    
    def getFinalCode(self):
        code = self.template + """       
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
        print("HELOW", settings['colorscheme'])
        if settings['colorscheme']!="none":
            settings['color'] = settings['colorscheme']
        self.settings = settings