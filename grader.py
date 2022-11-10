from datatypes import *


class Grader:
    def isPawParallelThroughout(self, side):
        return (side.initialContact == PositionType.PARALLEL and
                side.liftOff == PositionType.PARALLEL)

    def testDorsalPlantar(self, side, dorsal, plantar):
        return side.steppingDorsal == dorsal and side.steppingPlantar == plantar

    def isRotated(self, position):
        return position == PositionType.EXTERNALROTATION or position == PositionType.INTERNALROTATION

    def isPlantarSteppingFrequentOrConsistent(self, side):
        return side.steppingPlantar == FrequencyType.FREQUENT or side.steppingPlantar == FrequencyType.CONSISTENT

    def isDorsalSteppingAtLeastOccasional(self, side):
        return (side.steppingDorsal == FrequencyType.OCCASIONAL or
                side.steppingDorsal == FrequencyType.FREQUENT or
                side.steppingDorsal == FrequencyType.CONSISTENT)

    def isPlantSteppingAtLeastOccasional(self, side):
        return (side.steppingPlantar == FrequencyType.OCCASIONAL or
                side.steppingPlantar == FrequencyType.FREQUENT or
                side.steppingPlantar == FrequencyType.CONSISTENT)

    def numberExtensiveJoints(self, side):
        count = 0
        if side.hip == MovementType.EXTENSIVE:
            count += 1
        if side.knee == MovementType.EXTENSIVE:
            count += 1
        if side.ankle == MovementType.EXTENSIVE:
            count += 1
        return count

    def numberSlightJoints(self, side):
        count = 0
        if side.hip == MovementType.SLIGHT:
            count += 1
        if side.knee == MovementType.SLIGHT:
            count += 1
        if side.ankle == MovementType.SLIGHT:
            count += 1
        return count

    def numberNoneJoints(self, side):
        count = 0
        if side.hip == MovementType.NONE:
            count += 1
        if side.knee == MovementType.NONE:
            count += 1
        if side.ankle == MovementType.NONE:
            count += 1
        return count

    def grade(self, side):
        if self.isCase0(side):
            return 0
        elif self.isCase1(side):
            return 1
        elif self.isCase2(side):
            return 2
        elif self.isCase3(side):
            return 3
        elif self.isCase4(side):
            return 4
        elif self.isCase5(side):
            return 5
        elif self.isCase6(side):
            return 6
        elif self.isCase7(side):
            return 7
        elif self.isCase8(side):
            return 8
        elif self.isCase9(side):
            return 9
        elif self.isCase10(side):
            return 10
        elif self.isCase11(side):
            return 11
        elif self.isCase12(side):
            return 12
        elif self.isCase13(side):
            return 13
        elif self.isCase14(side):
            return 14
        elif self.isCase15(side):
            return 15
        elif self.isCase16(side):
            return 16
        elif self.isCase17(side):
            return 17
        elif self.isCase18(side):
            return 18
        elif self.isCase19(side):
            return 19
        elif self.isCase20(side):
            return 20
        else:
            return 21

    def isCase21(self, side):
        print("testing 21")
        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.toe == FrequencyType.CONSISTENT and
                self.isPawParallelThroughout(side) and
                side.trunkInstability == StabilityType.STABLE and
                side.tail == PositionType.UP)

    def isCase20(self, side):
        print("testing 20")

        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.toe == FrequencyType.CONSISTENT and
                self.isPawParallelThroughout(side) and
                side.trunkInstability == StabilityType.UNSTABLE and
                side.tail == PositionType.UP)

    def isCase19(self, side):
        print("testing 19")

        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.toe == FrequencyType.CONSISTENT and
                self.isPawParallelThroughout(side) and
                side.tail == PositionType.DOWN)

    def isCase18(self, side):
        print("testing 18")

        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.toe == FrequencyType.CONSISTENT and
                side.initialContact == PositionType.PARALLEL and
                self.isRotated(side.liftOff)
                )

    def isCase17(self, side):
        print("testing 17")

        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.toe == FrequencyType.FREQUENT and
                self.isPawParallelThroughout(side))

    def isCase16(self, side):
        print("testing 16")

        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.toe == FrequencyType.FREQUENT and
                side.initialContact == PositionType.PARALLEL and
                self.isRotated(side.liftOff))

    def isCase15(self, side):
        print("testing 15")

        return (side.steppingPlantar == FrequencyType.CONSISTENT and
                side.coordination == FrequencyType.CONSISTENT and
                side.initialContact == PositionType.PARALLEL and
                (side.toe == FrequencyType.NEVER or side.toe == FrequencyType.OCCASIONAL))

    def isCase14(self, side):
        print("testing 14")
        firstCase = (side.steppingPlantar == FrequencyType.CONSISTENT and
                     side.coordination == FrequencyType.CONSISTENT and
                     side.support == PlacementType.WITH_SUPPORT and
                     self.isRotated(side.initialContact) and
                     self.isRotated(side.liftOff)
                     )
        secondCase = (
                self.testDorsalPlantar(side, FrequencyType.OCCASIONAL, FrequencyType.FREQUENT) and
                side.coordination == FrequencyType.CONSISTENT)
        return firstCase or secondCase

    def isCase13(self, side):
        print("testing 13")
        return (self.isPlantarSteppingFrequentOrConsistent(side) and
                side.support == PlacementType.WITH_SUPPORT and
                side.coordination == FrequencyType.FREQUENT
                )

    def isCase12(self, side):
        print("testing 12")

        return (self.isPlantarSteppingFrequentOrConsistent(side) and
                side.support == PlacementType.WITH_SUPPORT and
                side.coordination == FrequencyType.OCCASIONAL
                )

    def isCase11(self, side):
        print("testing 11")

        return (self.isPlantarSteppingFrequentOrConsistent(side) and
                side.support == PlacementType.WITH_SUPPORT and
                side.coordination == FrequencyType.NEVER)

    def isCase10(self, side):
        print("testing 10")

        return (side.steppingPlantar == FrequencyType.OCCASIONAL and
                side.support == PlacementType.WITH_SUPPORT and
                side.coordination == FrequencyType.NEVER)

    def isCase9(self, side):
        print("testing 9")

        return (self.isDorsalSteppingAtLeastOccasional(side) and
                side.support == PlacementType.WITH_SUPPORT and
                side.steppingPlantar == FrequencyType.NEVER)

    def isCase8(self, side):
        print("testing 8")

        return ((side.sweep == PlacementType.SWEEP and
                 side.support == PlacementType.WITH_OUT_SUPPORT) or
                (self.isPlantSteppingAtLeastOccasional(side) and
                 side.support == PlacementType.WITH_OUT_SUPPORT)
                )

    def isCase7(self, side):
        print("testing 7")

        return (side.hip == MovementType.EXTENSIVE and
                side.ankle == MovementType.EXTENSIVE and
                side.knee == MovementType.EXTENSIVE)

    def isCase6(self, side):
        print("testing 6")
        return (self.numberExtensiveJoints(side) == 2 and
                self.numberSlightJoints(side) == 1)

    def isCase5(self, side):
        return (self.numberExtensiveJoints(side) == 1 and
                self.numberSlightJoints(side) == 2)

    def isCase4(self, side):
        return self.numberSlightJoints(side) == 3

    def isCase3(self, side):
        return (self.numberExtensiveJoints(side) == 2 and
                self.numberNoneJoints(side) == 1)

    def isCase2(self, side):
        return ((self.numberExtensiveJoints(side) == 1 and
                 self.numberSlightJoints(side) == 0) or
                (self.numberExtensiveJoints(side) == 1 and
                 self.numberSlightJoints(side) == 1))

    def isCase1(self, side):
        return (1 <= self.numberSlightJoints(side) <= 2 and
                self.numberExtensiveJoints(side) == 0)

    def isCase0(self, side):
        return (self.numberSlightJoints(side) == 0 and
                self.numberExtensiveJoints(side) == 0)
