from sections.section import Section
from guicomponents.buttongroup import ButtonGroup
from datatypes import NullType


class PawPositionSection(Section):
    def __init__(self):
        super().__init__()
        self.leftInitialContactSelector = None
        self.rightInitialContactSelector = None
        self.leftLiftOffSelector = None
        self.rightLiftOffSelector = None

        self.layout = None

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.leftInitialContactSelector = ButtonGroup()
        self.leftInitialContactSelector.buildPawPositionButtonGroup(isDark=True)
        self.rightInitialContactSelector = ButtonGroup()
        self.rightInitialContactSelector.buildPawPositionButtonGroup()
        self.leftLiftOffSelector = ButtonGroup()
        self.leftLiftOffSelector.buildPawPositionButtonGroup(isDark=True)
        self.rightLiftOffSelector = ButtonGroup()
        self.rightLiftOffSelector.buildPawPositionButtonGroup()
        self.addSelectorsToList()

    def addSelectorsToList(self):
        self.selectors.append(self.leftInitialContactSelector)
        self.selectors.append(self.rightInitialContactSelector)
        self.selectors.append(self.leftLiftOffSelector)
        self.selectors.append(self.rightLiftOffSelector)

    def buildLayout(self):
        self.initializeLayout()
        self.layoutHeaderSection()
        self.layoutSelectorSection()
        self.layoutDividers()

    def layoutHeaderSection(self):
        self.layout.addWidget(self.buildHeader("Prodominant\nPaw Position"), 0, 0, 2, 5)
        self.layout.addWidget(self.buildHeader("Initial\nContact"), 2, 0, 1, 2)
        self.layout.addWidget(self.buildHeader("Lift\nOff"), 2, 3, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 0, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 3, 1, 2)

    def layoutSelectorSection(self):
        self.layout.addWidget(self.leftInitialContactSelector, 4, 0, 3, 1)
        self.layout.addWidget(self.rightInitialContactSelector, 4, 1, 3, 1)
        self.layout.addWidget(self.leftLiftOffSelector, 4, 3, 3, 1)
        self.layout.addWidget(self.rightLiftOffSelector, 4, 4, 3, 1)

    def layoutDividers(self):
        self.layout.addWidget(self.buildVerticalDivider(), 2, 2, 5, 1)

    def getLeftInitialContact(self):
        return self.leftInitialContactSelector.getValue()

    def getRightInitialContact(self):
        return self.rightInitialContactSelector.getValue()

    def getLeftLiftOff(self):
        return self.leftLiftOffSelector.getValue()

    def getRightLiftOff(self):
        return self.rightLiftOffSelector.getValue()

    def isComplete(self):
        if self.leftInitialContactSelector.getValue() == NullType.NULL:
            return False
        if self.rightInitialContactSelector.getValue() == NullType.NULL:
            return False
        if self.leftLiftOffSelector.getValue() == NullType.NULL:
            return False
        if self.rightLiftOffSelector.getValue() == NullType.NULL:
            return False
        return True
