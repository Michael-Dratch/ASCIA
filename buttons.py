from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, label, isDark=False):
        super(Button, self).__init__(label)
        if isDark == False:
            self.selected = False
            self.unselectedStyle = """
                                    QPushButton {
                                    background-color: #eee
                                    }
                                    QPushButton:hover {
                                    background-color: #aaa
                                    }
                                    """
        elif isDark == True:
            self.unselectedStyle = """
                                    QPushButton {
                                    background-color: #aaa
                                    }
                                    QPushButton:hover {
                                    background-color: #888
                                    }
                                    """

        self.selectedStyle = """
                                QPushButton {
                                background-color: #22b600
                                }
                                """
        self.secondaryStyle = """
                                  QPushButton {
                                  background-color: #3895D3
                                  }
                                  """
        self.setStyleSheet(self.unselectedStyle)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def setUnselectedStyle(self):
        self.setStyleSheet(self.unselectedStyle)

    def setSelectedStyle(self):
        self.setStyleSheet(self.selectedStyle)

    def setSecondaryStyle(self):
        self.setStyleSheet(self.secondaryStyle)
