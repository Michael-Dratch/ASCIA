from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from record import Record
from guicomponents.buttons import Button
from guicomponents.buttongroup import ButtonGroup
from recordbuilder import RecordBuilder
from datatypes import SectionTypes
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

    def __init__(self, saveDataFunction):
        self.window = None
        self.errorWindow = None
        self.earlySectionActive = True
        self.intermediateSectionActive = True
        self.lateSectionActive = True
        self.saveData = saveDataFunction
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
        self.errorWindow = QWidget()
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
        self.earlyPhaseButton = self.buildSectionToggleButton(SectionTypes.EARLY)
        self.intermediatePhaseButton = self.buildSectionToggleButton(SectionTypes.INTERMEDIATE)
        self.latePhaseButton = self.buildSectionToggleButton(SectionTypes.LATE)

    def initializeLayout(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.centerLayout = QHBoxLayout()
        self.earlyPhaseSection = QGridLayout()
        self.intermediatePhaseSection = QGridLayout()
        self.latePhaseSection = QGridLayout()

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

    def buildSectionToggleButton(self, sectionType):
        button = Button("Section N/A")
        button.setMinimumWidth(100)
        button.clicked.connect(lambda: self.sectionToggleClicked(button, sectionType))
        return button

    def layoutSections(self):
        self.layoutEarlySection()
        self.layoutIntermediateSection()
        self.layoutLateSection()
        self.centerLayout.addLayout(self.earlyPhaseSection)
        self.centerLayout.addWidget(self.buildSectionDivider())
        self.centerLayout.addLayout(self.intermediatePhaseSection)
        self.centerLayout.addWidget(self.buildSectionDivider())
        self.centerLayout.addLayout(self.latePhaseSection)

    def layoutEarlySection(self):
        self.earlyPhaseSection.addWidget(self.limbMovementSection, 0, 0)
        self.earlyPhaseSection.addWidget(self.trunkPositionSection, 0, 1)
        self.earlyPhaseSection.addWidget(self.abdomenSection, 0, 2)
        self.earlyPhaseSection.addWidget(self.earlyPhaseButton, 1, 0, 1, 3)

    def layoutIntermediateSection(self):
        self.intermediatePhaseSection.addWidget(self.pawPlacementSection, 0, 0)
        self.intermediatePhaseSection.addWidget(self.steppingSection, 0, 1)
        self.intermediatePhaseSection.addWidget(self.intermediatePhaseButton, 1, 0, 1, 2)

    def layoutLateSection(self):
        self.latePhaseSection.addWidget(self.coordinationSection, 0, 0)
        self.latePhaseSection.addWidget(self.toeSection, 0, 1)
        self.latePhaseSection.addWidget(self.pawPositionSection, 0, 2)
        self.latePhaseSection.addWidget(self.instabilitySection, 0, 3)
        self.latePhaseSection.addWidget(self.tailSection, 0, 4)
        self.latePhaseSection.addWidget(self.latePhaseButton, 1, 0, 1, 5)

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

    def sectionToggleClicked(self, button, sectionType):
        if button.selected == False:
            button.selected = True
            button.setSecondaryStyle()
            self.deactivateSection(sectionType)

        else:
            button.selected = False
            button.setUnselectedStyle()
            self.activateSection(sectionType)

    def deactivateSection(self, sectionType):
        if sectionType == SectionTypes.EARLY:
            self.earlySectionActive = False
        elif sectionType == SectionTypes.INTERMEDIATE:
            self.intermediateSectionActive = False
        else:
            self.lateSectionActive = False

    def activateSection(self, sectionType):
        if sectionType == SectionTypes.EARLY:
            self.earlySectionActive = True
        elif sectionType == SectionTypes.INTERMEDIATE:
            self.intermediateSectionActive = True
        else:
            self.lateSectionActive = True

    def submitClicked(self):
        if self.validateInput():
            record = self.buildRecordDataObject()
            self.saveData(record)

    def validateInput(self):
        if not self.metaDataSection.isComplete():
            self.showErrorWindow("Must complete rat number, week, and date section of form")
            return False
        if self.earlySectionActive:
            if not self.isEarlySectionComplete():
                self.showErrorWindow("Must complete early recovery section")
                return False
        if self.intermediateSectionActive:
            if not self.isIntermediateSectionComplete():
                self.showErrorWindow("Must complete intermediate recovery section")
                return False
        if self.lateSectionActive:
            if not self.isLateSectionComplete():
                self.showErrorWindow("Must complete late recovery section")
                return False
        return True

    def isEarlySectionComplete(self):
        if not self.limbMovementSection.isComplete():
            return False
        if not self.trunkPositionSection.isComplete():
            return False
        if not self.abdomenSection.isComplete():
            return False
        return True

    def isIntermediateSectionComplete(self):
        if not self.pawPlacementSection.isComplete():
            return False
        if not self.steppingSection.isComplete():
            return False
        return True

    def isLateSectionComplete(self):
        if not self.coordinationSection.isComplete():
            return False
        if not self.toeSection.isComplete():
            return False
        if not self.pawPositionSection.isComplete():
            return False
        if not self.instabilitySection.isComplete():
            return False
        if not self.tailSection.isComplete():
            return False
        return True

    def buildRecordDataObject(self):
        recordBuilder = RecordBuilder(self)
        record = recordBuilder.buildRecordDataObject()
        return record

    def showErrorWindow(self, text):
        self.errorWindow = QWidget()
        self.errorWindow.setGeometry(self.window.pos().x() + 300, self.window.pos().y() + 200, 300, 100)
        layout = QVBoxLayout()
        self.errorWindow.setLayout(layout)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.errorWindow.show()


if __name__ == "__main__":
    gui = GUI()
    gui.start()
