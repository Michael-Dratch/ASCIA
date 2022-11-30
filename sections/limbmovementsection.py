from guicomponents.buttongroup import ButtonGroup
from sections.section import Section
from datatypes import NullType


class LimbMovementSection(Section):
    def __init__(self):
        super().__init__()
        self.rightKneeSelector = None
        self.leftKneeSelector = None
        self.rightAnkleSelector = None
        self.leftAnkleSelector = None
        self.rightHipSelector = None
        self.leftHipSelector = None
        self.layout = None

        self.buildSelectors()
        self.createLayout()

    def buildSelectors(self):
        self.buildHipSelectors()
        self.buildKneeSelectors()
        self.buildAnkleSelectors()
        self.addSelectorsToList()

    def createLayout(self):
        self.initializeLayout()
        self.layoutHeaderSection()
        self.layoutSelectorSection()
        self.layoutDividers()

    def layoutHeaderSection(self):
        self.layout.addWidget(self.buildHeader("Limb Movement"), 0, 0, 2, 8)
        self.layout.addWidget(self.createCenteredLabel("Hip"), 2, 0, 1, 2)
        self.layout.addWidget(self.createCenteredLabel("Knee"), 2, 3, 1, 2)
        self.layout.addWidget(self.createCenteredLabel("Ankle"), 2, 6, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 0, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 3, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 6, 1, 2)

    def layoutDividers(self):
        self.layout.addWidget(self.buildVerticalDivider(), 2, 2, 6, 1)
        self.layout.addWidget(self.buildVerticalDivider(), 2, 5, 6, 1)

    def layoutSelectorSection(self):
        self.layout.addWidget(self.leftHipSelector, 4, 0, 3, 1)
        self.layout.addWidget(self.rightHipSelector, 4, 1, 3, 1)
        self.layout.addWidget(self.leftKneeSelector, 4, 3, 3, 1)
        self.layout.addWidget(self.rightKneeSelector, 4, 4, 3, 1)
        self.layout.addWidget(self.leftAnkleSelector, 4, 6, 3, 1)
        self.layout.addWidget(self.rightAnkleSelector, 4, 7, 3, 1)

    def buildHipSelectors(self):
        self.leftHipSelector = ButtonGroup()
        self.leftHipSelector.buildLimbMovementButtonGroup(isDark=True)
        self.rightHipSelector = ButtonGroup()
        self.rightHipSelector.buildLimbMovementButtonGroup()

    def buildAnkleSelectors(self):
        self.leftAnkleSelector = ButtonGroup()
        self.leftAnkleSelector.buildLimbMovementButtonGroup(isDark=True)
        self.rightAnkleSelector = ButtonGroup()
        self.rightAnkleSelector.buildLimbMovementButtonGroup()

    def buildKneeSelectors(self):
        self.leftKneeSelector = ButtonGroup()
        self.leftKneeSelector.buildLimbMovementButtonGroup(isDark=True)
        self.rightKneeSelector = ButtonGroup()
        self.rightKneeSelector.buildLimbMovementButtonGroup()

    def addSelectorsToList(self):
        self.selectors.append(self.leftHipSelector)
        self.selectors.append(self.rightHipSelector)
        self.selectors.append(self.leftAnkleSelector)
        self.selectors.append(self.rightAnkleSelector)
        self.selectors.append(self.leftKneeSelector)
        self.selectors.append(self.rightKneeSelector)

    def getLeftHip(self):
        return self.leftHipSelector.getValue()

    def getRightHip(self):
        return self.rightHipSelector.getValue()

    def getLeftKnee(self):
        return self.leftKneeSelector.getValue()

    def getRightKnee(self):
        return self.rightKneeSelector.getValue()

    def getLeftAnkle(self):
        return self.leftAnkleSelector.getValue()

    def getRightAnkle(self):
        return self.rightAnkleSelector.getValue()

    def isComplete(self):
        if self.rightKneeSelector.getValue() == NullType.NULL:
            return False
        if self.leftKneeSelector.getValue() == NullType.NULL:
            return False
        if self.rightAnkleSelector.getValue() == NullType.NULL:
            return False
        if self.leftAnkleSelector.getValue() == NullType.NULL:
            return False
        if self.rightHipSelector.getValue() == NullType.NULL:
            return False
        if self.leftHipSelector.getValue() == NullType.NULL:
            return False
        return True
