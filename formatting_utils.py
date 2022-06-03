from datetime import datetime


REPLACEMENT_CHAR_VALUE = 0xFFFD
DURATION_FORMAT = '%H:%M:%S.%f'
TIMESTAMP_FORMAT = '%m/%d/%y %I:%M:%S %p'
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def contains_invalid_unicode(string: str) -> bool:
    return string.find(chr(REPLACEMENT_CHAR_VALUE)) != -1


def format_timestamp(timestamp: str) -> str:
    if contains_invalid_unicode(timestamp):
        raise ValueError
    datetime_timestamp = datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    print(datetime_timestamp)
    return ''


def format_address(address: str) -> str:
    if contains_invalid_unicode(address):
        raise ValueError
    return address


def format_zip(zipcode: str) -> str:
    zeroes_to_append = 5 - len(zipcode)
    return ('0' * zeroes_to_append) + zipcode


def format_duration(duration: str) -> str:
    hours, minutes, seconds_and_ms = duration.split(':')
    return str(float(hours) * SECONDS_IN_HOUR + float(minutes) * SECONDS_IN_MINUTE + float(seconds_and_ms))



