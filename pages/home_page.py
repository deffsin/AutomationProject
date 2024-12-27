from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    PAGE_URL = "https://www.automationexercise.com/"

    def accept_cookies(self):
        accept_cookies_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        )
        accept_cookies_button.click()

    def click_login_and_signup(self):
        login_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.LOGIN_AND_SIGNUP_BUTTON)
        )
        login_button.click()