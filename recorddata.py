class RecordData:
    def __init__(self):
        self.ratNumber = None
        self.week = None
        self.date = None
        self.tester = None
        self.scoreLeft = None
        self.scoreRight = None

        self.leftHip = None
        self.leftKnee = None
        self.leftAnkle = None
        self.rightHip = None
        self.rightKnee = None
        self.rightAnkle = None
        self.trunkSide = None
        self.trunkProp = None
        self.abdomen = None

        self.pawSweep = None
        self.pawWithoutSupp = None
        self.pawWithSupp = None
        self.steppingDorsalLeft = None
        self.steppingPlantarLeft = None
        self.steppingDorsalRight = None
        self.steppingPlantarRight = None

        self.coordination = None
        self.leftToe = None
        self.rightToe = None
        self.initialContactLeft = None
        self.initialContactRight = None
        self.liftOffLeft = None
        self.liftOffRight = None
        self.trunkInstability = None
        self.tail = None

    def toString(self):
        metaData = self.createMetaDataString()
        early = self.createEarlyPhaseString()
        intermediate = self.createIntermediatePhaseString()
        late = self.createLatePhaseString()
        result = metaData + early + intermediate + late

        return result

    def createMetaDataString(self):
        return """
                Rate#: {}
                Week: {}
                Date: {}
                Tester: {}
                Left Score: {}
                Right Score: {}
                """.format(self.ratNumber,
                           self.week,
                           self.date,
                           self.tester,
                           self.scoreLeft,
                           self.scoreRight)

    def createEarlyPhaseString(self):
        return """
                EARLY PHASE SECTION
                Limb Movement
                left hip: {}
                right hip: {}
                left Knee: {}
                right knee: {}
                left Ankle: {}
                right Ankle: {}
                
                Trunk Position
                Trunk Side: {}
                Trunk Prop: {}
                
                Abdomen
                Abdomen: {}
                """.format(self.leftHip.name,
                           self.rightHip.name,
                           self.leftKnee.name,
                           self.rightKnee.name,
                           self.leftAnkle.name,
                           self.rightAnkle.name,
                           self.trunkSide.name,
                           self.trunkProp.name,
                           self.abdomen.name)

    def createIntermediatePhaseString(self):
        return """
                INTERMEDIATE PHASE SECTION
                Paw Placement
                Sweep: {}
                Without Support: {}
                With Support: {}
                
                Stepping
                Left Dorsal: {}
                Right Dorsal: {}
                Left Plantar: {}
                Right Plantar: {}
                """.format(self.pawSweep.name,
                           self.pawWithoutSupp.name,
                           self.pawWithSupp.name,
                           self.steppingDorsalLeft.name,
                           self.steppingDorsalRight.name,
                           self.steppingPlantarLeft.name,
                           self.steppingPlantarRight.name)
        return intermediatePhase

    def createLatePhaseString(self):
        return """
                LATE PHASE SECTION
                Coordination: {}
                Left Toe: {}
                Right Toe: {}
                
                Predominant Paw Position
                Initial Contact
                left: {}
                right: {}
                
                Lift Off
                left: {}
                right: {}
                
                Trunk Instability: {}
                
                Tail: {}
                """.format(self.coordination.name,
                           self.leftToe.name,
                           self.rightToe.name,
                           self.initialContactLeft.name,
                           self.initialContactRight.name,
                           self.liftOffLeft.name,
                           self.liftOffRight.name,
                           self.trunkInstability.name,
                           self.tail.name)
