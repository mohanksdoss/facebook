from selenium import webdriver


class base:
    def get_browser(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\DHilan\PycharmProjects\PythonTesting\drivers\chromedriver.exe")
        self.driver.maximize_window()
        return self.driver

    def get_url(self, url):
        self.driver.get(url)

    def text(self, element, value):
        element.send_keys(value)

    def btn_click(self, element):
        element.click()

    def get_title(self):
        page_title = self.driver.title
        return page_title

    def end(self):
        self.driver.quit()
