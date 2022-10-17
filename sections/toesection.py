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
        self.leftToeSelector.buildP