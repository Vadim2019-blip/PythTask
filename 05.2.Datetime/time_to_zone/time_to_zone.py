from datetime import datetime

import dateutil.tz


DEFAULT_TZ_NAME = "Europe/Moscow"


def transformation(dt: datetime) -> datetime:

    if dt.tzinfo is None:
        return dt.replace(tzinfo=dateutil.tz.gettz(DEFAULT_TZ_NAME))
    else:
        return dt.astimezone(dateutil.tz.gettz(DEFAULT_TZ_NAME))


def now() -> datetime:
    """
    Returns the current datetime in the default timezone.

    :return: The current datetime in the default timezone.
    """
    # Get the current datetime in UTC.
    dt_utc = datetime.now(dateutil.tz.tzutc())

    # Convert the current datetime to the default timezone.
    dt_in_default_tz = dt_utc.astimezone(dateutil.tz.gettz(DEFAULT_TZ_NAME))

    # Return the current datetime in the default timezone.
    return dt_in_default_tz

def strftime(dt: datetime, fmt: str) -> str:
    """
    Converts a datetime object to a string in the default timezone.

    :param dt: The datetime object to convert.
    :param fmt: The format string to use.
    :return: The converted string.
    """
    # Convert the datetime object to the default timezone.
    dt_in_default_tz = transformation(dt)

    # Convert the datetime object to a string.
    dt_str = dt_in_default_tz.strftime(fmt)

    # Return the converted string.
    return dt_str

def strptime(dt_str: str, fmt: str) -> datetime:
    """
    Converts a string to a datetime object in the default timezone.

    :param dt_str: The string to convert.
    :param fmt: The format string to use.
    :return: The converted datetime object.
    """
    # Parse the string into a datetime object.
    dt = datetime.strptime(dt_str, fmt)

    # Convert the datetime object to the default timezone.
    dt_in_default_tz = transformation(dt)

    # Return the datetime object in the default timezone.
    return dt_in_default_tz



def diff(first_dt: datetime, second_dt: datetime) -> int:
    """
    Calculates the difference between two datetime objects in seconds.

    :param first_dt: The first datetime object.
    :param second_dt: The second datetime object.
    :return: The difference between the two datetime objects in seconds.
    """
    # Convert the datetime objects to the default timezone.
    first_dt_in_default_tz = transformation(first_dt)
    second_dt_in_default_tz = transformation(second_dt)

    # Calculate the difference between the two datetime objects in seconds.
    diff = int((second_dt_in_default_tz - first_dt_in_default_tz).total_seconds())

    # Return the difference in seconds.
    return diff



def timestamp(dt: datetime) -> int:
    """
    Converts a datetime object to a timestamp in the default timezone.

    :param dt: The datetime object to convert.
    :return: The timestamp in the default timezone.
    """
    # Convert the datetime object to the default timezone.
    dt_in_default_tz = transformation(dt)

    # Convert the datetime object to a timestamp.
    timestamp = dt_in_default_tz.timestamp()

    # Return the timestamp.
    return int(timestamp)


def from_timestamp(ts: int) -> datetime:
    # Create a datetime object from the timestamp in UTC.
    dt = datetime.fromtimestamp(ts, dateutil.tz.tzutc())

    # Convert the datetime object to the default timezone.
    dt_in_default_tz = dt.astimezone(dateutil.tz.gettz(DEFAULT_TZ_NAME))

    # Return the datetime object in the default timezone.
    return dt_in_default_tz