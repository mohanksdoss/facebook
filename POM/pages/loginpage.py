from selenium.webdriver.common.by import By

from POM import Locators


class LoginPage:
    def __init__(self, driver):
        self.userName = driver.find_element(By.ID, Locators.UserName_ID)
        self.password = driver.find_element(By.ID, Locators.PassWord_ID)
        self.login_btn = driver.find_element(By.ID, Locators.btn_login_ID)
        self.create_new = driver.find_element(By.ID, Locators.btn_create_new)


    def getuserName(self):
        return self.userName
    def getpassword(self):
        return self.password
    def getlogin(self):
        return self.login_btn
    def getcreateNew(self):
        return self.create_new

