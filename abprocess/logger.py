import logging
from dataclasses import dataclass, Field
from logging.handlers import RotatingFileHandler


@dataclass
class LogFileHandler:

    logger: logging.getLogger
    log_level: logging = logging.INFO
    formatter: logging = logging.Formatter('%(asctime)s :: %(levelname)s :: %(funcName)s :: %(message)s')


    def set_log_configuration(self):

        self.logger.setLevel(self.log_level)

        file_handler = RotatingFileHandler('/Users/amarcade/Documents/ADSL_connector/abprocess.log', 'a', 100000, 1)
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(self.formatter)

        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.log_level)
        stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(stream_handler)

