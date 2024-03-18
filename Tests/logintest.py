from Pageobjects.Login import test_001_Login
from utilities.readproperties import readconfig
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class TestLoginTests:
    @pytest.fixture(autouse=True)
    def setUp(self, oneTimeSetUp):
        self.lp = test_001_Login(self.driver)
        #self.username = readconfig.getUserEmail()
        #self.password = readconfig.getpassword()
        self.username = 'dunebank@gmail.com'
        self.password = 'Test@1234'

    def test01_invalid_login(self):
        self.lp.login(self.password)
        result = self.lp.loginUnSuccessfull()
        assert result == True
    def test02_login_validation(self):
        self.lp.login(self.username, self.password)
        result = self.lp.loginSuccessfull()
        assert result == True

    def test03_home_section(self):
        self.lp.clickOnHome()
        result = self.lp.getCurrentUrl()
        assert "https://www.facebook.com/" in result

    def test04_friends_section(self):
        self.lp.clickOnFriends()
        friend_section = self.lp.getCurrentUrl()
        assert "https://www.facebook.com/friends" in friend_section

    def test05_group_section(self):
        self.lp.clickOnGroups()
        group_section = self.lp.getCurrentUrl()
        assert "https://www.facebook.com/groups/feed/" in group_section

    def test06_create_a_text_story(self):
        self.lp.createATextStory("Test")
        result = self.lp.checkStoryPresence()
        assert result == True

    def test07_delete_story(self):
        self.lp.deleteStory()
        result = self.lp.checkStoryPresence()
        assert result == False









