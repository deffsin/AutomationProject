from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions

from locators.login_and_register_page_locators import LoginAndRegisterPageLocators
from pages.base_page import BasePage

class LoginAndRegisterPage(BasePage):

    # Login
    def is_login_to_your_account_visible(self):
        login_to_your_account = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LoginAndRegisterPageLocators.LOGIN_TO_YOUR_ACCOUNT_TEXT)
        )
        return login_to_your_account.is_displayed()

    def fill_login_form(self, email, password):
        email_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndRegisterPageLocators.LOGIN_EMAIL_FIELD)
        )
        email_field.send_keys(email)

        password_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndRegisterPageLocators.LOGIN_PASSWORD_FIELD)
        )
        password_field.send_keys(password)

    def login_error_text_visible(self):
        login_error_text = WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.visibility_of_element_located(LoginAndRegisterPageLocators.LOGIN_ERROR_MESSAGE_TEXT)
        )
        return login_error_text.is_displayed()

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located(LoginAndRegisterPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

    # Register
    def is_new_user_signup_text_visible(self):
        new_user_signup = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LoginAndRegisterPageLocators.NEW_USER_SIGNUP_TEXT)
        )
        return new_user_signup.is_displayed()

    def fill_signup_form(self, name, email):
        name_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndRegisterPageLocators.NAME_FIELD)
        )
        name_field.send_keys(name)

        email_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndRegisterPageLocators.EMAIL_FIELD)
        )
        email_field.send_keys(email)

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(LoginAndRegisterPageLocators.SIGNUP_BUTTON)
        )
        signup_button.click()