from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\DHilan\PycharmProjects\PythonTesting\drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
get = driver.title
print(get)