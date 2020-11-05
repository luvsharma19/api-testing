import configparser


class Configuration:
    global_config_path = 'setup.cfg'
    global_config = configparser.RawConfigParser(allow_no_value=True)
    with open(global_config_path) as configFile:
        global_config.read_file(configFile)
    global_config.sections()

    @staticmethod
    def getConfig(path):
        config = configparser.RawConfigParser(allow_no_value=True)
        with open(path) as configFile:
            config.read_file(configFile)
        config.sections()
        return config
