

class AnimalData:
    def __init__(self):
        self.leftHip = MovemventType.SLIGHT
        self.leftKnee = MovemventType.SLIGHT
        self.leftAnkle = MovemventType.SLIGHT
        self.rightHip = MovemventType.NONE
        self.rightKnee = MovemventType.NONE
        self.rightAnkle = MovemventType.NONE


    def getLeftHip(self):
        return self.leftHip

    def getLeftKnee(self):
        return self.leftKnee

    def getLeftAnkle(self):
        return self.leftAnkle

    def getRightHip(self):
        return self.rightHip

    def getRightKnee(self):
        return self.leftKnee

    def getRightAnkle(self):
        return self.rightAnkle

