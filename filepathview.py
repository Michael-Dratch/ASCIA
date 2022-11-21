from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt


class FilePathView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.layout)
        self.filePathLabel = QLabel("no file selected")
        self.layoutComponents(self.layout)
        self.fileSelected = False

    def layoutComponents(self, layout):
        layout.addWidget(QLabel("Data Location:"))
        layout.addWidget(self.filePathLabel)

    def setFilePath(self, text):
        self.fileSelected = True
        self.filePathLabel.setText(text)
