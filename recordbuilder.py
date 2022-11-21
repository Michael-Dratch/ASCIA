from record import Record


class RecordBuilder:
    def __init__(self, guiInstance):
        self.gui = guiInstance

    def buildRecordDataObject(self):
        record = Record()
        self.setRecordMetaData(record)
        self.setEarlyPhaseData(record)
        self.setIntermediatePhaseData(record)
        self.setLatePhaseData(record)
        return record

    def setRecordMetaData(self, record):
        record.ratNumber = self.gui.metaDataSection.getRatNumber()
        record.week = self.gui.metaDataSection.getWeek()
        record.date = self.gui.metaDataSection.getDate()
        record.tester = self.gui.metaDataSection.getTester()
        record.scoreLeft = self.gui.metaDataSection.getLeftScore()
        record.scoreRight = self.gui.metaDataSection.getRightScore()

    def setEarlyPhaseData(self, record):
        record.leftHip = self.gui.limbMovementSection.getLeftHip()
        record.rightHip = self.gui.limbMovementSection.getRightHip()
        record.leftKnee = self.gui.limbMovementSection.getLeftKnee()
        record.rightKnee = self.gui.limbMovementSection.getRightKnee()
        record.leftAnkle = self.gui.limbMovementSection.getLeftAnkle()
        record.rightAnkle = self.gui.limbMovementSection.getRightAnkle()
        record.trunkSide = self.gui.trunkPositionSection.getSide()
        record.trunkProp = self.gui.trunkPositionSection.getProp()
        record.abdomen = self.gui.abdomenSection.getAbdomen()

    def setIntermediatePhaseData(self, record):
        record.leftSweep = self.gui.pawPlacementSection.getLeftSweep()
        record.rightSweep = self.gui.pawPlacementSection.getRightSweep()
        record.leftSupport = self.gui.pawPlacementSection.getLeftSupport()
        record.rightSupport = self.gui.pawPlacementSection.getRightSupport()
        record.steppingDorsalLeft = self.gui.steppingSection.getLeftDorsal()
        record.steppingDorsalRight = self.gui.steppingSection.getRightDorsal()
        record.steppingPlantarLeft = self.gui.steppingSection.getLeftPlantar()
        record.steppingPlantarRight = self.gui.steppingSection.getRightPlantar()

    def setLatePhaseData(self, record):
        record.coordination = self.gui.coordinationSection.getCoordination()
        record.leftToe = self.gui.toeSection.getLeftToe()
        record.rightToe = self.gui.toeSection.getRightToe()
        record.initialContactLeft = self.gui.pawPositionSection.getLeftInitialContact()
        record.initialContactRight = self.gui.pawPositionSection.getRightInitialContact()
        record.liftOffLeft = self.gui.pawPositionSection.getLeftLiftOff()
        record.liftOffRight = self.gui.pawPositionSection.getRightLiftOff()
        record.trunkInstability = self.gui.instabilitySection.getTrunkInstability()
        record.tail = self.gui.tailSection.getTail()
