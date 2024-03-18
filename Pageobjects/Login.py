import time

from Base.selenium_webdriver import selenium_webdriver
import utilities.customLogger as cs

class test_001_Login(selenium_webdriver):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _email_id = 'email'
    _password = '//input[@id="pass"]'
    _signin_btn = '//button[contains(text(), "Log in")]'

    def clickSignInButton(self):
        self.elementClick(self._signin_btn, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email,self._email_id,locatorType="id")

    def enterPassword(self, passwrd):
        self.sendKeys(passwrd, self._password, locatorType="xpath")

    def login(self, email="", passwrd=""):
        self.enterEmail(email)
        self.enterPassword(passwrd)
        self.clickSignInButton()
        self.explicitWait(3)

    def loginSuccessfull(self):
        current_url = self.getCurrentUrl()
        if "welcome" in current_url:
            return True
        else:
            return False

    def loginUnSuccessfull(self):
        result = self.isElementPresent('//div[contains(text(), "The email address or mobile number you entered isn\'t connected to an account." )]', "XPATH")
        return result

    def clickOnHome(self):
        self.elementClick('//a[@aria-label="Home"]', "XPATH")

    def clickOnFriends(self):
        self.elementClick('//a[@aria-label="Friends"]', "XPATH")

    def clickOnGroups(self):
        self.elementClick('//a[@aria-label="Groups"]', "XPATH")

    def clickOnCreateastory(self):
        self.elementClick('//a[@aria-label="Create story"]', "XPATH")

    def clickOnCreateatextStory(self):
        self.elementClick("//div[contains(text(), 'Create a Text Story')]", "XPATH")

    def typeOnTextstory(self, data):
        self.explicitWait('//textarea[@dir = "ltr"]', "XPATH").click()
        self.explicitWait('//textarea[@placeholder = "Start typing"]', "XPATH").send_keys(data)


    def clickOnSharetostory(self):
        self.elementClick('//div[@aria-label="Share to Story"]', "XPATH")

    def checkStoryPresence(self):
        result = self.explicitWait('//a[@aria-label="View Your Story"]', "XPATH")
        if result is not None:
            return True
        else:
            return False

    def currentStory(self):
        result = self.explicitWait('//a[@aria-label="View Your Story"]', "XPATH")
        return result


    def createATextStory(self, data =""):
        self.clickOnHome()
        self.clickOnCreateastory()
        self.clickOnCreateatextStory()
        self.typeOnTextstory(data)
        self.clickOnSharetostory()

    def selectCurrentStory(self):
        self.currentStory().click()

    def pauseStory(self):
        self.elementClick('//div[@aria-label="Pause"]', "XPATH")

    def storyMenu(self):
        self.explicitWait('//div[@aria-label="Menu" and @aria-haspopup="menu"]', "XPATH").click()

    def deleteStory(self):
        self.explicitWait('(//div[@role="menuitem"])[2]', "XPATH").click()
        self.explicitWait("//span[text() = 'Delete']", "XPATH").click()

    def closeStorySection(self):
        self.elementClick('//div[@aria-label="Close"]', "XPATH")

    def mouseHoverAndClickDelete(self):
        self.mouseHoverClick('(//div[@role="menuitem"])[2]', "XPATH")
        self.explicitWait("//span[text() = 'Delete']", "XPATH").click()

    def deleteStory(self):
        self.selectCurrentStory()
        time.sleep(2)
        self.pauseStory()
        self.storyMenu()
        self.mouseHoverAndClickDelete()
        self.closeStorySection()



        
        





        



