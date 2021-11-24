from selenium.webdriver.common.by import By
from Automated.framework.BasePage import BasePage
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(r"E:\Project\Python\Toolbox\chromedriver.exe", chrome_options=options)
driver.get(r"http://127.0.0.1:8080/ciircrm1.0/index.php?m=user&a=login")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/fieldset/input[1]").send_keys('admin')

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/fieldset/input[3]").click()

ele = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/fieldset/div').text

print(ele)

chr = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/fieldset/div/button").text

str1= ele.replace(chr, '')

print(str1)



