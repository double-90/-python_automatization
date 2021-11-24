import unittest
from ddt import ddt, data
from pagedata import loginData as ld
from Automated.pageobjects.loginObject import loginObject 
from Automated.pageobjects.indexObject import indexObject 
from selenium import webdriver



@ddt
class loginCase(unittest.TestCase):

    def setUp(self) -> None:
        
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(r"E:\Project\Python\Toolbox\chromedriver.exe", chrome_options=options)
        self.driver.get(r"http://127.0.0.1:8080/ciircrm1.0/index.php?m=user&a=login")
        self.LP = loginObject(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    
    def test_login_success(self):

        self.LP.login(ld.login_success_data["user"], ld.login_success_data["passwd"])

        self.assertTrue(indexObject(self.driver).is_user_link_exists())

    @data(*ld.login_null_data)
    def test_login_null(self, data):

        self.LP.login(data["user"], data["passwd"])
        try:
            assert data["check"] in self.LP.get_errorInfo()
        except:
            raise

    @data(*ld.login_error_data)
    def test_login_error(self, data):

        self.LP.login(data["user"], data["passwd"])
        try:
            assert data["check"] in self.LP.get_errorInfo()
        except:
            raise
    

if __name__ == "__main__":

    unittest.main()

