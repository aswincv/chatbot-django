from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def values(cls):
        return tuple(attr.value for attr in cls)

    @classmethod
    def keys(cls):
        return tuple(attr.name for attr in cls)

    @classmethod
    def get_choices(cls):
        return tuple((attr.value, attr.name) for attr in cls)


class ButtonChoices(BaseEnum):
    STUPID = 1
    FAT = 2
    DUMP = 3
