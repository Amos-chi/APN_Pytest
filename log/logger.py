"""
LOG_FileHandler is to write all logs into LOG_FILENAME
"""
import datetime
import os
import logging
import sys
import time


date_ = datetime.datetime.now().strftime('%Y-%m-%d')
date_dir = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\log' + '\\' + date_


TIME_FORMAT = "%Y-%m-%dT%XZ%Z"  # year_month_day_time_weekdayinnumber_timezone
LOG_FILENAME = f"{date_dir}/" + ("dbg_" if __debug__ else "log_") + \
               time.strftime(TIME_FORMAT).replace(":", "：") + ".log"  # colon (:) cannot use in windows


class Logger:
    def __init__(self, log_format, file_name):
        self._format = log_format
        self._file_name = file_name
        self._default_level = os.environ.get('DEBUG_LEVEL', 'NOTSET')
        self._to_file = os.environ.get('LOG_TO_FILE', None)
        if self._to_file:
            self._to_file = self._to_file.lower() == 'true'
        self._to_stdout = os.environ.get('LOG_TO_STDOUT', None)
        if self._to_stdout:
            self._to_stdout = self._to_stdout.lower() == 'true'

    def get_logger(self, debug_level, name=__name__, to_file=False, to_stdout=True):
        """
        Get the logger instance
        :param name: name of the logger, normally it is the module name
        :param debug_level: 'WARN', 'DEBUG', 'INFO', 'WARNING', or 'ERROR'. It will be overlapped by env 'DEBUG_LEVEL'
        :param to_file: do we save the log info to log file
        :param to_stdout: do we output the log to stdout
        :return: the logger instance
        """
        # determine the logging level
        try:
            os_debug_level = getattr(logging, self._default_level)
            request_lev = getattr(logging, debug_level)
        except AttributeError as err:
            raise err
        lev = os_debug_level if os_debug_level > request_lev else request_lev
        # whether or not save to file/stdout
        to_file = to_file if self._to_file is None else self._to_file
        to_stdout = to_stdout if self._to_stdout is None else self._to_stdout
        # set debug level for logger
        logger = logging.getLogger(name)
        logger.propagate = False
        logger.handlers = []  # remove default loggers
        logger.setLevel(lev)
        # set log format
        formatter = logging.Formatter(self._format)
        # setup log file
        if to_file:
            if not os.path.exists(date_dir):
                os.makedirs(date_dir)
            log_file_handler = logging.FileHandler(filename=self._file_name, mode='a', encoding='utf-8', delay=True)
            log_file_handler.setLevel(level=lev)
            log_file_handler.setFormatter(formatter)
            # add file logger to logger
            logger.addHandler(log_file_handler)
        # setup stdout
        if to_stdout:
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setLevel(level=lev)
            stdout_handler.setFormatter(formatter)
            # add stdout logger to logger
            logger.addHandler(stdout_handler)
        return logger


get_logger = Logger('%(asctime)s %(name)s %(levelname)s - %(message)s', LOG_FILENAME).get_logger
