from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from buttons import Button
from datatypes import *


class ButtonGroup(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.value = None
        self.initializeButtonGroup()
        self.BUTTON_SIZE = QSize(25, 25)
        self.BUTTON_SIZE_LARGE = QSize(50, 25)

    def initializeButtonGroup(self):
        self.buttons = {}

    def buildLimbMovementButtonGroup(self, isDark=False):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        noneButton = self.buildButton("Ø", MovementType.NONE, isDark)
        slightButton = self.buildButton("S", MovementType.SLIGHT, isDark)
        extensiveButton = self.buildButton("E", MovementType.EXTENSIVE, isDark)
        self.layout.addWidget(noneButton)
        self.layout.addWidget(slightButton)
        self.layout.addWidget(extensiveButton)
        self.buttons[MovementType.NONE] = noneButton
        self.buttons[MovementType.SLIGHT] = slightButton
        self.buttons[MovementType.EXTENSIVE] = extensiveButton

    def buildLeftRightButtonGroup(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        leftButton = self.buildButton("L", SideType.LEFT, isDark=True)
        rightButton = self.buildButton("R", SideType.RIGHT)
        self.layout.addWidget(leftButton, 0, 0)
        self.layout.addWidget(rightButton, 0, 1)
        self.buttons[SideType.LEFT] = leftButton
        self.buttons[SideType.RIGHT] = rightButton

    def buildLeftRightMidButtonGroup(self):
        self.buildLeftRightButtonGroup()
        midButton = self.buildButton("Mid", SideType.MIDDLE)
        midButton.setFixedSize(self.BUTTON_SIZE_LARGE)
        self.layout.addWidget(midButton, 1, 0, 1, 2)
        self.buttons[SideType.MIDDLE] = midButton

    def buildAbdomenButtonGroup(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        dragButton = self.buildButton("Drag", AbdomenType.DRAG)
        self.setButtonSize(dragButton, self.BUTTON_SIZE_LARGE)
        parallelButton = self.buildButton("Parallel", AbdomenType.PARALLEL)
        self.setButtonSize(parallelButton, self.BUTTON_SIZE_LARGE)
        highButton = self.buildButton("High", AbdomenType.HIGH)
        self.setButtonSize(highButton, self.BUTTON_SIZE_LARGE)
        self.layout.addWidget(dragButton)
        self.layout.addWidget(parallelButton)
        self.layout.addWidget(highButton)
        self.buttons[AbdomenType.DRAG] = dragButton
        self.buttons[AbdomenType.PARALLEL] = parallelButton
        self.buttons[AbdomenType.HIGH] = highButton

    def setButtonSize(self, button, size):
        button.setMaximumSize(size)
        button.setMinimumSize(size)

    def buildFrequencyButtonGroup(self, isDark=False):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        neverButton = self.buildButton("Ø", FrequencyType.NEVER, isDark)
        occasionalButton = self.buildButton("O", FrequencyType.OCCASIONAL, isDark)
        frequentButton = self.buildButton("F", FrequencyType.FREQUENT, isDark)
        consistentButton = self.buildButton("C", FrequencyType.CONSISTENT, isDark)
        self.layout.addWidget(neverButton)
        self.layout.addWidget(occasionalButton)
        self.layout.addWidget(frequentButton)
        self.layout.addWidget(consistentButton)
        self.buttons[FrequencyType.NEVER] = neverButton
        self.buttons[FrequencyType.OCCASIONAL] = occasionalButton
        self.buttons[FrequencyType.FREQUENT] = frequentButton
        self.buttons[FrequencyType.CONSISTENT] = consistentButton

    def buildPawPositionButtonGroup(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        internalButton = self.buildButton("I", PositionType.INTERNALROTATION)
        externalButton = self.buildButton("E", PositionType.EXTERNALROTATION)
        parallelButton = self.buildButton("P", PositionType.PARALLEL)
        self.layout.addWidget(internalButton)
        self.layout.addWidget(externalButton)
        self.layout.addWidget(parallelButton)
        self.buttons[PositionType.INTERNALROTATION] = internalButton
        self.buttons[PositionType.EXTERNALROTATION] = externalButton
        self.buttons[PositionType.PARALLEL] = parallelButton

    def buildUpDownButtonGroup(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        upButton = self.buildButton("Up", PositionType.UP)
        downButton = self.buildButton("Down", PositionType.DOWN)
        self.layout.addWidget(upButton)
        self.layout.addWidget(downButton)
        self.buttons[PositionType.UP] = upButton
        self.buttons[PositionType.DOWN] = downButton

    def buildButton(self, label, value, isDark=False):
        button = Button(label, isDark)
        button.setFixedSize(self.BUTTON_SIZE)
        button.clicked.connect(lambda: self.setValue(value))
        return button

    def setValue(self, selection):
        self.value = selection
        self.highlightSelectedButton(selection)

    def highlightSelectedButton(self, selection):
        self.removeButtonHighlights()
        self.buttons[selection].setSelectedStyle()

    def removeButtonHighlights(self):
        for button in self.buttons.values():
            button.setUnselectedStyle()

    def getValue(self):
        return self.value
