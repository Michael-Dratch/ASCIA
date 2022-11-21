from sections.section import Section
from guicomponents.buttongroup import ButtonGroup
from datatypes import NullType


class InstabilitySection(Section):
    def __init__(self):
        super().__init__()
        self.instabilitySelector = None
        self.layout = None

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.instabilitySelector = ButtonGroup()
        self.instabilitySelector.buildStabilityButtonGroup()

    def buildLayout(self):
        self.initializeLayout()
        self.layout.addWidget(self.buildVerticalLabel("Trunk Instability"), 0, 0, 4, 1)
        self.layout.addWidget(self.instabilitySelector, 4, 0, 2, 1)

    def getTrunkInstability(self):
        return self.instabilitySelector.getValue()

    def isComplete(self):
        if self.instabilitySelector.getValue() == NullType.NULL:
            return False
        return True
