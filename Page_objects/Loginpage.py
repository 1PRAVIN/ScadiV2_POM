from selenium import webdriver
from selenium.webdriver import ActionChains


class LoginPage:

    Login_userid_text = "//input[@formcontrolname ='username']"
    Login_userpass_text = "//input[@id='userPass']"
    Login_button = "//button[@type='submit']"
    Logout_hyperlink = "//a[@title='Log Out']"
    Validation_message = "//div[@class='ui-toast-detail']"
    val_msg = ""

    def __init__(self, driver):
        self.driver = driver

    def username(self, userid):
        source = self.driver.find_element("xpath", self.Login_userid_text)
        action = ActionChains(self.driver)
        action.double_click(source).perform()
        self.driver.find_element("xpath", self.Login_userid_text).clear()
        self.driver.find_element("xpath", self.Login_userid_text).send_keys(userid)

    def userpass(self, password):
        source = self.driver.find_element("xpath", self.Login_userpass_text)
        action = ActionChains(self.driver)
        action.double_click(source).perform()
        self.driver.find_element("xpath", self.Login_userpass_text).clear()
        self.driver.find_element("xpath", self.Login_userpass_text).send_keys(password)

    def loginclick(self):
        self.driver.find_element("xpath", self.Login_button).click()

    def validation_msg(self):
        self.val_msg = self.driver.find_element("xpath", self.Validation_message).text
        return self.val_msg

    def logout(self):
        action = ActionChains(self.driver)
        action.double_click(self.driver.find_element("xpath", self.Logout_hyperlink)).perform()











