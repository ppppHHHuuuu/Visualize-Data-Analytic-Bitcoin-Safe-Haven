from datetime import datetime
def str_to_timestamp(date_str: str) -> int:
    """
    Convert a string date to a timestamp.

    :param date_str: The string date.
    :return: The timestamp.
    """
    if "EEST" in date_str:
        date_str = date_str.replace(" EEST", " ")
    if ("EET" in date_str):
        date_str = date_str.replace(" EET", " ")
    date_str = date_str.rstrip()
    timestamp = int(datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').timestamp() )

    return timestamp
def timestamp_to_str(timestamp: int) -> str:
    """
    Convert a timestamp to a string date.

    :param timestamp: The timestamp.
    :return: The string date.
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
def round_to_nearest_minute(timestamp: int) -> int:
    quotient, remainder = divmod(timestamp, 60)
    if remainder >= 30:
        quotient += 1
    return quotient * 60
# print (str_to_timestamp("2018-10-23 02:51:15 EEST"))