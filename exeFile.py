import time

from POM.pages.loginpage import LoginPage
from POM.pages.signUpPage import signUp
from base.Base import base


class Exe(base):
    def login(self):
        driver = self.get_browser()
        self.get_url("https://www.facebook.com/")
        print(self.get_title())
        login_page = LoginPage(driver)
        self.text(login_page.getuserName(),"mohan")
        self.text(login_page.getpassword(),"doss")
        self.btn_click(login_page.getlogin())
        self.end()


    def reg(self):
        driver = self.get_browser()
        self.get_url("https://www.facebook.com/")
        login_page = LoginPage(driver)
        self.btn_click(login_page.getcreateNew())
        time.sleep(5)
        signUp_page = signUp(driver)
        self.text(signUp_page.getFirstName(),"mohan")



e = Exe()
e.login()
e.reg()
