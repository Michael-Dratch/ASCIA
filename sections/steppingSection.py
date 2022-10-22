from sections.section import Section
from buttongroup import ButtonGroup
from datatypes import NullType


class SteppingSection(Section):
    def __init__(self):
        super().__init__()
        self.leftDorsal = None
        self.rightDorsal = None
        self.leftPlantar = None
        self.rightPlantar = None
        self.layout = None

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.leftDorsal = ButtonGroup()
        self.leftDorsal.buildFrequencyButtonGroup(isDark=True)
        self.rightDorsal = ButtonGroup()
        self.rightDorsal.buildFrequencyButtonGroup()
        self.leftPlantar = ButtonGroup()
        self.leftPlantar.buildFrequencyButtonGroup(isDark=True)
        self.rightPlantar = ButtonGroup()
        self.rightPlantar.buildFrequencyButtonGroup()

    def buildLayout(self):
        self.initializeLayout()
        self.layoutHeaderSection()
        self.layoutSelectorSection()
        self.layoutDividers()

    def layoutHeaderSection(self):
        self.layout.addWidget(self.buildHeader("Stepping"), 0, 0, 2, 5)
        self.layout.addWidget(self.buildHeader("Dorsal"), 2, 0, 1, 2)
        self.layout.addWidget(self.buildHeader("Plantar"), 2, 3, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 0, 1, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 3, 3, 1, 2)

    def layoutSelectorSection(self):
        self.layout.addWidget(self.leftDorsal, 4, 0, 4, 1)
        self.layout.addWidget(self.rightDorsal, 4, 1, 4, 1)
        self.layout.addWidget(self.leftPlantar, 4, 3, 4, 1)
        self.layout.addWidget(self.rightPlantar, 4, 4, 4, 1)

    def layoutDividers(self):
        self.layout.addWidget(self.buildVerticalDivider(), 2, 2, 6, 1)

    def getLeftDorsal(self):
        return self.leftDorsal.getValue()

    def getRightDorsal(self):
        return self.rightDorsal.getValue()

    def getLeftPlantar(self):
        return self.leftPlantar.getValue()

    def getRightPlantar(self):
        return self.rightPlantar.getValue()

    def isComplete(self):
        if self.leftDorsal.getValue() == NullType.NULL:
            return False
        if self.rightDorsal.getValue() == NullType.NULL:
            return False
        if self.leftPlantar.getValue() == NullType.NULL:
            return False
        if self.rightPlantar.getValue() == NullType.NULL:
            return False
        return True
