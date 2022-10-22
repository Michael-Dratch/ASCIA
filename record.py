from datatypes import NullType


class Record:
    def __init__(self):
        self.ratNumber = NullType.NULL
        self.week = NullType.NULL
        self.date = NullType.NULL
        self.tester = NullType.NULL
        self.scoreLeft = NullType.NULL
        self.scoreRight = NullType.NULL

        self.leftHip = NullType.NULL
        self.leftKnee = NullType.NULL
        self.leftAnkle = NullType.NULL
        self.rightHip = NullType.NULL
        self.rightKnee = NullType.NULL
        self.rightAnkle = NullType.NULL
        self.trunkSide = NullType.NULL
        self.trunkProp = NullType.NULL
        self.abdomen = NullType.NULL

        self.pawSweep = NullType.NULL
        self.pawWithoutSupp = NullType.NULL
        self.pawWithSupp = NullType.NULL
        self.steppingDorsalLeft = NullType.NULL
        self.steppingPlantarLeft = NullType.NULL
        self.steppingDorsalRight = NullType.NULL
        self.steppingPlantarRight = NullType.NULL

        self.coordination = NullType.NULL
        self.leftToe = NullType.NULL
        self.rightToe = NullType.NULL
        self.initialContactLeft = NullType.NULL
        self.initialContactRight = NullType.NULL
        self.liftOffLeft = NullType.NULL
        self.liftOffRight = NullType.NULL
        self.trunkInstability = NullType.NULL
        self.tail = NullType.NULL

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
