
class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//input[@class='button-1login-button']"
    link_logout_linktext="Logout"

    def __int__(self,driver):
        self.driver=driver
    def setUserName(self,username):
        self.driver.find_element_by_id(self.testbox_username_id).clear()
        self.driver.find_element_by_id(self.testbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.testbox_password_id).clear()
        self.driver.find_element_by_id(self.testbox_passward_id).send_keys(password)
    def clickLogin(self):
            self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
            self.driver.find_element_by_link_text(self.link_logout_linktext).click()