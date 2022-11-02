from unittest import TestCase
from grader import Grader
from record import Record
from datatypes import *


class BBBTester(TestCase):

    def setUp(self):
        self.grader = Grader()
        self.record = Record()

    def setRecordAllNone(self, record):
        record.leftHip = MovementType.NONE
        record.rightHip = MovementType.NONE
        record.leftKnee = MovementType.NONE
        record.rightKnee = MovementType.NONE
        record.leftAnkle = MovementType.NONE
        record.rightAnkle = MovementType.NONE

    def setRecordLatePhaseFullyRecovered(self, record):
        record.coordination = FrequencyType.CONSISTENT
        record.leftToe = FrequencyType.CONSISTENT
        record.rightToe = FrequencyType.CONSISTENT
        record.initialContactLeft = PositionType.PARALLEL
        record.initialContactRight = PositionType.PARALLEL
        record.liftOffLeft = PositionType.PARALLEL
        record.liftOffRight = PositionType.PARALLEL
        record.trunkInstability = StabilityType.STABLE
        record.tail = PositionType.UP

    def setToCase19(self):
        self.setRecordLatePhaseFullyRecovered(self.record)
        self.record.trunkInstability = StabilityType.UNSTABLE
        self.record.tail = PositionType.DOWN

    def assertBothSides(self, expected):
        self.assertLeftSide(expected)
        self.assertRightSide(expected)

    def assertLeftSide(self, expected):
        leftSide = self.record.getLeftSide()
        result = self.grader.grade(leftSide)
        self.assertEqual(expected, result)

    def assertRightSide(self, expected):
        rightSide = self.record.getRightSide()
        result = self.grader.grade(rightSide)
        self.assertEqual(expected, result)

    def test_allNulls_0(self):
        self.assertBothSides(0)

    def test_case21(self):
        self.setRecordLatePhaseFullyRecovered(self.record)
        self.assertBothSides(21)

    def test_case20(self):
        self.setRecordLatePhaseFullyRecovered(self.record)
        self.record.trunkInstability = StabilityType.UNSTABLE
        self.assertBothSides(20)

    def test_case19(self):
        self.setToCase19()
        self.assertBothSides(19)

    def test_liftOffExternalRotatedLeft_18(self):
        self.setToCase19()
        self.record.liftOffLeft = PositionType.EXTERNALROTATION
        self.assertLeftSide(18)
        self.assertRightSide(19)

    def test_liftOffExternalRotatedRight_18(self):
        self.setToCase19()
        self.record.liftOffRight = PositionType.EXTERNALROTATION
        self.assertLeftSide(19)
        self.assertRightSide(18)

    def test_liftOffInternalRotatedLeft_18(self):
        self.setToCase19()
        self.record.liftOffLeft = PositionType.INTERNALROTATION
        self.assertLeftSide(18)
        self.assertRightSide(19)

    def test_liftOffInternalRotatedRight_18(self):
        self.setToCase19()
        self.record.liftOffRight = PositionType.INTERNALROTATION
        self.assertLeftSide(19)
        self.assertRightSide(18)

    def test_frequentToeClearanceLeft(self):
        self.setToCase19()
        self.record.leftToe = FrequencyType.FREQUENT
        self.assertLeftSide(17)

    def test_frequentToeClearanceRight(self):
        self.setToCase19()
        self.record.rightToe = FrequencyType.FREQUENT
        self.assertRightSide(17)

    def test_left_case16(self):
        self.record.leftToe = FrequencyType.FREQUENT
        self.record.liftOffLeft = PositionType.EXTERNALROTATION
        self.assertLeftSide(16)

    def test_right_case16(self):
        self.record.coordination = FrequencyType.CONSISTENT
        self.record.rightToe = FrequencyType.FREQUENT
        self.record.liftOffRight = PositionType.EXTERNALROTATION
        self.assertRightSide(16)

    def test_NoToeClearanceLeft_case15(self):
        self.record.coordination = FrequencyType.CONSISTENT
        self.record.leftToe = FrequencyType.NEVER
        self.record.initialContactLeft = PositionType.PARALLEL
        self.assertLeftSide(15)

    def test_OccasionalToeClearanceLeft_Case15(self):
        self.record.coordination = FrequencyType.CONSISTENT
        self.record.leftToe = FrequencyType.OCCASIONAL
        self.record.initialContactLeft = PositionType.PARALLEL
        self.assertLeftSide(15)

    def test_frequentPlantarStepsAndOccasionalDorsalSteps_Case14(self):
        self.record.steppingDorsalLeft = FrequencyType.OCCASIONAL
        self.record.steppingPlantarLeft = FrequencyType.FREQUENT
        self.record.coordination = FrequencyType.CONSISTENT

    def test_consistentPlantarStepsAndExtRotatedPaw_Case14(self):
        self.record.steppingPlantarRight = FrequencyType.CONSISTENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.initialContactRight = PositionType.EXTERNALROTATION
        self.record.liftOffRight = PositionType.EXTERNALROTATION
        self.assertRightSide(14)

    def test_consistentPlantarStepsAndInternalRotatedPaw_Case14(self):
        self.record.steppingPlantarRight = FrequencyType.CONSISTENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.initialContactRight = PositionType.INTERNALROTATION
        self.record.liftOffRight = PositionType.INTERNALROTATION
        self.assertRightSide(14)

    def test_FrequentWithSupportPlantarStepsAndFrequentCoordination_Case13(self):
        self.record.steppingPlantarRight = FrequencyType.FREQUENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.FREQUENT
        self.assertRightSide(13)

    def test_ConsistentWithSupportPlantarStepsAndFrequentCoordination_Case13(self):
        self.record.steppingPlantarRight = FrequencyType.CONSISTENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.FREQUENT
        self.assertRightSide(13)

    def test_FrequentWithSupportPlantarStepsAndOccasionalCoordination_Case12(self):
        self.record.steppingPlantarRight = FrequencyType.FREQUENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.OCCASIONAL
        self.assertRightSide(12)

    def test_ConsistentWithSupportPlantarStepsAndOccasionalCoordination_Case12(self):
        self.record.steppingPlantarRight = FrequencyType.CONSISTENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.OCCASIONAL
        self.assertRightSide(12)

    def test_FrequentWithSupportPlantarStepsAndNoCoordination_Case11(self):
        self.record.steppingPlantarRight = FrequencyType.FREQUENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.NEVER
        self.assertRightSide(11)

    def test_ConsistentWithSupportPlantarStepsAndNoCoordination_Case11(self):
        self.record.steppingPlantarRight = FrequencyType.CONSISTENT
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.NEVER
        self.assertRightSide(11)

    def test_OccasionalWithSupportPlantarStepsAndNoCoordination_Case10(self):
        self.record.steppingPlantarRight = FrequencyType.OCCASIONAL
        self.record.rightPawPlacement = PlacementType.WITH_SUPPORT
        self.record.coordination = FrequencyType.NEVER
        self.assertRightSide(10)

    def test_OccasionalWithSupportDorsalStepping_Case9(self):
        self.record.steppingDorsalLeft = FrequencyType.OCCASIONAL
        self.record.leftPawPlacement = PlacementType.WITH_SUPPORT
        self.record.steppingPlantarLeft = FrequencyType.NEVER
        self.assertLeftSide(9)

    def test_FrequentWithSupportDorsalStepping_Case9(self):
        self.record.steppingDorsalLeft = FrequencyType.FREQUENT
        self.record.leftPawPlacement = PlacementType.WITH_SUPPORT
        self.record.steppingPlantarLeft = FrequencyType.NEVER
        self.assertLeftSide(9)

    def test_ConsistentWithSupportDorsalStepping_Case9(self):
        self.record.steppingDorsalLeft = FrequencyType.CONSISTENT
        self.record.leftPawPlacement = PlacementType.WITH_SUPPORT
        self.record.steppingPlantarLeft = FrequencyType.NEVER
        self.assertLeftSide(9)


if __name__ == '__main__':
    TestCase.main()
