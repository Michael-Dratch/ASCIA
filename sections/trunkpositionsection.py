from buttongroup import ButtonGroup
from sections.section import Section
from datatypes import NullType


class TrunkPositionSection(Section):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.sideSelector = None
        self.propSelector = None

        self.buildSelectors()
        self.createLayout()

    def buildSelectors(self):
        self.sideSelector = ButtonGroup()
        self.sideSelector.buildLeftRightMidButtonGroup()
        self.propSelector = ButtonGroup()
        self.propSelector.buildLeftRightButtonGroup()

    def createLayout(self):
        self.initializeLayout()
        self.layoutHeaderSection()
        self.layoutSelectorSection()
        self.layoutDividers()

    def layoutHeaderSection(self):
        self.layout.addWidget(self.buildHeader("Trunk\nPosition"), 0, 0, 3, 5)
        self.layout.addWidget(self.buildHeader("Side"), 3, 0, 1, 2)
        self.layout.addWidget(self.buildHeader("Prop"), 3, 3, 1, 2)

    def layoutSelectorSection(self):
        self.layout.addWidget(self.sideSelector, 4, 0, 2, 2)
        self.layout.addWidget(self.propSelector, 4, 2, 1, 3)

    def layoutDividers(self):
        self.layout.addWidget(self.buildVerticalDivider(), 3, 2, 5, 1)

    def getSide(self):
        return self.sideSelector.getValue()

    def getProp(self):
        return self.propSelector.getValue()

    def isComplete(self):
        if self.sideSelector.getValue() == NullType.NULL:
            return False
        if self.propSelector.getValue() == NullType.NULL:
            return False
        return True
