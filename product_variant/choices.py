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


class TireSizes():
    HEIGHT_CHOICES = [
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
    ]
    TIRE_CHOICES = [
        ('Height', (
            ('TWENTY_EIGHT', '28'),
            ('TWENTY_NINE', '29'),
            ('THIRTY', '30'),
            ('THIRTY_ONE', '31'),
            ('THIRTY_TWO', '32'),
            ('THIRTY_THREE', '33'),
            ('THIRTY_FIVE', '34'),
            ('THIRTY_FIVE', '35'),
        )
        ),
        ('Width', (
            ('NINE', '9'),
            ('TEN', '10'),
        )
        ),
    ]
    '''
    28x9x14
    28x9x15
    28x10x14
    28x10x15
    
    28x9
    30x10

  '''
