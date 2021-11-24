from Automated.framework.BasePage import BasePage
from Automated.pagelocator.indexLocator import indexLocator as loc

class indexObject(BasePage):

    def is_user_link_exists(self):

        try:
            self.wait_EleVisible(loc.user_link, model="用户已登录")
            return True
        
        except:
            return False