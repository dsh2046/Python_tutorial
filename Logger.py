import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)      # 设置默认等级（共５个等级: WARNING, INFO, DEBUG, CRITICAL, ERROR）

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')  # 设置日志文件的显示格式

file_handler = logging.FileHandler('sample.log')　　＃　输出到文件
file_handler.setLevel(logging.ERROR)               ＃　设置日志文件等级
file_handler.setFormatter(formatter)　　　　　　　　　＃　设置日志文件格式

stream_handler = logging.StreamHandler()   # 输出到屏幕上显示
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def dv(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.exception('divided by zero!')
    else:
        return result

dv(4, 0)
