from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import *
from sections.limbmovementsection import LimbMovementSection
from sections.trunkpositionsection import TrunkPositionSection
from sections.abdomensection import AbdomenSection
from sections.pawplacementsection import PawPlacementSection
from sections.steppingSection import SteppingSection
from sections.coordinationsection import CoordinationSection
from sections.toesection import ToeSection
from sections.pawpositionsection import PawPositionSection
from sections.instabilitysection import InstabilitySection
from sections.tailSection import TailSection
from sections.metadatasection import MetaDataSection


class GUI:

    def __init__(self):
        self.window = None
        self.styleSheet = """
        QWidget#section {
            border: 1px solid black
            }
        QPushButton {
            border: 1px solid black
            }
            """

    def start(self):
        app = QApplication([])
        self.window = QWidget()
        self.window.setStyleSheet(self.styleSheet)
        self.window.setGeometry(100, 100, 600, 400)
        self.window.setWindowTitle("BBB Locomotor Rating Scale Grader")
        self.buildMainLayout()

        self.window.show()
        app.exec()

    def buildMainLayout(self):
        self.initializeLayout()
        self.buildSections()
        self.layoutSections()
        metaDataSection = MetaDataSection()
        sectionButtons = self.buildSectionButtonLayout()
        self.buildSubmitButton()
        key = self.buildKey()

        self.mainLayout.addWidget(metaDataSection)
        self.mainLayout.addLayout(self.layout)
        self.mainLayout.addWidget(sectionButtons)
        self.mainLayout.addWidget(key)

        self.window.setLayout(self.mainLayout)

    def buildSectionButtonLayout(self):
        sectionButtons = QWidget()
        sectionButtons.setStyleSheet("""QPushButton:hover{background-color: #999}""")
        layout = QHBoxLayout()
        sectionButtons.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        sectionButtons.setLayout(layout)
        self.earlyPhaseButton = QPushButton("Section N/A")
        self.earlyPhaseButton.setMinimumWidth(100)
        self.intermediatePhaseButton = QPushButton("Section N/A")
        self.intermediatePhaseButton.setMinimumWidth(100)
        self.intermediatePhaseButton.setMaximumWidth(100)
        self.latePhaseButton = QPushButton("Section N/A")
        self.latePhaseButton.setMinimumWidth(100)

        layout.addWidget(self.earlyPhaseButton)
        layout.setAlignment(self.earlyPhaseButton, Qt.AlignmentFlag.AlignLeft)
        layout.addSpacerItem(QSpacerItem(45, 20))
        layout.addWidget(self.intermediatePhaseButton)

        layout.addWidget(self.latePhaseButton)
        layout.setAlignment(self.latePhaseButton, Qt.AlignmentFlag.AlignRight)
        layout.addSpacerItem(QSpacerItem(200, 20))

        return sectionButtons

    def initializeLayout(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.layout = QHBoxLayout()

    def buildSections(self):
        self.limbMovementSection = self.buildSection(LimbMovementSection(), 200, 250)
        self.trunkPositionSection = self.buildSection(TrunkPositionSection(), 200, 250)
        self.abdomenSection = self.buildSection(AbdomenSection(), 100, 250)
        self.pawPlacementSection = self.buildSection(PawPlacementSection(), 200, 250)
        self.coordinationSection = self.buildSection(CoordinationSection(), 100, 250)
        self.toeSection = self.buildSection(ToeSection(), 100, 250)
        self.pawPositionSection = self.buildSection(PawPositionSection(), 200, 250)
        self.steppingSection = self.buildSection(SteppingSection(), 200, 250)
        self.instabilitySection = self.buildSection(InstabilitySection(), 100, 250)
        self.tailSection = self.buildSection(TailSection(), 100, 250)

    def layoutSections(self):
        self.layout.addWidget(self.limbMovementSection)
        self.layout.addWidget(self.trunkPositionSection)
        self.layout.addWidget(self.abdomenSection)
        self.layout.addWidget(self.buildSectionDivider())
        self.layout.addWidget(self.pawPlacementSection)
        self.layout.addWidget(self.steppingSection)
        self.layout.addWidget(self.buildSectionDivider())
        self.layout.addWidget(self.coordinationSection)
        self.layout.addWidget(self.toeSection)
        self.layout.addWidget(self.pawPositionSection)
        self.layout.addWidget(self.instabilitySection)
        self.layout.addWidget(self.tailSection)

    def buildSection(self, sectionObject, width, height):
        section = sectionObject
        section.setObjectName('section')
        section.setMaximumSize(width, height)
        return section

    def buildSectionDivider(self):
        divider = QFrame()
        divider.setFrameStyle(QFrame.Shape.VLine | QFrame.Shadow.Plain)
        divider.setMaximumSize(4, 250)
        divider.setMinimumSize(4, 250)
        divider.setLineWidth(20)
        return divider

    def buildKey(self):
        key = QWidget()
        key.setMaximumHeight(100)
        keyLayout = QGridLayout()
        key.setLayout(keyLayout)
        keyLayout.addWidget(QLabel("Ø - No Movement"), 0, 0, 1, 1)
        keyLayout.addWidget(QLabel("S - Slight Movement"), 1, 0, 1, 1)
        keyLayout.addWidget(QLabel("E - Extensive Movement"), 2, 0, 1, 1)
        keyLayout.addWidget(QLabel("Ø - Never        0%, *Clearance <= 5%"), 0, 1, 1, 1)
        keyLayout.addWidget(QLabel("O - Occasional   <= 50%"), 1, 1, 1, 1)
        keyLayout.addWidget(QLabel("F - Frequent   <= 51 - 94%%"), 2, 1, 1, 1)
        keyLayout.addWidget(QLabel("C - Consistent   95 - 100%"), 3, 1, 1, 1)
        keyLayout.addWidget(QLabel("+ D.Steps > 4/HL   **Toe Drags >4/HL"), 4, 1, 1, 1)
        keyLayout.addWidget(QLabel("I - Internal Rotation"), 0, 2, 1, 1)
        keyLayout.addWidget(QLabel("E - External Rotation"), 1, 2, 1, 1)
        keyLayout.addWidget(QLabel("P - Parallel"), 2, 2, 1, 1)
        keyLayout.setColumnStretch(0, 2)
        keyLayout.setColumnStretch(1, 1)
        keyLayout.setContentsMargins(10, 10, 10, 10)

        keyLayout.addWidget(self.submitButton, 0, 3, 2, 1)
        return key

    def buildSubmitButton(self):
        self.submitButton = QPushButton("Submit")
        self.submitButton.setMinimumSize(60, 40)
        self.submitButton.setStyleSheet("""
                                        QPushButton:hover{
                                        background-color: #999
                                        }
                                        """)


if __name__ == "__main__":
    gui = GUI()
    gui.start()
