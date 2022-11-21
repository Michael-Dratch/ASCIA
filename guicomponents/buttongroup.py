from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from guicomponents.buttons import Button
from datatypes import *


class ButtonGroup(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.value = NullType.NULL
        self.initializeButtonGroup()
        self.BUTTON_SIZE = QSize(35, 35)
        self.BUTTON_SIZE_LARGE = QSize(60, 35)

    def initializeButtonGroup(self):
        self.buttons = {}

    def buildLimbMovementButtonGroup(self, isDark=False):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
        noneButton = self.buildButton("Ø", MovementType.NONE, isDark)
        slightButton = self.buildButton("S", MovementType.SLIGHT, isDark)
        extensiveButton = self.buildButton("E", MovementType.EXTENSIVE, isDark)
        self.layout.addWidget(noneButton)
        self.layout.addWidget(slightButton)
        self.layout.addWidget(extensiveButton)
        self.buttons[MovementType.NONE] = noneButton
        self.buttons[MovementType.SLIGHT] = slightButton
        self.buttons[MovementType.EXTENSIVE] = extensiveButton

    def removeContentMargins(self):
        self.layout.setContentsMargins(0, 0, 0, 0)

    def buildLeftRightButtonGroup(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
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

    def buildLeftRightBothButtonGroup(self):
        self.buildLeftRightButtonGroup()
        bothButton = self.buildButton("Both", SideType.BOTH)
        bothButton.setFixedSize(self.BUTTON_SIZE_LARGE)
        self.layout.addWidget(bothButton, 1, 0, 1, 2)
        self.buttons[SideType.BOTH] = bothButton

    def buildAbdomenButtonGroup(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
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

    def buildSweepButton(self, text, isDark=False):
        self.initializeHBoxLayout()
        sweepButton = self.buildButton(text, PlacementType.SWEEP, isDark)
        self.layout.addWidget(sweepButton)
        self.buttons[PlacementType.SWEEP] = sweepButton

    def buildSupportButtonGroup(self, text, isDark=False):
        self.initializeHBoxLayout()
        woSuppButton = self.buildButton(text, PlacementType.WITH_OUT_SUPPORT, isDark)
        withSuppButton = self.buildButton(text, PlacementType.WITH_SUPPORT, isDark)
        self.layout.addWidget(woSuppButton)
        self.layout.addWidget(withSuppButton)
        self.buttons[PlacementType.WITH_OUT_SUPPORT] = woSuppButton
        self.buttons[PlacementType.WITH_SUPPORT] = withSuppButton

    def buildFrequencyButtonGroup(self, isDark=False):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
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

    def buildPawPositionButtonGroup(self, isDark=False):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
        internalButton = self.buildButton("I", PositionType.INTERNALROTATION, isDark)
        externalButton = self.buildButton("E", PositionType.EXTERNALROTATION, isDark)
        parallelButton = self.buildButton("P", PositionType.PARALLEL, isDark)
        self.layout.addWidget(internalButton)
        self.layout.addWidget(externalButton)
        self.layout.addWidget(parallelButton)
        self.buttons[PositionType.INTERNALROTATION] = internalButton
        self.buttons[PositionType.EXTERNALROTATION] = externalButton
        self.buttons[PositionType.PARALLEL] = parallelButton

    def buildUpDownButtonGroup(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
        upButton = self.buildButton("Up", PositionType.UP)
        self.setButtonSize(upButton, self.BUTTON_SIZE_LARGE)
        downButton = self.buildButton("Down", PositionType.DOWN)
        self.setButtonSize(downButton, self.BUTTON_SIZE_LARGE)
        self.layout.addWidget(upButton)
        self.layout.addWidget(downButton)
        self.buttons[PositionType.UP] = upButton
        self.buttons[PositionType.DOWN] = downButton

    def buildStabilityButtonGroup(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()
        stableButton = self.buildButton("Stable", StabilityType.STABLE)
        self.setButtonSize(stableButton, self.BUTTON_SIZE_LARGE)
        unstableButton = self.buildButton("Unstable", StabilityType.UNSTABLE)
        self.setButtonSize(unstableButton, self.BUTTON_SIZE_LARGE)
        self.layout.addWidget(unstableButton)
        self.layout.addWidget(stableButton)
        self.buttons[StabilityType.UNSTABLE] = unstableButton
        self.buttons[StabilityType.STABLE] = stableButton

    def buildGradeSubmitButtonGroup(self, gradeHandler, submitHandler):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        gradeButton = Button("Grade")
        gradeButton.clicked.connect(gradeHandler)
        gradeButton.setMinimumSize(60, 40)
        submitButton = Button("Submit")
        submitButton.clicked.connect(submitHandler)
        submitButton.setMinimumSize(60, 40)
        self.layout.addWidget(gradeButton)
        self.layout.addWidget(submitButton)

    def initializeHBoxLayout(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.removeContentMargins()

    def buildButton(self, label, value, isDark=False):
        button = Button(label, isDark)
        button.setFixedSize(self.BUTTON_SIZE)
        button.clicked.connect(lambda: self.setValue(value))
        return button

    def setButtonSize(self, button, size):
        button.setMaximumSize(size)
        button.setMinimumSize(size)

    def setValue(self, selection):
        self.removeButtonHighlights()
        if self.value == selection:
            self.value = NullType.NULL
        else:
            self.value = selection
            self.highlightSelectedButton(selection)

    def highlightSelectedButton(self, selection):
        self.buttons[selection].setSelectedStyle()

    def removeButtonHighlights(self):
        for button in self.buttons.values():
            button.setUnselectedStyle()

    def getValue(self):
        return self.value
