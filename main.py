from gui import GUI
from excelwriter import ExcelWriter


class App:
    def __init__(self):
        self.writer = ExcelWriter()
        self.gui = GUI(self.writer.saveRecord)

    def start(self):
        self.gui.start()


if __name__ == "__main__":
    app = App()
    app.start()
