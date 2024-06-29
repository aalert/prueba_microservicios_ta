import re

DAYS = re.compile(r"(\d+d)")
HOURS = re.compile(r"(\d+h)")
MINUTES = re.compile(r"(\d+m)")
WRONG_LETTERS = re.compile(r"[^dmh,\d\s]+")
LETTER_WITHOUT_NUMBER = re.compile(r"\b(?<!\d)[mhd]\b")


def parse_absolutime_time(absolute_time: str) -> tuple[str, str, str]:
    """
    Parse absolutime time from a string with the format *15m, 3h, 2d* to
    a tuple with the format (hours, minutes, seconds)
    ej parse_absolutime_time("15m, 3h, 2d") -> (15, 3, 2)
    """
    absolute_time = absolute_time.lower()

    days = re.findall(DAYS, absolute_time)
    hours = re.findall(HOURS, absolute_time)
    minutes = re.findall(MINUTES, absolute_time)

    if len(days) > 1 or len(hours) > 1 or len(minutes) > 1:
        raise ValueError("Invalid time format")

    if not days and not hours and not minutes:
        raise ValueError("Invalid time format")

    if re.search(WRONG_LETTERS, absolute_time):
        raise ValueError("Invalid time format")

    if re.search(LETTER_WITHOUT_NUMBER, absolute_time):
        raise ValueError("Invalid time format")

    result_tuple = (
        minutes[0] if minutes else None,
        hours[0] if hours else None,
        days[0] if days else None,
    )

    return result_tuple


