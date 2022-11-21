from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel


class Key(QWidget):
    def __init__(self):
        super().__init__()
        self.buildKey()

    def buildKey(self):
        keyLayout = QGridLayout()
        self.setLayout(keyLayout)
        keyLayout.addWidget(QLabel("Ø - No Movement"), 0, 0, 1, 1)
        keyLayout.addWidget(QLabel("S - Slight Movement"), 1, 0, 1, 1)
        keyLayout.addWidget(QLabel("E - Extensive Movement"), 2, 0, 1, 1)
        keyLayout.addWidget(QLabel("Ø - Never        0%, *Clearance <= 5%"), 0, 1, 1, 1)
        keyLayout.addWidget(QLabel("O - Occasional   <= 50%"), 1, 1, 1, 1)
        keyLayout.addWidget(QLabel("F - Frequent   <= 51 - 94%%"), 2, 1, 1, 1)
        keyLayout.addWidget(QLabel("C - Consistent   95 - 100%"), 3, 1, 1, 1)
        keyLayout.addWidget(QLabel("+ D.Steps > 4/HL   **Toe Drags >4/HL"), 4, 1, 1, 1)
        keyLayout.addWidget(QLabel("I - Internal Rotation"), 0, 2, 1, 1)
        keyLayout.addWidget(QLabel("E - External Rotation"), 1, 2, 1, 1)
        keyLayout.addWidget(QLabel("P - Parallel"), 2, 2, 1, 1)
        keyLayout.setColumnStretch(0, 2)
        keyLayout.setColumnStretch(1, 1)
        keyLayout.setContentsMargins(10, 10, 10, 10)
