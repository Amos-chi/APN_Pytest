# Time : 2023/2/21 17:18
from log import logger

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
class pylogger():

    alogger = logger.get_logger(debug_level='INFO',to_file=True)
