from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Webpage:

    def __init__(self, url, browser):

        self.url = url
        self.browser = browser
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Edge':
            self.driver = webdriver.Edge()

        self.active_element = self.driver.find_element(By.NAME, '')
        print(url)
        return

    def click(self, field):
        return

    def setActiveElement(self, by_type, identifier):
        self.active_element = self.driver.find_element(by_type, identifier)
        return self.active_element

    def enterValue(self, value):
        self.active_element.send_keys(value)
        return

    def close(self):
        return

    def open(self):
        return
