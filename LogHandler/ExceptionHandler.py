# Databricks notebook source
# MAGIC %md
# MAGIC # ExceptionHandler Class
# MAGIC
# MAGIC ## Overview
# MAGIC
# MAGIC The `ExceptionHandler` class is designed to create custom exceptions with logging capabilities. It allows for easy integration with PySpark applications, providing a structured way to handle errors and log messages.
# MAGIC
# MAGIC ## Class Structure
# MAGIC
# MAGIC The `ExceptionHandler` class consists of the following components:
# MAGIC
# MAGIC - `__init__`: Initializes an ExceptionHandler object with optional parameters such as logging_helper, logger_prefix, and messages.
# MAGIC - `_initialize_logger`: Private method to initialize the logger based on the provided logging_helper.
# MAGIC - `__str__`: Returns a string representation of the exception, concatenating multiple messages if present.
# MAGIC - `logging_exception`: Logs the exception message using the initialized logger.
# MAGIC
# MAGIC ## Usage
# MAGIC
# MAGIC To use the ExceptionHandler class:
# MAGIC
# MAGIC 1. Create an instance of ExceptionHandler, optionally passing logging_helper, logger_prefix, and messages.
# MAGIC 2. Call the `logging_exception` method to log the exception message.
# MAGIC 3. Optionally, customize the logging behavior by providing a LoggingHelper object and logger_prefix.
# MAGIC

# COMMAND ----------

class ExceptionHandler(Exception):
    ''' A class to create custom exceptions with logging capabilities. '''

    def __init__(self, logging_helper=None, logger_prefix=None, messages=""):
        ''' Initializes an ExceptionHandler object.

        Args:
            logging_helper (LoggingHelper, optional): a LoggingHelper object for logging.
            logger_prefix (str, optional): the prefix of the logger name.
            messages (str or list, optional): the message(s) of the exception.
        '''
        super().__init__()
        self.messages = messages if isinstance(messages, list) else [messages]
        self.logging_helper = logging_helper
        self.logger_prefix = logger_prefix
        self.LOGGER_EXCEPTIONHANDLER = self._initialize_logger()

    def _initialize_logger(self):
        ''' Initializes the logger for exception handling. '''
        if self.logging_helper is None:
            return type('', (object,), {"error": lambda x: print(x)})()
        else:
            return self.logging_helper.log4jLogger.LogManager.getLogger(
                f'{self.logger_prefix}.{self.__module__}.{self.__class__.__name__}'
            )

    def __str__(self):
        return f"MDP ERROR: {' '.join(self.messages)}" if self.messages else 'MDP ERROR: ExceptionHandler has been raised'

    def logging_exception(self):
        ''' Logs the exception message. '''
        if self.logging_helper and self.logger_prefix:
            self.LOGGER_EXCEPTIONHANDLER.error(str(self))
        else:
            print(str(self))

