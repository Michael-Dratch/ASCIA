from sections.section import Section
from guicomponents.buttongroup import ButtonGroup
from datatypes import NullType


class TailSection(Section):
    def __init__(self):
        super().__init__()
        self.tailSelector = None
        self.layout = None

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.tailSelector = ButtonGroup()
        self.tailSelector.buildUpDownButtonGroup()

    def buildLayout(self):
        self.initializeLayout()
        self.layout.addWidget(self.buildHeader("Tail"), 0, 0, 4, 1)
        self.layout.addWidget(self.tailSelector, 4, 0, 2, 1)

    def getTail(self):
        return self.tailSelector.getValue()

    def isComplete(self):
        if self.tailSelector.getValue() == NullType.NULL:
            return False
        return True
