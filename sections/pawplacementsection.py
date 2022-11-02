from PyQt6.QtWidgets import QFrame
from sections.section import Section
from guicomponents.buttongroup import ButtonGroup
from datatypes import NullType


class PawPlacementSection(Section):
    def __init__(self):
        super().__init__()
        self.leftPawPlacementSelector = None
        self.rightPawPlacementSelector = None

        self.layout = None

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.leftSweepSelector = ButtonGroup()
        self.leftSweepSelector.buildSweepButton("L", isDark=True)
        self.rightSweepSelector = ButtonGroup()
        self.rightSweepSelector.buildSweepButton("R")
        self.leftSupportSelector = ButtonGroup()
        self.leftSupportSelector.buildSupportButtonGroup("L", isDark=True)
        self.rightSupportSelector = ButtonGroup()
        self.rightSupportSelector.buildSupportButtonGroup("R")

    def buildLayout(self):
        self.initializeLayout()
        self.layoutHeaderSection()
        self.layoutSelectorSection()
        self.layoutDividers()

    def layoutHeaderSection(self):
        self.layout.addWidget(self.buildHeader("Paw\nPlacement"), 0, 0, 2, 8)
        self.layout.addWidget(self.buildHeader("Plantar Pl."), 2, 3, 1, 5)
        self.layout.addWidget(self.buildHeader("Sweep"), 3, 0, 1, 2)
        self.layout.addWidget(self.buildHeader("W/O\nSupp."), 3, 3, 1, 2)
        self.layout.addWidget(self.buildHeader("W\nSupp."), 3, 6, 1, 2)

    def layoutSelectorSection(self):
        self.layout.addWidget(self.leftSweepSelector, 4, 0, 1, 1)
        self.layout.addWidget(self.rightSweepSelector, 4, 1, 1, 1)
        self.layout.addWidget(self.leftSupportSelector, 4, 2, 1, 6)
        self.layout.addWidget(self.rightSupportSelector, 5, 2, 1, 6)

    def layoutDividers(self):
        self.layout.addWidget(self.buildVerticalDivider(), 3, 2, 4, 1)
        self.layout.addWidget(self.buildVerticalDivider(), 3, 5, 4, 1)

    def getLeftSweep(self):
        return self.leftSweepSelector.getValue()

    def getRightSweep(self):
        return self.rightSweepSelector.getValue()

    def getLeftSupport(self):
        return self.leftSupportSelector.getValue()

    def getRightSupport(self):
        return self.rightSupportSelector.getValue()

    def isComplete(self):
        if self.leftSupportSelector.getValue() == NullType.NULL:
            return False
        if self.rightSupportSelector.getValue() == NullType.NULL:
            return False
        return True
