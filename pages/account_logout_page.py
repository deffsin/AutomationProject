import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions

from locators.home_registered_account_page_locators import HomeRegisteredAccountPageLocators
from pages.base_page import BasePage

class AccountLogoutPage(BasePage):
    def logout_button_click(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomeRegisteredAccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()