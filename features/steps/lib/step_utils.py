from datetime import datetime
import pytz
# This is util file


def is_x_less_than_y (x, y):
    if hasattr(x, 'lower') and hasattr(y, 'lower'):
        # if they are strings, lower it first for comparison
        x = x.lower()
        y = y.lower()
    return x < y


""" This function checks if all elements in the given lst is monotonically increasingly, returns None if it is.
 Otherwise returns the first element that violates the rule
  For example, [1, 2, 3, 5, 7, 7, 8, 10] will return None
               [1, 3, 4, 7, 5, 8, 10, 9] will return 7

    If reverse is True, it will check if lst is monotonically decreasingly instead
"""


def find_bad_element_from_monotonically_increasing_list(lst, reverse=False):
    """ This function checks if all elements in the given lst is monotonically increasingly, returns None if it is.
     Otherwise returns the first element that violates the rule
      For example, [1, 2, 3, 5, 7, 7, 8, 10] will return None
                   [1, 3, 4, 7, 5, 8, 10, 9] will return 7

        If reverse is True, it will check if lst is monotonically decreasingly instead
    """
    prev = lst.pop(0)   # Pop out the first element from the lst and store it to prev
    for e in lst:       # At this point lst does not have the first element
        if (not reverse and is_x_less_than_y(e, prev)) or (reverse and is_x_less_than_y(prev, e)):
            return prev
        prev = e
    return None


def str2bool(s):
    return s.lower() in ("true", "yes", "t", "1", "is")


def is_str_none(s):
    return s in ("None", "none")


def status_str2bool(status):
    return status.strip().lower() in ('active', 'activated', 're-activated', 'on', 'enable', 'displayed', 'checked')


def extract_digits_from_str(s):
    import re
    return re.findall(r'\d+', s)


def ordinal_str_to_indexes(s):
    ordinal_nums = extract_digits_from_str(s)
    return [int(num)-1 for num in ordinal_nums]


def ordinal_str_to_single_index(s):
    return ordinal_str_to_indexes(s)[0]


def table_to_str(table):
    result = ''
    if table.headings:
        result = '|'
    for heading in table.headings:
        result += heading + '|'
    result += '\n'
    for row in table.rows:
        if row.cells:
            result += '|'
        for cell in row.cells:
            result += cell + '|'
        result += '\n'
    return result


def generate_timezone_offset_and_name_included_dst(timezone_name):
    # Get timezone name and offset included DST
    time_zone_code = timezone_name.replace(' ', '_')
    timezone_offset = datetime.now(pytz.timezone(time_zone_code)).strftime('%z')
    return generate_custom_format_of_timezone(timezone_offset, timezone_name)


def generate_custom_format_of_timezone(timezone_offset, timezone_name):
    """
    Convert to a format.
    For ex: (GMT-10:00) Pacific/Honolulu
    :param timezone_offset:
    :param timezone_name:
    :return:
    """
    return '(GMT' + str(timezone_offset[:3] + ':' + timezone_offset[3:]) + ') ' + timezone_name.replace('_', ' ')
