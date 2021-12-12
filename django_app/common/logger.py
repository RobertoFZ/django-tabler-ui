import logging
import json
# Log configuration
logging.basicConfig(level=logging.INFO)


class LoggerManager:
    FORMAT = '%(asctime)-15s'

    @staticmethod
    def log(data):
        logging.basicConfig(format=LoggerManager.FORMAT)
        logger = logging.getLogger('app-log')
        logger.info(json.dumps(data))
