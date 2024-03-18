import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import utilities.customLogger as cl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
class selenium_webdriver():

    log = cl.customLogger(loglevel=logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getByType(self, locatorType = "id"):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.CLASS_NAME
        elif locatorType =="xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.error("Provided locatorType"+locatorType+"is not correct")
        return False

    def getElement(self,locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found")
        except:
            self.log.error("Element Not Found")
        return element

    def elementClick(self,locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator"+locator+"locator Type"+locatorType)
        except:
            self.log.error("Cannot click on element with locator"+locator+"locator Type"+locatorType)

    def sendKeys(self,data , locator, locatorType="id" ):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("send keys on element with locator"+locator+" locator Type "+locatorType)
        except:
            self.log.error("cannot send keys on element with locator"+locator+"locator Type"+locatorType)

    def explicitWait(self, locator, locatorType = "id", timeout = 10, pollfrequency = 0.5):
        element = None
        try:
            byType =self.getByType(locatorType)
            self.log.info("waiting for maximum"+str(timeout)+"until the element to be clickable")

            wait = WebDriverWait(self.driver, timeout,pollfrequency, ignored_exceptions= [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element Appeared on webpage")

        except:
            self.log.error("Element not appeared on webpage")

        return element

    def getCurrentUrl(self):
        result = self.driver.current_url
        return result
        

    def isElementPresent(self,locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element is Present")
                return True
            else:
                self.log.error("Element is not Present")
                return False
        except:
            self.log.error("Element is not Present")
            return False

    def mouseHoverClick(self,locator, locatorType):
        element = None
        try:
            actions = ActionChains(self.driver)
            element = self.getElement(locator, locatorType)
            actions.move_to_element(element).click().perform()
            self.log.info("Mouse hovered and click successfully with"+ locator + 'and' + locatorType)

        except:
            self.log.error("cannot hover mouse and click with"+ locator + 'and' + locatorType)
            
        return element












        


