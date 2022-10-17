class Grader:
    def gradeHindLeg(self, animalData, side):
        hip = self.getHipMobility(animalData ,side)
        knee = self.getKneeMobility(animalData, side)
        ankle = self.getHipMobility(animalData, side)

        if self.checkNoObservableHindLimbMovement(hip, knee, ankle):
            return 0
        elif self.checkSlightMovementofOneOrTwoJoints(hip, knee, ankle):
            return 1
        elif self.checkExtensiveMovementOfOneJoint(hip, knee, ankle):
            return 2



    def checkNoObservableHindLimbMovement(self, hip, knee, ankle):
        return  (hip == MovementType.NONE) and (knee == MovementType.NONE) and (ankle == MovementType.NONE)


    def checkSlightMovementofOneOrTwoJoints(self, hip, knee, ankle):
        pass



    # Methods for getting movement value of specific side
    def getHipMobility(self, animalData, side):
        if side == "LEFT":
            return animalData.getLeftHip()
        if side == "RIGHT":
            return animalData.getRightHip()

    def getKneeMobility(self, animalData, side):
        if side == "LEFT":
            return animalData.getLeftKnee()
        if side == "RIGHT":
            return animalData.getRightKnee()

    def getAnkleMobility(self, animalData, side):
        if side == "LEFT":
            return animalData.getLeftAnkle()
        if side == "RIGHT":
            return animalData.getRightAnkle()


