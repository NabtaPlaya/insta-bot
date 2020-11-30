from selenium import webdriver
from time import sleep
from sauce import pw

class GoBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
       

GoBot('testaccount', pw)
