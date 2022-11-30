from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QDateEdit


class MetaDataSection(QWidget):
    def __init__(self):
        super().__init__()
        self.ratNumberInput = None
        self.weekInput = None
        self.dateInput = None
        self.testerInput = None
        self.leftScore = None
        self.rightScore = None
        self.layout = None
        self.INPUT_SIZE_SMALL = 40

        self.initializeLayout()
        self.buildInputs()
        self.buildLayout()
        self.setDate()

    def initializeLayout(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(20)

    def buildInputs(self):
        self.ratNumberInput = QLineEdit()
        self.weekInput = QLineEdit()
        self.weekInput.setValidator(QIntValidator())
        self.weekInput.setMaximumWidth(self.INPUT_SIZE_SMALL)
        self.dateInput = QDateEdit()
        self.testerInput = QLineEdit()
        self.leftScore = QLineEdit()
        self.leftScore.setValidator(QIntValidator())
        self.leftScore.setMaximumWidth(self.INPUT_SIZE_SMALL)
        self.rightScore = QLineEdit()
        self.rightScore.setValidator(QIntValidator())
        self.rightScore.setMaximumWidth(self.INPUT_SIZE_SMALL)

    def buildLayout(self):
        self.layout.addWidget(QLabel("Rat #:"))
        self.layout.addWidget(self.ratNumberInput)
        self.layout.addWidget(QLabel("Week:"))
        self.layout.addWidget(self.weekInput)
        self.layout.addWidget(QLabel("Date:"))
        self.layout.addWidget(self.dateInput)
        self.layout.addWidget(QLabel("Tester:"))
        self.layout.addWidget(self.testerInput)
        self.layout.addWidget(QLabel("Score:"))
        self.layout.addWidget(QLabel("Left"))
        self.layout.addWidget(self.leftScore)
        self.layout.addWidget(QLabel("Right"))
        self.layout.addWidget(self.rightScore)

    def setDate(self):
        dateTime = QDateTime()
        self.dateInput.setDateTime(dateTime.currentDateTime())

    def setLeftScore(self, score):
        self.leftScore.setText(str(score))

    def setRightScore(self, score):
        self.rightScore.setText(str(score))

    def getRatNumber(self):
        return self.ratNumberInput.text()

    def getWeek(self):
        return self.weekInput.text()

    def getDate(self):
        return self.dateInput.date().toString(Qt.DateFormat.ISODate)

    def getTester(self):
        return self.testerInput.text()

    def getLeftScore(self):
        return self.leftScore.text()

    def getRightScore(self):
        return self.rightScore.text()

    def isComplete(self):
        if self.ratNumberInput.text() == "":
            return False
        if self.weekInput.text() == "":
            return False
        return True

    def resetSection(self):
        self.ratNumberInput.setText("")
        self.leftScore.setText("")
        self.rightScore.setText("")
