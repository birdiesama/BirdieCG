import random
import maya.cmds as cmds
from PySide2 import QtWidgets
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

class ColorCubeUI(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ColorCubeUI, self).__init__(parent=parent)
        
        def create_colored_cubes():
            for _ in range(10):
                cube = cmds.polyCube()[0]
                cmds.setAttr(cube + ".translate", *(random.uniform(-5, 5) for _ in range(3)), type="double3")
                cmds.setAttr(cube + ".scale", *(random.uniform(.5, 3) for _ in range(3)), type="double3")
                lambert = cmds.shadingNode("lambert", asShader=True)
                cmds.setAttr(lambert + ".color", *(random.uniform(0, 1) for _ in range(3)), type="double3")
                cmds.select(cube)
                cmds.hyperShade(assign=lambert)
        
        self.create_button = QtWidgets.QPushButton("Create Colored Cubes")
        self.create_button.clicked.connect(create_colored_cubes)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.create_button)

def create_ui():
    ui = ColorCubeUI()
    ui.show(dockable=True)

create_ui()

"""
These are the prompts I did to create this tool:

Write a maya python tool to create a cube then randomize its color. Encapsulate it into a function. Write a UI to execute the function, and launch it.
### Need to be very specific about what you want

Cannot find procedure "createWindow".
Start of trace: (command window: line 1).
createWindow (command window: line 1). 
### You can copy and paste the command to the chat so it can reiterate the code

instead of change color of the cube, create a lambert then assign the color to the cube 
### fixing bugs

write the UI again, but using PySide 
### change how the UI is written

The UI appeared quickly and closed itself. 
### Now the UI launched and quickly disappeared, trying to fix the bug

# Error: maya.standalone.initialize() can not be call inside of Maya.
# # Traceback (most recent call last):
# #   File "<maya console>", line 6, in <module>
# # RuntimeError: maya.standalone.initialize() can not be call inside of Maya.

Make it so that the script can be run in the script editor
### Make the code runable through the script editor

The UI was launched then quickly disappeared

reiterate the script so it creates 10 cube with randomized position between (-5, -5, -5) and (5, 5, 5) and radomized size between .5 and 3
### adding more functions to the tool

Remove all of the comments and rewrite the code without any comments
### Now hitting the character limit of the trail version of chatGPT, trying to get around it.

optimize the code so it is shorter
"""
