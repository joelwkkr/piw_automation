from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions



class Webpage:

    def __init__(self, browser_name):

        self.browser_name = browser_name.lower()
        if self.browser_name == 'chrome':
            self.browser = webdriver.Chrome()
        elif self.browser_name == 'edge':
            self.browser = webdriver.Edge()
        elif self.browser_name = 'firefox':
            self.browser = webdriver.Firefox()

        self.active_element = ''
        return

    def openUrl(self, url):
        self.browser.get(url)
        return

    def connectToExistingSession(self):
        return

    def click(self, field):
        return

    def setActiveElement(self, by_type, identifier):
        self.active_element = self.browser.find_element(by_type, identifier)
        return self.active_element

    def enterValue(self, value):
        self.active_element.send_keys(value)
        return

    def close(self):
        return

    def open(self):
        return
