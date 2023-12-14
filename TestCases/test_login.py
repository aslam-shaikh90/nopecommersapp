import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import Utilities.readProperties
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Utilities.ReadConfig.getApplicaioinURL()
    username = Utilities.ReadConfig.getUseremail()
    password = Utilities.ReadConfig.getpassward()

    def text_homePageTitel(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            self.driver.save.screenshot(".\\Screenshot\\"+"text_homePageTitel.png")
            self.driver.close()
            assert False
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save.screenshot(".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            assert False
