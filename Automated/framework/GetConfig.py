from configparser import ConfigParser


class GetConfig():

    def __init__(self):

        self.config = ConfigParser()     # 类实例化
        self.path = r"E:\python_jenkins\workspace\python_project001\Automated\config\config.ini"   # 配置文件路径
        self.config.read(self.path)      # 读取配置文件


    def get_Path(self, key, section="filePath"):      # 读取路径

        return self.config.get(section, key)

        # 例如 GetConfig().get_path("log_path")  可获取到存放log的路径
