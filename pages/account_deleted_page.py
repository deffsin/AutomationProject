from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from locators.account_deleted_page_locators import AccountDeletedPageLocators
from pages.base_page import BasePage

class AccountDeletedPage(BasePage):
    def account_deleted_text_visible(self):
        account_deleted_text = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountDeletedPageLocators.ACCOUNT_DELETED_TEXT)
        )
        return account_deleted_text.is_displayed()

    def continue_button_click(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AccountDeletedPageLocators.CONTINUE_BUTTON)
        )
        continue_button.click()