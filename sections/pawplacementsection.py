from PyQt6.QtWidgets import QFrame
from sections.section import Section
from buttongroup import ButtonGroup


class PawPlacementSection(Section):
    def __init__(self):
        super().__init__()
        self.sweepSelector = None
        self.withOutSupportSelector = None
        self.withSupportSelecor = None
        self.layout = None

        self.buildSelectors()
        self.buildLayout()

    def buildSelectors(self):
        self.sweepSelector = ButtonGroup()
        self.sweepSelector.buildLeftRightButtonGroup()
        self.withOutSupportSelector = ButtonGroup()
        self.withOutSupportSelector.buildLeftRightButtonGroup()
        self.withSupportSelecor = ButtonGroup()
        self.withSupportSelecor.buildLeftRightButtonGroup()

    def buildLayout(self):
        self.initializeLayout()
        self.layoutHeaderSection()
        self.layoutSelectorSection()
        self.layoutDividers()

    def layoutHeaderSection(self):
        self.layout.addWidget(self.buildHeader("Paw\nPlacement"), 0, 0, 2, 8)
        self.layout.addWidget(self.buildHeader("Plantar Pl."), 2, 3, 1, 5)
        self.layout.addWidget(self.buildHeader("Sweep"), 3, 0, 1, 2)
        self.layout.addWidget(self.buildHeader("W/O\nSupp."), 3, 3, 1, 2)
        self.layout.addWidget(self.buildHeader("W\nSupp."), 3, 6, 1, 2)

    def layoutSelectorSection(self):
        self.layout.addWidget(self.sweepSelector, 4, 0, 1, 2)
        self.layout.addWidget(self.withOutSupportSelector, 4, 3, 1, 2)
        self.layout.addWidget(self.withSupportSelecor, 4, 6, 1, 2)

    def layoutDividers(self):
        self.layout.addWidget(self.buildVerticalDivider(), 3, 2, 4, 1)
        self.layout.addWidget(self.buildVerticalDivider(), 3, 5, 4, 1)

    def getSweep(self):
        return self.sweepSelector.getValue()

    def getWithOutSupport(self):
        return self.withOutSupportSelector.getValue()

    def getWithSupport(self):
        return self.withSupportSelecor.getValue()
