# biopython
paradox extension for the biopython.


## Visualizer Methods (3DVisualizer.py)
PySide2 -> QtWidgets -> QWidget -> Visualizer
1. ```updateComboBox()```
    > clears and updates comboBox/dropdown

2. ```downloadPDB(name="temp")```
   > tries to download a file with index selected in comboBox/dropdown  

3. ```getSearchList(query, max_length=10)```
   > searches the given query from the **pydb** library and returns *max_length* number of queries

4. ```changeFile()```
   > triggers FileDialog to get input filename


## PDBVisualizer Methods (PDBVisualizerSubWidget.py)
Python2 -> QtWebEngineWidgets -> QWebEngineView -> PDBVisualizer

1. ```__init__(width, height)```
   > initializes view and other variables

2. ```setupView()```
   > extracts html component and sets it to the class

3. ```parseSystem()```
   > parses pdb file

4. ```showFile()```
   > calls setupView()


> **Note**: there are a lot of files which doesn't render from py3Dmol