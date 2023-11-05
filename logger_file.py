import logging

def log_function(logger, log_level=logging.DEBUG, message = ''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.log(log_level, f"{message} - {func.__name__}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
def Logger(my_logger):
    logger = logging.getLogger(my_logger)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    filehandler = logging.FileHandler('loging.log')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger

# @log_function(Logger('tezt'), log_level=logging.CRITICAL, message='dorod br too')
# def example_function(x, y):
#     result = x + y
#     return result
#
# result = example_function(2, 3)
