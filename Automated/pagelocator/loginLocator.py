from selenium.webdriver.common.by import By

class loginLocator():

    user_input = (By.XPATH, r"/html/body/div[2]/div/div[2]/div/form/fieldset/input[1]")

    passwd_input = (By.XPATH, r"/html/body/div[2]/div/div[2]/div/form/fieldset/input[2]")

    submit_button = (By.XPATH, r"/html/body/div[2]/div/div[2]/div/form/fieldset/input[3]")

    error_info = (By.XPATH, r"/html/body/div[2]/div/div[2]/div/form/fieldset/div")

    