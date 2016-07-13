# coding=utf-8

CONF_FILE = 'config.ini'

class SingletonMeta(type):  
    def __init__(cls, name, bases, dict):  
        super(SingletonMeta, cls).__init__(name, bases, dict)  
        cls._instance = None  

    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kw)  
        return cls._instance


class Configure(object):

    __metaclass__ = SingletonMeta

    def __init__(self, ini=CONF_FILE):
        from ConfigParser import ConfigParser
        config = ConfigParser(defaults={'name':'Winning Health PACS+ Patient Data Upload Service', 'port':'9000'})
        config.read(ini)
        self.config = config

    def get(self, section, option):
        return self.config.get(section, option)

    def get_default(self, section, option, default=None):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        else:
            return default




if __name__ == '__main__':
    a = Configure()
    print a.get('SERVICE','port','23')