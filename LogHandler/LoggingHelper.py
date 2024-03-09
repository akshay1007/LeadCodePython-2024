# Databricks notebook source
# MAGIC %md
# MAGIC # LoggingHelper Class Documentation
# MAGIC
# MAGIC ## Overview
# MAGIC The `LoggingHelper` class provides functionalities to define loggers, handle log files, and move them to DBFS (Databricks File System) from the cluster through relevant methods.
# MAGIC
# MAGIC ## Class: LoggingHelper
# MAGIC
# MAGIC ### Description
# MAGIC A class and its members are used to define loggers, FileHandlers, and to move log files to DBFS from the cluster through relevant getter and setter methods.
# MAGIC
# MAGIC ### Constructor: `__init__(self, target_container=None, target_directory=None, target_filename=None, load_log_date=None, logger_prefix=None, curr_clust_id=None)`
# MAGIC
# MAGIC #### Description
# MAGIC Initializes a LoggingHelper object.
# MAGIC
# MAGIC If all the arguments are passed as None, it will initialize a dummy logger only able to print information onto the console.
# MAGIC
# MAGIC #### Arguments
# MAGIC - `target_container` (str, optional): The container in the storage account where this log file should be stored.
# MAGIC - `target_directory` (str, optional): The directory in the container where this log file should be stored.
# MAGIC - `target_filename` (str, optional): The name with which the log should be stored.
# MAGIC - `load_log_date` (str, optional): The date when this log was generated.
# MAGIC - `logger_prefix` (str, optional): The prefix of the logger (with which the log was recorded).
# MAGIC - `curr_clust_id` (str, optional): The computing cluster where this job was executed (i.e., where the log was generated).
# MAGIC
# MAGIC ### Attributes
# MAGIC - `MDP_LOGGER`: If all constructor arguments are None, a dummy logger is initialized. Otherwise, the logger is initialized based on the provided parameters.
# MAGIC
# MAGIC ### Methods
# MAGIC - No public methods are defined in the provided code.
# MAGIC

# COMMAND ----------

import os

class LoggingHelper:
    '''A class and its members are used to define loggers, FileHandlers and to move log files to DBFS from cluster through relevant getter and setter methods'''
    
    def __init__(self,
                 target_container=None,
                 target_directory=None,
                 target_filename=None,
                 load_log_date=None,
                 logger_prefix=None,
                 curr_clust_id=None):
        '''Initializes a LoggingHelper object.
        
        If all the arguments are passed as None, it will initialize a dummy logger only able to print information onto the console.
        
        Args:
            target_container (str, optional): The container in the storage account where this log file should be stored.
            target_directory (str, optional): The directory in the container where this log file should be stored.
            target_filename (str, optional): The name with which the log should be stored.
            load_log_date (str, optional): The date when this log was generated.
            logger_prefix (str, optional): The prefix of the logger (with which the log was recorded).
            curr_clust_id (str, optional): The computing cluster where this job was executed (i.e., where the log was generated).
        '''
        if all(arg is None for arg in [target_container, target_directory, target_filename, load_log_date, curr_clust_id]):
            self.MDP_LOGGER = type('', (object,), {"info": lambda x: print(x), "error": lambda x: print(x)})
        else:
            self.logger_prefix = logger_prefix
            self.log_name = f"{self.logger_prefix}_Runtime.log"
            self.driver_log_path = f"/databricks/driver/logs/{self.log_name}"
            self.adls_log_path = f'/mnt/mdp/log/{target_container}/{target_directory}/{target_filename}/{load_log_date}/{curr_clust_id}'
            self.generic_logger_properties = f"""
                log4j.logger.{self.logger_prefix}=INFO, mdpNBRunLogFile 
                log4j.appender.mdpNBRunLogFile=org.apache.log4j.DailyRollingFileAppender
                log4j.appender.mdpNBRunLogFile.File=logs/{self.log_name}
                log4j.appender.mdpNBRunLogFile.layout=org.apache.log4j.PatternLayout
                log4j.appender.mdpNBRunLogFile.layout.ConversionPattern={{'logger.name':'%c', 'level':'%p', 'timestamp':'%d{{yyyy-MM-dd HH:mm:ss,SSS}}', 'message':'%m'}}%n"""
            self.log4j_custom_properties_path = f'/databricks/runtime_log4j_properties/{curr_clust_id}_{self.logger_prefix}_log4j_custom_logger.properties'
            dbutils.fs.put('dbfs:'+self.log4j_custom_properties_path, self.generic_logger_properties, True)
            self.log4jLogger = sc._jvm.org.apache.log4j
            os.sync()
            self.log4jLogger.PropertyConfigurator.configure('/dbfs'+self.log4j_custom_properties_path)

