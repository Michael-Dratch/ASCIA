class Gui:
    def __init__(self):
        self.window = None
        self.metaDataSection = None
        self.limbMovementSection = None
        self.trunkPositionSection = None
        self.abdomenSection = None
        self.pawPlacementSection = None
        self.coordinationSection = None
        self.toeSection = None
        self.pawPositionSection = None
        self.steppingSection = None
        self.instabilitySection = None
        self.tailSection = None

    def start(self):
        self.window.show()
