from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from sections.section import Section
from buttongroup import ButtonGroup


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

    def createLayout(self):
        self.initializeLayout()
        self.layout.addWidget(self.buildVerticalLabel("Abdomen"), 0, 0, 3, 1)
        self.layout.addWidget(self.abdomenSelector, 4, 0, 3, 1)

    def getAbdomen(self):
        return self.abdomenSelector.getValue()
