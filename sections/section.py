from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter


class Section(QFrame):
    def __init__(self):
        super().__init__()
        self.selectors = []

    def initializeLayout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def buildLeftRightLabel(self):
        label = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        label.setLayout(layout)
        layout.addWidget(self.createCenteredLabel("L"))
        layout.addWidget(self.createCenteredLabel("R"))
        return label

    def createCenteredLabel(self, text):
        jointLabel = QLabel(text)
        jointLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return jointLabel

    def buildHorizontalDivider(self):
        hDivider = QFrame()
        hDivider.setFrameStyle(QFrame.Shape.HLine | QFrame.Shadow.Plain)
        hDivider.setLineWidth(2)
        return hDivider

    def buildVerticalDivider(self):
        vDivider = QFrame()
        vDivider.setFrameStyle(QFrame.Shape.VLine | QFrame.Shadow.Plain)
        vDivider.setLineWidth(2)
        return vDivider

    def buildHeader(self, text):
        header = self.createCenteredLabel(text)
        return header

    def buildVerticalLabel(self, text, isNarrow=False):
        labelContainer = QWidget()
        layout = QHBoxLayout()
        labelContainer.setLayout(layout)
        label = VerticalLabel(text, isNarrow)
        layout.addWidget(label)
        return labelContainer

    def resetSelectors(self):
        for selector in self.selectors:
            selector.reset()


class VerticalLabel(QWidget):
    def __init__(self, text=None, isNarrow=False):
        super(self.__class__, self).__init__()
        self.text = text
        self.narrow = isNarrow

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.narrow:
            painter.translate(10, 90)
        else:
            painter.translate(20, 100)
        painter.rotate(-90)
        if self.text:
            painter.drawText(0, 0, self.text)
        painter.end()
