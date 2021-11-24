from Automated.framework.BasePage import BasePage
from Automated.pagelocator.loginLocator import loginLocator as loc

class loginObject(BasePage):

    def login(self, username, passwd):

        self.wait_EleVisible(loc.user_input, model="等待用户输入框")

        self.clean_Text(loc.user_input, model="清除用户框文本")

        self.input_Text(loc.user_input, text=username, model="输入用户名")

        self.wait_EleVisible(loc.passwd_input, model="等待密码输入框")

        self.clean_Text(loc.passwd_input, model="清除密码框文本")

        self.input_Text(loc.passwd_input, text=passwd, model="输入密码")

        self.click_Element(loc.submit_button, model="登录")

    
    def get_errorInfo(self):

        self.wait_EleVisible(loc.error_info, model="等待错误提示框")
        return self.get_Text(loc.error_info, model="获取错误提示框内容")