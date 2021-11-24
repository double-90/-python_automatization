import logging
import time
from Automated.framework.GetConfig import GetConfig

class Logger():

    def __init__(self, name):

        # 创建记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)   

        # 创建处理器(输出到文件)
        logPath = GetConfig().get_Path("log_path")                            # 日志存放路径
        logDate = time.strftime("%Y%m%d%H", time.localtime(time.time()))      # 日志创建时间
        logName = logPath + logDate + ".log"                                  # 日志名称
        hand = logging.FileHandler(logName, mode="a", encoding="utf-8")         
        hand.setLevel(logging.INFO)    

        # 创建格式器（定义输出格式）
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s', '%m%d%H%M%S')
        hand.setFormatter(formatter)

        # 绑定处理器
        self.logger.addHandler(hand)

    def get_log(self):
        return self.logger

