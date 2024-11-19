import time
from loguru import logger
from core.config import settings

# logger.remove(handler_id=None)

# 获取日志路径
log_path = settings.LOG_PATH
# 创建日志路径，如果不存在则创建
log_path.mkdir(parents=True, exist_ok=True)

# 获取日志路径下的info日志文件名，格式为info_年-月-日.log
log_path_info = log_path.joinpath(f"info_{time.strftime('%Y-%m-%d')}.log")
# 获取日志路径下的error日志文件名，格式为error_年-月-日.log
log_path_error = log_path.joinpath(f"error_{time.strftime('%Y-%m-%d')}.log")

# 添加info日志记录，每天凌晨0点进行日志切割，保留7天内的日志，使用队列进行异步写入，编码格式为UTF-8，日志级别为INFO
info = logger.add(log_path_info, rotation="00:00", retention="7 days", enqueue=True, encoding="UTF-8", level="INFO")
# 添加error日志记录，每天凌晨0点进行日志切割，保留3天内的日志，使用队列进行异步写入，编码格式为UTF-8，日志级别为ERROR
error = logger.add(log_path_error, rotation="00:00", retention="7 days", enqueue=True, encoding="UTF-8", level="ERROR")