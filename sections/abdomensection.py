from sections.section import Section
from guicomponents.buttongroup import ButtonGroup
from datatypes import NullType


class AbdomenSection(Section):
    def __init__(self):
        super().__init__()
        self.abdomenSelector = None
        self.layout = None

        self.buildSelectors()
        self.createLayout()

    def buildSelectors(self):
        self.abdomenSelector = ButtonGroup()
        self.abdomenSelector.buildAbdomenButtonGroup()
        self.selectors.append(self.abdomenSelector)

    def createLayout(self):
        self.initializeLayout()
        self.layout.addWidget(self.buildVerticalLabel("Abdomen"), 0, 0, 3, 1)
        self.layout.addWidget(self.abdomenSelector, 4, 0, 3, 1)

    def getAbdomen(self):
        return self.abdomenSelector.getValue()

    def isComplete(self):
        if self.abdomenSelector.getValue() == NullType.NULL:
            return False
        return True
