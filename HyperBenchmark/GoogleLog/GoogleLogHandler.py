from logging import StreamHandler
import datetime
import logging
class GoogleLogHandler(StreamHandler):
    def __init__(self, logger):
        StreamHandler.__init__(self)
        self.logger = logger

    def emit(self, record:dict):
        # add the message to the logger
        self.logger.append(record)
        return