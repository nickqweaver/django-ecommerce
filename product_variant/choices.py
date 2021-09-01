from enum import Enum


class Sizes(Enum):
    XSMALL = "XS"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    XLARGE = "XL"


class BoltPatterns():
    RZR = 'RZR'
    CAN = 'CAN'
    BOLT_PATTERN_CHOICES = [
        (RZR, '14x136'),
        (CAN, '14x156'),
    ]

    def get_choices(self):
        return self.BOLT_PATTERN_CHOICES


class WheelSizes():
    WHEEL_SIZE_CHOICES = [
        (Sizes.XSMALL, '14x8'),
        (Sizes.SMALL, '14x10'),
        (Sizes.MEDIUM, '15x7'),
        (Sizes.LARGE, '15x8'),
        (Sizes.XLARGE, '15x10'),
    ]

    def get_choices(self):
        return self.WHEEL_SIZE_CHOICES
