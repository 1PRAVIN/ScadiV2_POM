import time
import pytest
from selenium import webdriver
from Page_objects.Loginpage import LoginPage


class Test_login:

    correct_userid = 63516
    correct_user_password = "Ecom@222"
    wrong_userid = 123
    wrong_user_password = "Ecom@000"

    def test_wrongid_wrongpassword(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.username(self.wrong_userid)
        time.sleep(2)
        self.lp.userpass(self.wrong_user_password)
        time.sleep(2)
        self.lp.loginclick()
        time.sleep(2)
        val_msg = self.lp.validation_msg()
        self.driver.save_screenshot(".//Screenshots//"+"Pass_test_wrongid_wrongpassword.png")
        print("\n Validation message on login - " + val_msg)
        self.driver.close()

    def test_correctid_correctpassword(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.username(self.correct_userid)
        time.sleep(2)
        self.lp.userpass(self.correct_user_password)
        time.sleep(2)
        self.lp.loginclick()
        if self.correct_userid == int(self.driver.find_element("xpath", "//span[@class='customer_code ng-star-inserted']").text.strip("()")):
            self.driver.save_screenshot(".//Screenshots//"+"Pass_test_correctid_correctpassword.png")
            self.lp.logout()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"Fail_test_correctid_correctpassword.png")
            self.lp.logout()

        self.driver.close()









