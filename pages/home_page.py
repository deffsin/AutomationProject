from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions

from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    PAGE_URL = "https://www.automationexercise.com/"

    def accept_cookies(self):
        accept_cookies_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        )
        accept_cookies_button.click()

    def is_home_page_visible(self):
        home_page_visible = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.HOME_BUTTON)
        )
        return home_page_visible.is_displayed()

    def click_login_and_signup(self):
        login_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.LOGIN_AND_SIGNUP_BUTTON)
        )
        login_button.click()

    # After signing in account
    def logout_button_click(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

    def logged_in_as_text_visible(self):
        logged_in_as_username = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.LOGGED_IN_AS_TEXT)
        )
        return logged_in_as_username.is_displayed()

    def delete_account(self):
        delete_account_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.DELETE_ACCOUNT_BUTTON)
        )
        delete_account_button.click()

    # After account deletion
    def account_deleted_text_visible(self):
        account_deleted_text = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.ACCOUNT_DELETED_TEXT)
        )
        return account_deleted_text.is_displayed()

    def continue_button_click(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(BasePageLocators.CONTINUE_BUTTON)
        )
        continue_button.click()