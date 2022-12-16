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
