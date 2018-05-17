import logging
from datetime import datetime
import dateutil
import dateutil.tz
import time


class DataHelper(object):
    logger = logging.getLogger(__name__)

    @staticmethod
    def sort_alphabet_string_list(string_list, reverse=False):
        return sorted(string_list, key=lambda s: s.lower(), reverse=reverse)

    @staticmethod
    def convert_string_list_to_integer_list(string_list):
        return [int(item) for item in string_list]

    @staticmethod
    def convert_string_list_to_float_list(string_list):
        return [float(item) for item in string_list]

    @staticmethod
    def convert_string_list_with_multiple_delimiter_to_float_list(string_list):
        return [float(item.replace(',', '')) for item in string_list]

    @staticmethod
    def convert_string_with_multiple_delimiter_to_float(string):
        return float(string.replace(',', ''))

    @staticmethod
    def get_unique_string_by_time():
        return datetime.now().strftime('%Y%m%d-%H%M%S%f')

    @staticmethod
    def get_local_timezone_name():
        local_timezone = dateutil.tz.tzlocal()
        return local_timezone.tzname(datetime.now(local_timezone))

    @staticmethod
    def exclude_dictionary(dictionary, **criteria):

        excluded_keys = criteria.get('excluded_keys') if 'excluded_keys' in criteria else list()
        excluded_values = criteria.get('excluded_values') if 'excluded_values' in criteria else list()
        result = {}
        for key, value in dict(dictionary).items():
            if key in excluded_keys:
                continue
            if value in excluded_values:
                continue
            result[key] = value
        return result

    @staticmethod
    def switching_keys_and_values_in_a_dictionary(my_dict):
        """
        Switching keys and values in a dictionary in python
        :param my_dict:
        :return:
        Ex:
        my_dict = {2:3, 5:6, 8:9}
        return {3:2, 6:5, 9:8}
        """
        switching_dict = {v: k for k, v in my_dict.iteritems()}
        return switching_dict

    @staticmethod
    def remove_underscore_and_capitalize_word(words):
        """
        Remove underscore and capitalize the first letter of word
        :param words:
        :return:
        """
        words_without_underscore = str(words).replace('_', ' ')
        return words_without_underscore.title()

    @staticmethod
    def get_list_from_string_list(str_array, separator=','):
        return [x.strip() for x in str_array.split(separator)]

    @staticmethod
    def get_sorted_list(entities, by_attribute, reverse=False):
        return sorted(entities, key=lambda k: k[by_attribute], reverse=reverse)

    @staticmethod
    def filter_list_dict_by_dict(list_dict, filter_dict):
        """
        Filter list of dict by filter_dict.
        :param list_dict:
        :param filter_dict:
        :return: Return list of dict match filter_dict
        Ex: list_dict=[{'id': 1, 'v': 11},
                       {'id': 1, 'v': 111},
                       {'id': 2, 'v': 22},
                       {'id': 3, 'v': 33}]
        Case1:
             filter_dict={'id': 1, 'v': 11}
          => return [{'id': 1, 'v': 11}]

        Case2:
             filter_dict={'id': 1}
          => return [{'id': 1, 'v': 11}, {'id': 1, 'v': 111}]
        """

        result_list = []
        for item in list_dict:
            count_match = len(filter_dict.keys())
            count_check = 0
            if set(filter_dict.keys()).issubset(set(item.keys())):
                for k, v in filter_dict.items():
                    if v == item[k]:
                        count_check += 1
            if count_check == count_match:
                result_list.append(item)
            else:
                continue
        return result_list

    @staticmethod
    def get_value_of_key_from_list_dict(list_dict, selected_key):
        """
        Get value of key from list dict
        :param list_dict:
        :param selected_key:
        :return: list of values that have selected_key in each dict
        Ex: list_dict=[{'id': 1, 'v': 11},
                       {'id': 2, 'v': 22},
                       {'id': 3, 'v': 33}]
             selected_key='id'
          => return [1,2,3]
        """
        result_list = []
        for dict_item in list_dict:
            if selected_key in dict(dict_item).keys():
                result_list.append(dict_item.get(selected_key))
        return result_list

    @staticmethod
    def get_value_from_nested_dict(data_dict, map_str, separator='.'):
        """
            Get value from nested dict
        :param data_dict:
        :param map_str: key1.key2.key3
        :param separator: for split map string of path. Default: '.'
        :return:
        Ex: list_dict={{'id1': {'value':'1'}},
                       {'id2': {'value':'2'}},
                       {'id3': {'value':'3'}}
             map_str='id1.value'
          => return '1'
        """
        map_list = str(map_str).split(separator)
        pointer = data_dict
        value = None
        try:
            for ind in range(len(map_list)):
                key = map_list[ind]
                if isinstance(pointer, list):
                    if ind == len(map_list) - 1:
                        value = pointer[int(key[1:-1])]
                        return value
                    pointer = pointer[int(key[1:-1])]
                elif ind == len(map_list) - 1:
                    value = pointer[key]
                    return value
                elif key in pointer:
                    pointer = pointer[key]
            return value
        except (KeyError, TypeError, IndexError):
            return None

    @staticmethod
    def set_value_to_nested_dict(dict_data, map_str, value, separator='.'):
        """
            Set value to nested dict
        :param dict_data:
        :param map_str: key1.key2.key3
        :param value:
        :param separator: for split map string of path. Default: '.'
        :return:
        """
        map_list = str(map_str).split(separator)
        pointer = dict_data
        for ind in range(len(map_list)):
            key = map_list[ind]
            if '[' in key:
                if ind == len(map_list) - 1:
                    pointer[int(key[1:-1])] = value
                    return
                pointer = pointer[int(key[1:-1])]
            elif ind == len(map_list) - 1:
                pointer[key] = value
                return
            elif key in pointer:
                pointer = pointer[key]
            else:
                pointer[key] = {}
                pointer = pointer[key]

    @staticmethod
    def convert_list_to_string(list_tmp, separator=','):
        """
        Convert list to string
        :param list_tmp:
        :param separator:
        :return:
        Ex: list_str=['1','2','3','4','5']
          => return '1,2,3,4,5'
        """
        result_str = list_tmp
        if isinstance(list_tmp, list):
            result_str = str(separator.join(list_tmp))
        return result_str

    @staticmethod
    def format_unicode_to_right_format_string(invalid_format_unicode):
        """
        Convert unicode string to right format string
        :param invalid_format_unicode:
        :return:
        """
        return str(invalid_format_unicode.encode('ascii', 'ignore').decode('ascii')).replace('\n', '')

    @staticmethod
    def format_unicode_to_right_format_string_of_list(invalid_format_unicode_list):
        """
        Convert unicode string to right format string of all elements in list
        :param invalid_format_unicode_list:
        :return:
        """
        result_list = []
        for item in invalid_format_unicode_list:
            result_list.append(DataHelper.format_unicode_to_right_format_string(item))
        return result_list

    @staticmethod
    def convert_unicode_list_to_string_list(unicode_list):
        return [x.encode('UTF8') for x in unicode_list]

    @staticmethod
    def replace_old_to_new_value_from_string_list(string_list, old, new=''):
        return [item.replace(old, new) for item in string_list]

    @staticmethod
    def wait_until_match_condition(time_out, error, method, *args):
        """
        Wait until method return True. This is often applied to wait the the returned result of API
        :param time_out:
        :param error: error when timeout
        :param method:
        :param args: all arguments for method
        :return:
        """
        count_loop = 0
        interval_wait = 5
        while True:
            condition = method(*args)
            if condition:
                return True
            time.sleep(interval_wait)
            count_loop += 1
            if (interval_wait * count_loop) > time_out:
                raise RuntimeError(error)

    @staticmethod
    def remove_space_in_element_of_string_list(string_list):
        return [element.replace(' ', '') for element in string_list]

    @staticmethod
    def first_lower(s):
        return s[0].lower() + s[1:]

    @staticmethod
    def remove_duplicate_dict_from_a_list(dict_list):
        new_dict_list = []

        for item in dict_list:
            if item not in new_dict_list:
                new_dict_list.append(item)
        return new_dict_list

    @staticmethod
    def remove_key_from_a_dict_list(dict_list, key):
        for item in dict_list:
            item.pop(key)
        return dict_list

    @staticmethod
    def compare_list_in_list_in_order(child_list, parent_list):
        if child_list[0] not in parent_list:
            return False
        index = parent_list.index(child_list[0])
        new_list = []
        for item in parent_list[index:index+len(child_list)]:
            new_list.append(item)
        new_list_str = ','.join(new_list)
        child_list_str = ','.join(child_list)
        if child_list_str != new_list_str:
            return False
        return True

    @staticmethod
    def remove_leading_and_ending_spaces_from_a_list(string_list):
        return [element.strip() for element in string_list]
