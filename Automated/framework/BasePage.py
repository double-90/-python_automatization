from Automated.framework.Logger import Logger
from Automated.framework.GetConfig import GetConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 定义一个页面基类，封装一些页面操作方法
class BasePage(object):

    def __init__(self, driver):

        self.driver = driver
        self.logger = Logger(__name__).get_log()

    # 查找元素
    def find_Element(self, loc, model=None):

        self.logger.info("{0}:查找元素".format(model))

        try:
            return self.driver.find_element(*loc)

        except:
            self.logger.exception("{0}:查找元素失败".format(model))
            self.save_Img(model)
            raise
    
    # 保存截屏
    def save_Img(self, model=None):

        imgPath = GetConfig().get_Path("imgpath")                            # 图片保存路径
        imgTime = time.strftime("%m%d%H%M%S", time.localtime(time.time()))   # 图片生成时间
        imgName = imgPath + f"{model}" + imgTime + ".png"

        try:
            self.driver.save_screenshot(imgName)
            self.logger.info(f"截屏成功，保存至：{imgName}")
        except:
            self.logger.exception("截屏失败！")

    # 等待元素
    def wait_EleVisible(self, loc, timeout=20, poll_frequency=0.5, model=None):
        
        self.logger.info("{0}:等待元素出现".format(model))

        try:
            start = time.time()
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(EC.visibility_of_element_located(loc))
            end = time.time()
            self.logger.info("%s发现元素，耗时：%.2f" % (model, end-start))

        except:
            self.logger.exception("{0}:未发现元素，等待超时".format(model))
            self.save_Img(model)
            raise

    def wait_EleNoVisible(self, loc, timeout=20, poll_frequency=0.5, model=None):

        self.logger.info("{0}：等待元素不可见".format(model))

        try:
            start = time.time()
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until_not(EC.visibility_of_element_located(loc))
            end=time.time()
            self.logger.info("%s元素不可见，耗时：%.2f" % (model, end-start))

        except:
            self.logger.exception("{0}：元素仍可见，等待超时".format(model))
            self.save_Img(model)
            raise
    
    # 点击
    def click_Element(self, loc, model=None):

        ele = self.find_Element(loc, model)     # 找到元素

        self.logger.info("{0}:点击元素".format(model)) 

        try:
            ele.click()
        except:
            self.logger.exception("{0}:点击失败".format(model))
            self.save_Img(model)
            raise
    
    # 清除文本
    def clean_Text(self, loc, model=None):

        ele = self.find_Element(loc, model)

        self.logger.info("{0}:清除元素文本".format(model))

        try:
            ele.clear()
        
        except:
            self.logger.exception("{0}清除元素文本失败".format(model))
            self.save_Img(model)
            raise

    
    # 输入(输入之前清空文本)
    def input_Text(self, loc, text, model=None):
        
        ele = self.find_Element(loc, model)
        ele.clear()
        self.logger.info("{0}:输入文本内容".format(model))
        
        try:

            ele.send_keys(text)
        
        except:
            self.logger.exception("{0}:输入内容失败".format(model))
            self.save_Img(model)
            raise

    # 获得文本框内容 
    def get_Text(self, loc, model=None):

        ele = self.find_Element(loc, model)
        self.logger.info("{0}：获得元素文本".format(model))
        try:
            text = ele.text
            self.logger.info("{0}：获得文本内容({1})".format(model, text))
            return text
        
        except:
            self.logger.exception("{0}：文本内容获取失败".format(model))
            self.save_Img(model)
            raise
    

            

    