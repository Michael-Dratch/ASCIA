from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
from guicomponents.buttons import Button
from guicomponents.buttongroup import ButtonGroup
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
from filepathview import FilePathView
from gui import Gui


class GuiBuilder:
    def __init__(self,
                 gradeHandler,
                 submitHandler,
                 sectionToggleHandler,
                 newFileHandler,
                 loadFileHandler):
        self.gradeClicked = gradeHandler
        self.submitClicked = submitHandler
        self.newFileClicked = newFileHandler
        self.loadFileClicked = loadFileHandler
        self.sectionToggleClicked = sectionToggleHandler
        self.width = 600
        self.height = 400
        self.selectorSectionHeight = 300
        self.styleSheet = """
                QLabel {
                    font-size: 15px
                    }
                QWidget#section {
                    border: 1px solid black
                    }
                QPushButton {
                    border: 1px solid black
                    }
                    """

    def build(self):
        gui = Gui()
        mainWindow = QMainWindow()
        mainWindow.setWindowTitle("ASCIA")
        mainWindow.setWindowIcon(QIcon("images/rat_small.PNG"))
        window = QWidget()
        mainWindow.setCentralWidget(window)
        window.setStyleSheet(self.styleSheet)
        window.setGeometry(int(600 - self.width / 2), int(400 - self.height / 2),
                           self.width, self.height)
        mainWindow.setMenuWidget(self.buildMenuBar())
        self.buildMainLayout(window)
        gui.mainWindow = mainWindow
        self.addSectionsToGui(gui)
        return gui

    def buildMenuBar(self):
        menuBar = QMenuBar()
        fileMenu = QMenu("File", menuBar)
        menuBar.addMenu(fileMenu)
        self.createFileMenuActions(fileMenu)
        return menuBar

    def createFileMenuActions(self, fileMenu):
        newFileAction = QAction("New File", fileMenu)
        newFileAction.triggered.connect(self.newFileClicked)
        loadFileAction = QAction("Load File", fileMenu)
        loadFileAction.triggered.connect(self.loadFileClicked)
        fileMenu.addActions([newFileAction, loadFileAction])

    def buildMainLayout(self, window):
        self.initializeComponents()
        self.layoutSections()
        self.layoutFooter()
        self.mainLayout.addWidget(self.metaDataSection)
        self.mainLayout.addLayout(self.centerLayout)
        self.mainLayout.addLayout(self.footer)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        window.setLayout(self.mainLayout)

    def initializeComponents(self):
        self.initializeLayout()
        self.initializeSectionToggleButtons()
        self.buildSections()
        self.metaDataSection = MetaDataSection()
        self.initializeFooter()

    def initializeFooter(self):
        self.key = Key()
        self.gradeSubmitButtons = ButtonGroup()
        self.gradeSubmitButtons.buildGradeSubmitButtonGroup(self.gradeClicked, self.submitClicked)
        self.filePathView = FilePathView()

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
        self.limbMovementSection = self.buildSection(LimbMovementSection(), 200, self.selectorSectionHeight)
        self.trunkPositionSection = self.buildSection(TrunkPositionSection(), 200, self.selectorSectionHeight)
        self.abdomenSection = self.buildSection(AbdomenSection(), 100, self.selectorSectionHeight)
        self.pawPlacementSection = self.buildSection(PawPlacementSection(), 200, self.selectorSectionHeight)
        self.coordinationSection = self.buildSection(CoordinationSection(), 100, self.selectorSectionHeight)
        self.toeSection = self.buildSection(ToeSection(), 100, self.selectorSectionHeight)
        self.pawPositionSection = self.buildSection(PawPositionSection(), 200, self.selectorSectionHeight)
        self.steppingSection = self.buildSection(SteppingSection(), 200, self.selectorSectionHeight)
        self.instabilitySection = self.buildSection(InstabilitySection(), 100, self.selectorSectionHeight)
        self.tailSection = self.buildSection(TailSection(), 100, self.selectorSectionHeight)

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
        self.footer = QGridLayout()
        self.footer.addWidget(self.key, 0, 0, 1, 1)
        self.footer.addWidget(self.gradeSubmitButtons, 0, 1, 1, 1)
        self.footer.addWidget(self.filePathView, 1, 0, 1, 1)

    def buildSection(self, sectionObject, width, height):
        sectionObject.setObjectName('section')
        sectionObject.setMinimumHeight(height)
        # sectionObject.setMaximumSize(width, height)
        return sectionObject

    def buildSectionDivider(self):
        divider = QFrame()
        divider.setFrameStyle(QFrame.Shape.VLine | QFrame.Shadow.Plain)
        divider.setMinimumSize(4, self.selectorSectionHeight)
        divider.setLineWidth(20)
        return divider

    def addSectionsToGui(self, gui):
        gui.metaDataSection = self.metaDataSection
        gui.filePathView = self.filePathView
        gui.limbMovementSection = self.limbMovementSection
        gui.trunkPositionSection = self.trunkPositionSection
        gui.abdomenSection = self.abdomenSection
        gui.pawPlacementSection = self.pawPlacementSection
        gui.coordinationSection = self.coordinationSection
        gui.toeSection = self.toeSection
        gui.pawPositionSection = self.pawPositionSection
        gui.steppingSection = self.steppingSection
        gui.instabilitySection = self.instabilitySection
        gui.tailSection = self.tailSection
