class DataStorage(object):
    def __init__(self, context):
        self.__session = {context.browser.session_id: []}
        self.__common_data = {context.browser.session_id: dict()}
        self.__user_list = {context.browser.session_id: []}
        self.__emails = {context.browser.session_id: []}

    def store_session(self, context):
        self.__session[context.browser.session_id] = context.session

    def get_session(self, context):
        return self.__session[context.browser.session_id]

    def store_common_data(self, context, key, value):
        self.__common_data[context.browser.session_id][key] = value

    def get_common_data(self, context, key):
        return self.__common_data[context.browser.session_id].get(key, None)

    def store_user(self, context, user):
        self.__user_list[context.browser.session_id].append(user)

    def get_user_list(self, context):
        return self.__user_list[context.browser.session_id]

    def store_mail(self, context, mail):
        self.__emails[context.browser.session_id].append(mail)

    def get_mails(self, context):
        return self.__emails[context.browser.session_id]

    def cleanup(self, context):
        return None
