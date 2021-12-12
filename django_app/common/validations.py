import re


class RegexValidations:
    # To validate 29-10-2021 date format
    DATE_FORMAT = r"([\d{2}])+-([\d{2}])+-([\d{4}])"
    # To validate 13:20 date format
    TIME_FORMAT = r"(?:[01]\d|2[0123]):(?:[012345]\d)"
    # To validate positive numbers
    POSITIVE_NUMBER = r"(\d+)"


def validate_date_format(date, regex=RegexValidations.DATE_FORMAT):
    return validate_regex(date, regex)


def validate_time_format(time, regex=RegexValidations.TIME_FORMAT):
    return validate_regex(time, regex)


def validate_positive_number(number, regex=RegexValidations.POSITIVE_NUMBER):
    return validate_regex(number, regex)


def validate_regex(string, regex):
    return re.match(regex, string)
