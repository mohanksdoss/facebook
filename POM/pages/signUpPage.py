from selenium.webdriver.common.by import By

from POM import Locators


class signUp:
    def __init__(self,driver):
        self.first_name = driver.find_element(By.NAME,Locators.text_firstName)
        self.sur_name = driver.find_element(By.NAME,Locators.text_surName)
        self.mobile_num = driver.find_element(By.XPATH,Locators.mobile_num_xpath)

    def getFirstName(self):
        return self.first_name
    def getSurName(self):
        return self.sur_name
    def getMobileNum(self):
        return self.mobile_num