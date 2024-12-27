from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.login_and_signup_page_locators import LoginAndSignUpPageLocators
from pages.base_page import BasePage

import time

class LoginAndSignUpPage(BasePage):
    # Potom Delete
    def accept_cookies(self):
        accept_cookies_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        )
        accept_cookies_button.click()

    def is_new_user_signup_text_visible(self):
        new_user_signup = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LoginAndSignUpPageLocators.NEW_USER_SIGNUP_TEXT)
        )
        return new_user_signup.is_displayed()


    def fill_signup_form(self, name, email):
        name_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndSignUpPageLocators.NAME_FIELD)
        )
        name_field.send_keys(name)

        email_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndSignUpPageLocators.EMAIL_FIELD)
        )
        email_field.send_keys(email)

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndSignUpPageLocators.SIGNUP_BUTTON)
        )
        signup_button.click()

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        login_and_signup_page = LoginAndSignUpPage(driver)
        login_and_signup_page.open()
        login_and_signup_page.accept_cookies()
        login_and_signup_page.is_new_user_signup_text_visible()
        login_and_signup_page.fill_signup_form(name="Name", email="emfsdfsfsail@gmail.com")
        login_and_signup_page.click_signup_button()
        time.sleep(2)

    finally:
        driver.quit()
