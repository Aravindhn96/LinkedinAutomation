import logging
from selenium import webdriver
import utilities.customLogger as cs
from utilities.readproperties import readconfig

class webDriverFactory():
    log = cs.customLogger(logging.DEBUG)

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        driver = None
        try:
            if self.browser.lower() == "firefox":
                driver = webdriver.Firefox()
            elif self.browser.lower() == "chrome":
                driver = webdriver.Chrome()
            elif self.browser.lower() == "ie":
                driver = webdriver.Ie()
            else:
                raise ValueError(f"Unsupported browser type: {self.browser}")
        except Exception as e:
            self.log.error(f"Failed to launch the browser: {e}")

        if driver is not None:
            self.log.info("WebDriver successfully initialized")
            driver.get('https://www.facebook.com/login/')
            driver.implicitly_wait(3)
            driver.maximize_window()
        else:
            self.log.error("WebDriver initialization failed")

        return driver


    