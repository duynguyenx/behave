import json
import logging
import requests
from conf.env_setup import EnvSetup
from features.hooks.api import api_constants
from features.hooks.api.api_error import APIError
from features.hooks.api.data_helper import DataHelper


class RequestHelper(object):
    logger = logging.getLogger(__name__)

    @staticmethod
    def print_response_json(request):
        RequestHelper.logger.debug('Response code: %s', request.status_code)
        if request.status_code not in [204, 404]:
            RequestHelper.logger.debug(u'''Response json:
            {json}'''.format(json=request.json()))

    @staticmethod
    def send_post_request(session, end_point, data='', header={}):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending POST request
        URL  = {url}
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        if not header:
            header = {'content-type': 'application/json'}
        headers.update(header)
        response = requests.post(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_put_request(session, end_point, data='', header={}):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending PUT request
        URL  = {url}
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        if not header:
            header = {'content-type': 'application/json'}
        headers.update(header)
        response = requests.put(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_patch_request(session, end_point, data='', header={}):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending PATCH request
        URL  = {url}
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        if not header:
            header = {'content-type': 'application/json'}
        headers.update(header)
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_delete_request(session, end_point, data='', header={}):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending DELETE request
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        if not header:
            header = {'content-type': 'application/json'}
        headers.update(header)
        response = requests.delete(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_get_request(session, end_point):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending GET request
        URL  = {url}'''.format(url=url))
        response = requests.get(url, headers=session.get_auth_token())
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def get_all_responses_with_paging_by_next(session, endpoint, error_message, cursors, separator='.'):
        result_list = []
        url = EnvSetup.API_HOST + endpoint
        while True:
            response = requests.get(url, headers=session.get_auth_token())
            if response.status_code != api_constants.RESPONSE_CODE_SUCCESSFUL:
                error_message = '{custom_message}. API error: {api_error}'.format(custom_message=error_message,
                                                                                  api_error=response.text)
                raise APIError(error_message)
            result_list += response.json().get('data')
            dict_paging = DataHelper.get_value_from_nested_dict(response.json(),
                                                                str(cursors).rsplit(separator, 1)[0])
            if not dict_paging or 'next' not in dict_paging.keys():
                break
            url = dict_paging.get('next')
            if 'previous' in dict_paging.keys():
                previous_url = dict_paging.get('previous')
                if previous_url == url:
                    break
        return result_list

    @staticmethod
    def get_all_responses_with_paging_by_next_url(session, endpoint, error_message, cursors,
                                                  data_cursor='data', separator='.'):
        result_list = []
        while True:
            response = RequestHelper.send_get_request(session, endpoint)
            if response.status_code != api_constants.RESPONSE_CODE_SUCCESSFUL:
                error_message = '{custom_message}. API error: {api_error}'.format(custom_message=error_message,
                                                                                  api_error=response.text)
                raise APIError(error_message)
            data = DataHelper.get_value_from_nested_dict(response.json(), data_cursor)
            result_list += data
            dict_paging = DataHelper.get_value_from_nested_dict(response.json(),
                                                                str(cursors).split(separator)[0])
            next_ulr = dict_paging.get(str(cursors).split(separator)[-1])
            if next_ulr == '':
                break
            endpoint = next_ulr
        return result_list

    @staticmethod
    def is_valid_url(session, endpoint):
        response = RequestHelper.send_get_request(session, endpoint)
        if response.status_code not in (api_constants.RESPONSE_CODE_SUCCESSFUL,
                                        api_constants.RESPONSE_CODE_SUCCESSFUL_NO_CONTENT):
            return False
        return True
