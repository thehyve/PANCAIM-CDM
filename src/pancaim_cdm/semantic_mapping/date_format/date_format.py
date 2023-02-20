from enum import Enum


class DateFormat(Enum):
    # For supported date formats, see: https://strftime.org/
    YMD = '%Y-%m-%d'
    YM = '%Y-%m'
    Y = '%Y'
