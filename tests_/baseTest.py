import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.events import EventFiringWebDriver

from common_.utilities_.customListener import CustomListener


class BaseTest(unittest.TestCase):
    """
        This class serves as the base for Selenium test cases, providing common setup and tear down procedures.
    """
    def setUp(self):

            # Options for run browser in headless mode
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")  # Disable sandbox mode
        self.simpleDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

        # self.simpleDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = EventFiringWebDriver(self.simpleDriver, CustomListener(self.simpleDriver))
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.onlyoffice.com/")

    def tearDown(self):
        self.driver.close()
