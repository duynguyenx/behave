class DataHelper:

    @staticmethod
    def get_list_from_string_list(str_array, separator=','):
        return [x.strip() for x in str_array.split(separator)]

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
    def convert_key_value_table_to_dictionary(table):
        result = {}
        for key, value in table:
            result[key] = value
        return result
