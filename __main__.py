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
        self.writer = ExcelWriter(self.showErrorMessage)
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
        if leftScore == 'Error' or rightScore == 'Error':
            self.showErrorMessage('Was not able to calculate score from parameters entered. Check inputs and resubmit.')
            return
        else:
            self.guiController.setLeftScore(leftScore)
            self.guiController.setRightScore(rightScore)

    def saveRecord(self, record):
        self.writer.saveRecord(record)

    def setFilePath(self, filePath):
        self.writer.setFilePath(filePath)

    def showErrorMessage(self, text):
        self.guiController.showErrorWindow(text)


if __name__ == "__main__":
    app = App()
    app.start()
