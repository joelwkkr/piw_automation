from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas
import sys


class Webpage:

    def __init__(self, browser_name):

        self.browser_name = browser_name.lower()
        if self.browser_name == 'chrome':
            self.browser = webdriver.Chrome()
        elif self.browser_name == 'edge':
            self.browser = webdriver.Edge()
        elif self.browser_name == 'firefox':
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


class File:

    def __init__(self, path, file_type):
        self.path = path
        self.file_type = file_type.lower()
        self.sheet = ''
        self.book = ''
        return

    def open(self):
        if self.file_type == 'excel':
            self.book = pandas.ExcelFile(self.path)
            self.sheet = pandas.read_excel(self.book, usecols='c,h', header=4, names=['ID', 'Text'], index_col=0)
        elif self.file_type == 'csv':
            self.book = pandas.read_csv(self.path, header=0)
            self.sheet = pandas.DataFrame.read_csv(self.path, header=0)
        return

    def getRow(self, id):
        return


if __name__ == "__main__":

    template = sys.argv[1]

    f = File(template, 'excel')
    f.open()

    print(f.sheet)

    entries = f.sheet['Text']
    print(entries.get(1.10))

    print(f.sheet['Text'][1.10])

    wp = Webpage('Edge')
    wp.openUrl('https://selenium-python.readthedocs.io/getting-started.html')

    wp.setActiveElement(By.NAME, 'q').send_keys('potato')

    wp.browser

    while not wp.browser.title.startswith('Search'):
        continue
