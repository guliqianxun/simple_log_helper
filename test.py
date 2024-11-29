import time
import logging
from simple_log_helper import CustomLogger, LoggerManager

logger = CustomLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
logger.show_progress(50)
@logger.log_function_call
def test_function():
    time.sleep(1)
test_function()
config = {
    'log_folder': './Logs',
    'level': 'INFO',
    'loggers': ['app', 'db'],
    'logger_levels': {
        'db': 'WARNING',
    }
}

# Initialize the LoggerManager with the configuration
logger_manager = LoggerManager(config)

# Get loggers
app_logger = logger_manager.get_logger('app')
db_logger = logger_manager.get_logger('db')
test_logger = logger_manager.get_logger('test')
db_logger.info('This is an info message from db logger.')
db_sub_logger = db_logger.getChild('sub')
db_sub_logger.propagate = False
db_sub_logger.info('This is a child logger message.')


# Use the loggers
app_logger.info('This is an info message from app logger.')
db_logger.warning('This is a warning message from db logger.')
test_logger.debug('This is a debug message from test logger.')
test_logger.error('This is an error message from test logger.')

# Use the custom methods
@app_logger.log_function_call
def sample_function(x, y):
    return x + y

result = sample_function(5, 7)
app_logger.show_progress(75)

# Shutdown the loggers when done
logger_manager.shutdown()

