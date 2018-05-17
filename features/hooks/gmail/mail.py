from lxml import etree


class Mail(object):

    def __init__(self, id, message):
        self.__dict__ = {
            'id': id,
            'message': message
        }

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return str(self.__dict__)

    def get_body_text(self):
        root = etree.HTML(self.__dict__['message'])
        lines = root.xpath('.//tr[2]/*[@class="padding"]/text()')
        return ''.join(lines)

    def get_action_link(self):
        root = etree.HTML(self.__dict__['message'])
        return root.xpath('.//*[contains(@id,"action-link")]/@href')[0]

    def get_security_code(self):
        root = etree.HTML(self.__dict__['message'])
        chars = root.xpath('normalize-space(//*[@id="temp-password"])')
        return ''.join(chars)
