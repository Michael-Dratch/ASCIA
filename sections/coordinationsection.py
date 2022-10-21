from sections.section import Section
from buttongroup import ButtonGroup


class CoordinationSection(Section):
    def __init__(self):
        super().__init__()
        self.coordinationSelector = None
        self.layout = None

        self.buildSelectors()
        self.buildLayout()
        self.setMinimumSize(30, 250)
        self.setMaximumSize(30, 250)

    def buildSelectors(self):
        self.coordinationSelector = ButtonGroup()
        self.coordinationSelector.buildFrequencyButtonGroup()

    def buildLayout(self):
        self.initializeLayout()
        self.layout.addWidget(self.buildVerticalLabel("Coordination", isNarrow=True), 0, 0, 4, 1)
        self.layout.addWidget(self.coordinationSelector, 3, 0, 4, 1)

    def getCoordination(self):
        return self.coordinationSelector.getValue()
