from unittest import TestCase
from grader import Grader
from animalside import AnimalSide
from datatypes import *


class BBBTester(TestCase):

    def setUp(self):
        self.grader = Grader()
        self.side = AnimalSide()

    def allJointsExtensive(self, side):
        side.hip = MovementType.EXTENSIVE
        side.knee = MovementType.EXTENSIVE
        side.ankle = MovementType.EXTENSIVE

    def assertGrade(self, side, grade):
        result = self.grader.grade(side)
        self.assertEqual(grade, result)

    def test_nullCase(self):
        side = AnimalSide()
        self.assertGrade(side, 0)

    def test_case0(self):
        side = AnimalSide()
        side.hip = MovementType.NONE
        side.knee = MovementType.NONE
        side.ankle = MovementType.NONE

        self.assertGrade(side, 0)

    def test_case1(self):
        # week7 rat: 519 grader:han
        side = AnimalSide()
        side.hip = MovementType.SLIGHT
        side.knee = MovementType.SLIGHT
        side.ankle = MovementType.NONE
        side.trunkSide = SideType.LEFT
        side.trunkProp = SideType.RIGHT
        side.abdomen = AbdomenType.PARALLEL
        side.sweep = SideType.LEFT
        side.steppingDorsal = FrequencyType.CONSISTENT

        self.assertGrade(side, 1)

    def test_case2(self):
        side = AnimalSide()
        side.hip = MovementType.EXTENSIVE
        side.knee = MovementType.NONE
        side.ankle = MovementType.NONE

        self.assertGrade(side, 2)
        side.knee = MovementType.SLIGHT
        self.assertGrade(side, 2)

    def test_case3(self):
        side = AnimalSide()
        side.hip = MovementType.EXTENSIVE
        side.knee = MovementType.EXTENSIVE
        side.ankle = MovementType.NONE

        self.assertGrade(side, 3)

    def test_case4(self):
        side = AnimalSide()
        side.hip = MovementType.SLIGHT
        side.knee = MovementType.SLIGHT
        side.ankle = MovementType.SLIGHT

        self.assertGrade(side, 4)

    def test_case5(self):
        # week7 rat: 524 grader:gavin
        side = AnimalSide()
        side.hip = MovementType.EXTENSIVE
        side.knee = MovementType.SLIGHT
        side.ankle = MovementType.SLIGHT
        side.trunkSide = SideType.LEFT
        side.trunkProp = SideType.RIGHT
        side.abdomen = AbdomenType.PARALLEL
        side.support = PlacementType.WITH_OUT_SUPPORT
        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        self.assertGrade(side, 5)

    def test_case6(self):
        side = AnimalSide()
        self.allJointsExtensive(side)
        side.ankle = MovementType.SLIGHT

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = SideType.BOTH
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = NullType.NULL
        side.steppingPlantar = FrequencyType.CONSISTENT

        self.assertGrade(side, 6)

        side.abdomen = AbdomenType.DRAG
        side.steppingDorsal = FrequencyType.OCCASIONAL
        side.steppingPlantar = FrequencyType.FREQUENT
        self.assertGrade(side, 6)

    def test_case7(self):
        side = AnimalSide()
        self.allJointsExtensive(side)
        self.assertGrade(side, 7)

    def test_case8(self):
        side = AnimalSide()
        self.allJointsExtensive(side)
        side.support = PlacementType.WITH_OUT_SUPPORT
        side.trunkSide = SideType.MIDDLE
        side.abdomen = AbdomenType.PARALLEL
        side.sweep = PlacementType.SWEEP

        self.assertGrade(side, 8)

        side.sweep = NullType.NULL
        side.steppingPlantar = FrequencyType.OCCASIONAL
        self.assertGrade(side, 8)

    def test_case9(self):
        side = AnimalSide()
        self.allJointsExtensive(side)
        side.trunkSide = SideType.MIDDLE
        side.trunkProp = SideType.LEFT
        side.abdomen = AbdomenType.PARALLEL
        side.support = PlacementType.WITH_SUPPORT
        side.steppingPlantar = FrequencyType.OCCASIONAL

        self.assertGrade(side, 9)

    def test_case10(self):
        side = AnimalSide()
        self.allJointsExtensive(side)
        side.trunkSide = SideType.MIDDLE
        side.abdomen = AbdomenType.PARALLEL
        side.support = PlacementType.WITH_SUPPORT
        side.steppingPlantar = FrequencyType.OCCASIONAL
        side.coordination = FrequencyType.NEVER

        self.assertGrade(side, 10)

    def test_case11(self):
        side = AnimalSide()
        self.allJointsExtensive(side)
        side.trunkSide = SideType.MIDDLE
        side.abdomen = AbdomenType.PARALLEL
        side.support = PlacementType.WITH_SUPPORT
        side.steppingPlantar = FrequencyType.FREQUENT
        side.coordination = FrequencyType.NEVER

        self.assertGrade(side, 11)

        side.steppingPlantar = FrequencyType.CONSISTENT
        self.assertGrade(side, 11)

    def test_case12(self):
        side = AnimalSide()
        side = AnimalSide()
        self.allJointsExtensive(side)
        side.trunkSide = SideType.MIDDLE
        side.abdomen = AbdomenType.PARALLEL
        side.support = PlacementType.WITH_SUPPORT
        side.steppingPlantar = FrequencyType.FREQUENT
        side.coordination = FrequencyType.OCCASIONAL

        self.assertGrade(side, 12)

    def test_case13(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.LEFT
        side.trunkProp = NullType.NULL
        side.abdomen = AbdomenType.HIGH

        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.FREQUENT
        side.toe = FrequencyType.FREQUENT
        side.initialContact = PositionType.EXTERNALROTATION
        side.liftOff = PositionType.EXTERNALROTATION
        side.trunkInstability = StabilityType.UNSTABLE
        side.tail = PositionType.UP

        self.assertGrade(side, 13)

    def test_case14(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.LEFT
        side.trunkProp = NullType.NULL
        side.abdomen = AbdomenType.HIGH

        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.FREQUENT
        side.initialContact = PositionType.EXTERNALROTATION
        side.liftOff = PositionType.EXTERNALROTATION
        side.trunkInstability = StabilityType.UNSTABLE
        side.tail = PositionType.UP

        self.assertGrade(side, 14)

        # side.toe = FrequencyType.CONSISTENT
        # self.assertGrade(side, 14)

    def test_case15(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = SideType.BOTH
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.NEVER
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.PARALLEL
        side.trunkInstability = StabilityType.UNSTABLE
        side.tail = PositionType.UP

        self.assertGrade(side, 15)
        side.toe = FrequencyType.OCCASIONAL
        self.assertGrade(side, 15)

    def test_case16(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = SideType.BOTH
        side.abdomen = AbdomenType.HIGH

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.FREQUENT
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.INTERNALROTATION
        side.trunkInstability = StabilityType.UNSTABLE
        side.tail = PositionType.UP

        result = self.grader.grade(side)
        self.assertEqual(result, 16)

    def test_case17(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.RIGHT
        side.trunkProp = NullType.NULL
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = NullType.NULL
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.FREQUENT
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.PARALLEL
        side.trunkInstability = StabilityType.UNSTABLE
        side.tail = PositionType.UP

        result = self.grader.grade(side)
        self.assertEqual(result, 17)

    def test_case18(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = NullType.NULL
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.CONSISTENT
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.EXTERNALROTATION
        side.trunkInstability = StabilityType.STABLE
        side.tail = PositionType.UP

        self.assertGrade(side, 18)

    def test_case19(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = SideType.BOTH
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = FrequencyType.NEVER
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.CONSISTENT
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.PARALLEL
        side.trunkInstability = StabilityType.STABLE
        side.tail = PositionType.DOWN

        result = self.grader.grade(side)
        self.assertEqual(result, 19)

    def test_case20(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = NullType.NULL
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = NullType.NULL
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.CONSISTENT
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.PARALLEL
        side.trunkInstability = StabilityType.UNSTABLE
        side.tail = PositionType.UP

        self.assertGrade(side, 20)

    def test_case21(self):
        side = AnimalSide()
        self.allJointsExtensive(side)

        side.trunkSide = SideType.MIDDLE
        side.trunkProp = NullType.NULL
        side.abdomen = AbdomenType.PARALLEL

        side.sweep = NullType.NULL
        side.support = PlacementType.WITH_SUPPORT

        side.steppingDorsal = NullType.NULL
        side.steppingPlantar = FrequencyType.CONSISTENT

        side.coordination = FrequencyType.CONSISTENT
        side.toe = FrequencyType.CONSISTENT
        side.initialContact = PositionType.PARALLEL
        side.liftOff = PositionType.PARALLEL
        side.trunkInstability = StabilityType.STABLE
        side.tail = PositionType.UP

        self.assertGrade(side, 21)


if __name__ == '__main__':
    TestCase.main()
