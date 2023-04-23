import logging, json

# Set up formatter for json logging
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_dict = {
            'timestamp': record.created,
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'file': record.filename,
            'line': record.lineno,
            'function': record.funcName,
            'logger': record.name,
            'exception': None
        }
        if record.exc_info:
            log_dict['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_dict)
    
def setup_logging(logger_name):
    # name the logger
    logger = logging.getLogger(logger_name)

    # create instance of FileHandler
    json_formatter = JsonFormatter()
    file_handler = logging.FileHandler(f'{logger_name}.json')
    file_handler.setFormatter(json_formatter)
    file_handler.setLevel(logging.DEBUG)

    # create instance of StreamHandler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # create a logger and add the console handler to it
    logger = logging.getLogger()
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
