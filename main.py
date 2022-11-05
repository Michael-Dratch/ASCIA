from PyQt6.QtWidgets import QApplication, QFileDialog
from grader import Grader
from excelwriter import ExcelWriter
from guibuilder import GuiBuilder
from guicontroller import GuiController


class App:
    def __init__(self):
        self.writer = None
        self.grader = None
        self.guiBuilder = None
        self.guiController = None
        self.initializeComponents()

    def initializeComponents(self):
        self.writer = ExcelWriter("./BBB_Data.xlsx")
        self.grader = Grader()
        self.guiController = GuiController()
        self.guiController.setGradeHandler(self.gradeRecord)
        self.guiController.setSubmitHandler(self.saveRecord)
        self.guiController.setUpdateFilePathHandler(self.setFilePath)
        self.guiBuilder = GuiBuilder(self.guiController.gradeClicked,
                                     self.guiController.submitClicked,
                                     self.guiController.sectionToggleClicked,
                                     self.guiController.newFileClicked,
                                     self.guiController.loadFileClicked)

    def start(self):
        application = QApplication([])
        gui = self.guiBuilder.build()
        self.guiController.setGui(gui)
        gui.start()
        application.exec()

    def gradeRecord(self, record):
        leftScore = self.grader.grade(record.getLeftSide())
        rightScore = self.grader.grade(record.getRightSide())
        self.guiController.setLeftScore(leftScore)
        self.guiController.setRightScore(rightScore)

    def saveRecord(self, record):
        self.writer.saveRecord(record)

    def setFilePath(self, filePath):
        self.writer.setFilePath(filePath)


if __name__ == "__main__":
    app = App()
    app.start()
