from datetime import datetime, timedelta

REPLACEMENT_CHAR_VALUE = 0xFFFD
DURATION_FORMAT = '%H:%M:%S.%f'
TIMESTAMP_FORMAT = '%m/%d/%y %I:%M:%S %p'
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def contains_invalid_unicode(string: str) -> bool:
    # Checks if string has Unicode replacement character, indicating invalid UTF-8 char
    
    return string.find(chr(REPLACEMENT_CHAR_VALUE)) != -1


def format_timestamp(timestamp: str) -> str:
    # Takes in timestamp string and converts to Eastern timezone in RFC3339 format if valid

    if contains_invalid_unicode(timestamp):
        raise ValueError
    western_timestamp = datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    eastern_timestamp = western_timestamp - timedelta(hours=3)
    return eastern_timestamp.isoformat('T') + 'Z'


def format_address(address: str) -> str:
    # Checks if address string contains invalid Unicode and throws error if it does

    if contains_invalid_unicode(address):
        raise ValueError
    return address


def format_zip(zipcode: str) -> str:
    # Appends zeroes to zipcode string so it is of length 5

    zeroes_to_append = 5 - len(zipcode)
    return ('0' * zeroes_to_append) + zipcode


def format_name(name: str) -> str:
    # Formats name by returning uppercase conversion, taking non-English characters into account
    
    return name.upper()


def format_duration(duration: str) -> str:
    # Parses duration string and returns amount of seconds duration represents

    hours, minutes, seconds_and_ms = duration.split(':')
    return str(float(hours) * SECONDS_IN_HOUR + float(minutes) * SECONDS_IN_MINUTE + float(seconds_and_ms))



