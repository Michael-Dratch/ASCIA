from gui import GUI
from grader import Grader
from excelwriter import ExcelWriter


class App:
    def __init__(self):
        self.writer = ExcelWriter()
        self.grader = Grader()
        self.gui = GUI()
        self.gui.setGradeMethod(self.gradeRecord)
        self.gui.setSaveMethod(self.saveRecord)
        self.gui.setNewFilePathMethod(self.newFilePath)

    def start(self):
        self.gui.start()

    def gradeClicked(self, record):
        leftScore = Grader.grade(record.getLeftSide())
        rightScore = Grader.grade(record.getRightSide())

    def saveRecord(self, record):
        self.writer.saveRecord(record)

    def newFilePath(self, filePath):
        self.writer.setFilePath(filePath)


if __name__ == "__main__":
    app = App()
    app.start()
