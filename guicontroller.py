from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFileDialog
from datatypes import SectionTypes
from recordbuilder import RecordBuilder


class GuiController:

    def __init__(self):
        self.submitHandler = None
        self.gradeHandler = None
        self.updateFilePathHandler = None
        self.filePath = ""
        self.earlySectionActive = True
        self.intermediateSectionActive = True
        self.lateSectionActive = True
        self.errorWindow = None
        self.gui = None

    def setGui(self, gui):
        self.gui = gui

    def setGradeHandler(self, handler):
        self.gradeHandler = handler

    def setSubmitHandler(self, handler):
        self.submitHandler = handler

    def setUpdateFilePathHandler(self, handler):
        self.updateFilePathHandler = handler

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

    def gradeClicked(self):
        if self.validateInput():
            recordBuilder = RecordBuilder(self.gui)
            record = recordBuilder.buildRecordDataObject()
            self.gradeHandler(record)

    def submitClicked(self):
        if self.validateInput():
            recordBuilder = RecordBuilder(self.gui)
            record = recordBuilder.buildRecordDataObject()
            self.submitHandler(record)
            self.resetGUI()

    def validateInput(self):
        # if not self.gui.metaDataSection.isComplete():
        #     self.showErrorWindow("Must complete rat number, week, and date section of form")
        #     return False
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
        # if not self.gui.filePathView.fileSelected:
        #     self.showErrorWindow("Must select or create excel file for saving data in file menu")
        #     return False
        return True

    def isEarlySectionComplete(self):
        if not self.gui.limbMovementSection.isComplete():
            return False
        return True

    def isIntermediateSectionComplete(self):
        if not self.gui.pawPlacementSection.isComplete():
            return False
        if not self.gui.steppingSection.isComplete():
            return False
        return True

    def isLateSectionComplete(self):
        if not self.gui.coordinationSection.isComplete():
            return False
        if not self.gui.toeSection.isComplete():
            return False
        if not self.gui.pawPositionSection.isComplete():
            return False
        if not self.gui.instabilitySection.isComplete():
            return False
        if not self.gui.tailSection.isComplete():
            return False
        return True

    def showErrorWindow(self, text):
        self.errorWindow = QWidget()
        self.errorWindow.setGeometry(self.gui.mainWindow.pos().x() + 300, self.gui.mainWindow.pos().y() + 200, 300, 100)
        layout = QVBoxLayout()
        self.errorWindow.setLayout(layout)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.errorWindow.show()

    def setLeftScore(self, score):
        self.gui.metaDataSection.setLeftScore(score)

    def setRightScore(self, score):
        self.gui.metaDataSection.setRightScore(score)

    def newFileClicked(self):
        result = QFileDialog.getSaveFileName(self.gui.mainWindow, "Create New Excel File", "",
                                             "Excel File (*.xlsx)")
        dirPath = result[0]
        self.gui.filePathView.setFilePath(dirPath)
        self.updateFilePathHandler(dirPath)

    def loadFileClicked(self):
        result = QFileDialog.getOpenFileName(self.gui.mainWindow, "Load Existing Excel File", "",
                                             "Excel File (*.xlsx)")
        dirPath = result[0]
        self.gui.filePathView.setFilePath(dirPath)
        self.updateFilePathHandler(dirPath)

    def resetGUI(self):
        gui = self.gui
        gui.limbMovementSection.resetSelectors()
        gui.abdomenSection.resetSelectors()
        gui.coordinationSection.resetSelectors()
        gui.instabilitySection.resetSelectors()
        gui.pawPlacementSection.resetSelectors()
        gui.pawPositionSection.resetSelectors()
        gui.steppingSection.resetSelectors()
        gui.tailSection.resetSelectors()
        gui.toeSection.resetSelectors()
        gui.trunkPositionSection.resetSelectors()
        gui.metaDataSection.resetSection()
