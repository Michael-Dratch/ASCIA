from PyQt6.QtWidgets import *
from recorddata import RecordData
from buttons import Button
from buttongroup import ButtonGroup
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
from sections.key import Key


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
        self.initializeComponents()
        self.layoutSections()
        self.layoutFooter()
        self.mainLayout.addWidget(self.metaDataSection)
        self.mainLayout.addLayout(self.centerLayout)
        self.mainLayout.addLayout(self.footer)
        self.window.setLayout(self.mainLayout)

    def initializeComponents(self):
        self.initializeLayout()
        self.initializeSectionToggleButtons()
        self.buildSections()
        self.metaDataSection = MetaDataSection()
        self.initializeFooter()

    def initializeFooter(self):
        self.key = Key()
        self.gradeSubmitButtons = ButtonGroup()
        self.gradeSubmitButtons.buildGradeSubmitButtonGroup(None, self.submitClicked)

    def initializeSectionToggleButtons(self):
        self.earlyPhaseButton = self.buildSectionToggleButton()
        self.intermediatePhaseButton = self.buildSectionToggleButton()
        self.latePhaseButton = self.buildSectionToggleButton()

    def initializeLayout(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.centerLayout = QHBoxLayout()
        self.earlyPhaseContainer = QGridLayout()
        self.intermediatePhaseContainer = QGridLayout()
        self.latePhaseContainer = QGridLayout()

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

    def buildSectionToggleButton(self):
        button = Button("Section N/A")
        button.setMinimumWidth(100)
        return button

    def layoutSections(self):
        self.layoutEarlySection()
        self.layoutIntermediateSection()
        self.layoutLateSection()
        self.centerLayout.addLayout(self.earlyPhaseContainer)
        self.centerLayout.addWidget(self.buildSectionDivider())
        self.centerLayout.addLayout(self.intermediatePhaseContainer)
        self.centerLayout.addWidget(self.buildSectionDivider())
        self.centerLayout.addLayout(self.latePhaseContainer)

    def layoutEarlySection(self):
        self.earlyPhaseContainer.addWidget(self.limbMovementSection, 0, 0)
        self.earlyPhaseContainer.addWidget(self.trunkPositionSection, 0, 1)
        self.earlyPhaseContainer.addWidget(self.abdomenSection, 0, 2)
        self.earlyPhaseContainer.addWidget(self.earlyPhaseButton, 1, 0)

    def layoutIntermediateSection(self):
        self.intermediatePhaseContainer.addWidget(self.pawPlacementSection, 0, 0)
        self.intermediatePhaseContainer.addWidget(self.steppingSection, 0, 1)
        self.intermediatePhaseContainer.addWidget(self.intermediatePhaseButton, 1, 0)

    def layoutLateSection(self):
        self.latePhaseContainer.addWidget(self.coordinationSection, 0, 0)
        self.latePhaseContainer.addWidget(self.toeSection, 0, 1)
        self.latePhaseContainer.addWidget(self.pawPositionSection, 0, 2)
        self.latePhaseContainer.addWidget(self.instabilitySection, 0, 3)
        self.latePhaseContainer.addWidget(self.tailSection, 0, 4)
        self.latePhaseContainer.addWidget(self.latePhaseButton, 1, 0)

    def layoutFooter(self):
        self.footer = QHBoxLayout()
        self.footer.addWidget(self.key)
        self.footer.addWidget(self.gradeSubmitButtons)

    def buildSection(self, sectionObject, width, height):
        sectionObject.setObjectName('section')
        sectionObject.setMaximumSize(width, height)
        return sectionObject

    def buildSectionDivider(self):
        divider = QFrame()
        divider.setFrameStyle(QFrame.Shape.VLine | QFrame.Shadow.Plain)
        divider.setMaximumSize(4, 270)
        divider.setMinimumSize(4, 270)
        divider.setLineWidth(20)
        return divider

    def submitClicked(self):
        self.buildRecordDataObject()

    def buildRecordDataObject(self):
        record = RecordData()
        self.setRecordMetaData(record)
        self.setEarlyPhaseData(record)
        self.setIntermediatePhaseData(record)
        self.setLatePhaseData(record)
        print(record.toString())

    def setRecordMetaData(self, record):
        record.ratNumber = self.metaDataSection.getRatNumber()
        record.week = self.metaDataSection.getWeek()
        record.date = self.metaDataSection.getDate()
        record.tester = self.metaDataSection.getTester()
        record.scoreLeft = self.metaDataSection.getLeftScore()
        record.scoreRight = self.metaDataSection.getRightScore()

    def setEarlyPhaseData(self, record):
        record.leftHip = self.limbMovementSection.getLeftHip()
        record.rightHip = self.limbMovementSection.getRightHip()
        record.leftKnee = self.limbMovementSection.getLeftKnee()
        record.rightKnee = self.limbMovementSection.getRightKnee()
        record.leftAnkle = self.limbMovementSection.getLeftAnkle()
        record.rightAnkle = self.limbMovementSection.getRightAnkle()
        record.trunkSide = self.trunkPositionSection.getSide()
        record.trunkProp = self.trunkPositionSection.getProp()
        record.abdomen = self.abdomenSection.getAbdomen()

    def setIntermediatePhaseData(self, record):
        record.pawSweep = self.pawPlacementSection.getSweep()
        record.pawWithoutSupp = self.pawPlacementSection.getWithOutSupport()
        record.pawWithSupp = self.pawPlacementSection.getWithSupport()
        record.steppingDorsalLeft = self.steppingSection.getLeftDorsal()
        record.steppingDorsalRight = self.steppingSection.getRightDorsal()
        record.steppingPlantarLeft = self.steppingSection.getLeftPlantar()
        record.steppingPlantarRight = self.steppingSection.getRightPlantar()

    def setLatePhaseData(self, record):
        record.coordination = self.coordinationSection.getCoordination()
        record.leftToe = self.toeSection.getLeftToe()
        record.rightToe = self.toeSection.getRightToe()
        record.initialContactLeft = self.pawPositionSection.getLeftInitialContact()
        record.initialContactRight = self.pawPositionSection.getRightInitialContact()
        record.liftOffLeft = self.pawPositionSection.getLeftLiftOff()
        record.liftOffRight = self.pawPositionSection.getRightLiftOff()
        record.trunkInstability = self.instabilitySection.getTrunkInstability()
        record.tail = self.tailSection.getTail()


if __name__ == "__main__":
    gui = GUI()
    gui.start()
