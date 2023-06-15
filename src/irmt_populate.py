from lib.webpage import Webpage
from lib.file import File

wp = Webpage('https://selenium-python.readthedocs.io/getting-started.html', 'Chrome')

wp.enter_value('potato', 'q')