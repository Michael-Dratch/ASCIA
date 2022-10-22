from enum import Enum


class NullType(Enum):
    NULL = 0


class SectionTypes(Enum):
    EARLY = 0
    INTERMEDIATE = 1
    LATE = 2


class MovementType(Enum):
    NONE = 0
    SLIGHT = 1
    EXTENSIVE = 2


class SideType(Enum):
    LEFT = 0
    RIGHT = 1
    MIDDLE = 2


class FrequencyType(Enum):
    NEVER = 0
    OCCASIONAL = 1
    FREQUENT = 2
    CONSISTENT = 3


class PositionType(Enum):
    INTERNALROTATION = 0
    EXTERNALROTATION = 1
    PARALLEL = 2
    UP = 3
    DOWN = 4


class AbdomenType(Enum):
    DRAG = 0
    PARALLEL = 1
    HIGH = 2


class StabilityType(Enum):
    STABLE = 0
    UNSTABLE = 1
