from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://facebook.com")

    def test_Login(self):
        """Function verifies the login successful or not
        @self : Object
        """

        driver = self.driver
        facebook_username = eval(input("\nEnter Your FaceBook Username:"))
        facebook_password = eval(input("\nEnter Your FaceBook Password:"))
        emailFieldId = "email"
        pwdFieldId = "pass"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoPath = "(//a[contains(@href,'logo')])[1]"

        emailFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(emailFieldId)
        )
        passwordFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(pwdFieldId)
        )
        loginButtonElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(loginButtonXpath)
        )

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebook_username)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(facebook_password)
        loginButtonElement.click()

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(fbLogoPath)
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
