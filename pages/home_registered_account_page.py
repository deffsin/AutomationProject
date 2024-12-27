from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from locators.home_registered_account_page_locators import HomeRegisteredAccountPageLocators
from pages.base_page import BasePage

class HomeRegisteredAccountPage(BasePage):
    def logged_in_as_text_visible(self):
        logged_in_as_username = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(HomeRegisteredAccountPageLocators.LOGGED_IN_AS_TEXT)
        )
        return logged_in_as_username.is_displayed()

    def delete_account(self):
        delete_account_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomeRegisteredAccountPageLocators.DELETE_ACCOUNT_BUTTON)
        )
        delete_account_button.click()
