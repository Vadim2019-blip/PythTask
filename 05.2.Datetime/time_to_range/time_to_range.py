import datetime
import enum
import typing as tp  # noqa


class GranularityEnum(enum.Enum):
    """
    Enum for describing granularity
    """
    DAY = datetime.timedelta(days=1)
    TWELVE_HOURS = datetime.timedelta(hours=12)
    HOUR = datetime.timedelta(hours=1)
    THIRTY_MIN = datetime.timedelta(minutes=30)
    FIVE_MIN = datetime.timedelta(minutes=5)


def truncate_to_granularity(dt: datetime.datetime, gtd: GranularityEnum) -> datetime.datetime:
    """
    :param dt: datetime to truncate
    :param gtd: granularity
    :return: resulted datetime
    """
    if gtd == GranularityEnum.FIVE_MIN:
        return dt.replace(minute=dt.minute - (dt.minute % 5), second=0, microsecond=0)
    elif gtd == GranularityEnum.THIRTY_MIN:
        return dt.replace(minute=dt.minute - (dt.minute % 30), second=0, microsecond=0)
    elif gtd == GranularityEnum.HOUR:
        return dt.replace(minute=0, second=0, microsecond=0)
    elif gtd == GranularityEnum.TWELVE_HOURS:
        return dt.replace(hour=dt.hour - (dt.hour % 12), minute=0, second=0, microsecond=0)
    elif gtd == GranularityEnum.DAY:
        return dt.replace(hour=0, minute=0, second=0, microsecond=0)

class DtRange:
    def __init__(
            self,
            before: int,
            after: int,
            shift: int,
            gtd: GranularityEnum
) -> None:
        """
        :param before: number of datetimes should take before `given datetime`
        :param after: number of datetimes should take after `given datetime`
        :param shift: shift of `given datetime`
        :param gtd: granularity
        """
        self._before = before
        self._after = after
        self._shift = shift
        self._gtd = gtd

    def __call__(self, dt: datetime.datetime) -> tp.List[datetime.datetime]:
        """
        :param dt: given datetime
        :return: list of datetimes in range
        """
        R_dt = truncate_to_granularity(dt, self._gtd)
        shifts1 = []
        for shift in range(-self._before + self._shift, self._after + self._shift + 1):
            shifts1.append(tp.cast(datetime.timedelta, self._gtd.value) * shift)

        return [R_dt + i for i in shifts1]


def get_interval(
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        gtd: GranularityEnum
) -> list[datetime.datetime]:
    """
    :param start_time: start of interval
    :param end_time: end of interval
    :param gtd: granularity
    :return: list of datetimes according to granularity
    """

    def truncate_and_round_up(dt: datetime.datetime) -> datetime.datetime:
        R_dt = truncate_to_granularity(dt, gtd)
        if dt - R_dt > datetime.timedelta(0):
            R_dt += gtd.value
        return R_dt

    ceil_dt = truncate_and_round_up(start_time)
    rounded_end = truncate_to_granularity(end_time, gtd)

    return [ceil_dt + i * gtd.value for i in range((rounded_end - ceil_dt) // gtd.value + 1)]

