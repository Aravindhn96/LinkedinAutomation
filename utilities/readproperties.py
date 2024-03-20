import configparser
import utilities.customLogger as cl
import logging


log = cl.customLogger(logging.DEBUG)
config = configparser.RawConfigParser()
config.read(".\\utilities\\config.ini")

class readconfig():
    
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url  

    @staticmethod
    def getUserEmail():
        userEmail = config.get('common info', 'username')
        return userEmail

    @staticmethod
    def getpassword():
        userPassword = config.get('common info', 'password')
        return userPassword

        