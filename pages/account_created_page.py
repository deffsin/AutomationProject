from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from locators.account_created_page_locators import AccountCreatedPageLocators
from pages.base_page import BasePage

class AccountCreatedPage(BasePage):
    def account_created_text_visible(self):
        account_created_text = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountCreatedPageLocators.ACCOUNT_CREATED_TEXT)
        )
        return account_created_text.is_displayed()

    def continue_button_click(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AccountCreatedPageLocators.CONTINUE_BUTTON)
        )
        continue_button.click()