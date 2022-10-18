from sections.section import Section
from buttongroup import ButtonGroup


class ToeSection(Section):
    def __init__(self):
        super().__init__()
        self.leftToeSelector = None
        self.rightToeSelector = None
        self.layout

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.leftToeSelector = ButtonGroup()
        self.leftToeSelector.buildFrequencyButtonGroup(isDark=True)
        self.rightToeSelector = ButtonGroup()
        self.rightToeSelector.buildFrequencyButtonGroup()

    def buildLayout(self):
        self.initializeLayout()
        self.layout.addWidget(self.buildHeader("Toe\nClear."), 0, 0, 3, 2)
        self.layout.addWidget(self.buildLeftRightLabel(), 2, 0, 1, 2)
        self.layout.addWidget(self.leftToeSelector, 3, 0, 4, 1)
        self.layout.addWidget(self.rightToeSelector, 3, 1, 4, 1)

    def getLeftToe(self):
        return self.leftToeSelector.getValue()

    def getRightToe(self):
        return self.rightToeSelector.getValue()
