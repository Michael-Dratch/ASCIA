from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import *
from sections.limbmovementsection import LimbMovementSection
from sections.trunkpositionsection import TrunkPositionSection
from sections.abdomensection import AbdomenSection
from sections.pawplacementsection import PawPlacementSection
from sections.steppingSection import SteppingSection
from sections.coordinationsection import CoordinationSection


class GUI:

    def __init__(self):
        self.window = None
        self.styleSheet = """
        QWidget#section {
            border: 1px solid black
            }
        QPushButton {
            border: 1px solid black
            }
            """

    def start(self):
        app = QApplication([])
        self.window = QWidget()
        self.window.setStyleSheet(self.styleSheet)
        self.window.setGeometry(100, 100, 600, 600)
        self.window.setWindowTitle("BBB Locomotor Rating Scale Grader")
        self.buildMainLayout()

        self.window.show()
        app.exec()

    def buildMainLayout(self):
        layout = QHBoxLayout()
        limbMovementSection = LimbMovementSection()
        limbMovementSection.setObjectName('section')
        limbMovementSection.setStyleSheet(self.styleSheet)
        limbMovementSection.setMaximumSize(200, 250)
        layout.addWidget(limbMovementSection)

        self.window.setLayout(layout)

        trunkPositionSection = TrunkPositionSection()
        trunkPositionSection.setObjectName('section')
        trunkPositionSection.setMaximumSize(200, 250)
        layout.addWidget(trunkPositionSection)

        abdomenSection = AbdomenSection()
        abdomenSection.setObjectName('section')
        abdomenSection.setMaximumSize(100, 250)
        layout.addWidget(abdomenSection)

        layout.addWidget(self.buildSectionDivider())

        pawSection = PawPlacementSection()
        pawSection.setObjectName('section')
        pawSection.setMaximumSize(200, 250)
        layout.addWidget(pawSection)

        steppingSection = SteppingSection()
        steppingSection.setObjectName('section')
        steppingSection.setMaximumSize(200, 250)
        layout.addWidget(steppingSection)

        layout.addWidget(self.buildSectionDivider())

        coordinationSection = CoordinationSection()
        coordinationSection.setObjectName('section')
        coordinationSection.setMaximumSize(100, 250)
        layout.addWidget(coordinationSection)

    def buildSectionDivider(self):
        divider = QFrame()
        divider.setFrameStyle(QFrame.Shape.VLine | QFrame.Shadow.Plain)
        divider.setMaximumSize(4, 300)
        divider.setMinimumSize(4, 300)
        divider.setLineWidth(20)
        return divider


if __name__ == "__main__":
    gui = GUI()
    gui.start()
