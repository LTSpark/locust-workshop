import json, logging, os

from fnmatch import fnmatch

class Logger:

    def __init__(self, test_name, log_file_name):
        self.logger = self.__build(test_name, log_file_name)

    @staticmethod
    def create_log_file(log_file_name):
        open(f'{log_file_name}.log', 'w').close()
    
    def __build(self, test_name, log_file_name):

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

        logger = logging.getLogger(test_name)
        handler = logging.FileHandler(f'{log_file_name}.log')

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(handler)
        handler.setFormatter(formatter)

        return logger
    
    def info(self, data):
        self.logger.info(json.dumps(data))

    def debug(self, data):
        self.logger.error(json.dumps(data))

    def error(self, data):
        self.logger.error(json.dumps(data))
