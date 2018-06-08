import configparser as cp

class Config:
    CONFIG_FILE = 'config.ini'
    def readConfig(self):
        conf = cp.SafeConfigParser()
        conf.read(CONFIG_FILE)

config = Config()

print(conf.get('settings', 'host'))
