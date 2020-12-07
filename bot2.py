from selenium import webdriver
from time import sleep
from sauce import pw

#based upon this youtube tutorial: https://www.youtube.com/watch?v=7qcQDeShXpg
#get errors for the following: aise exception_class(message, screen, stacktrace)
#selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//a[contains(text(), 'Log in')]"}
# (Session info: chrome=87.0.4280.67)

class GoBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
       

GoBot('testaccount', pw)
