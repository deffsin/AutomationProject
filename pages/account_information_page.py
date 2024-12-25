from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.account_information_page_locators import AccountInformationPageLocators

import time

class AccountInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.automationexercise.com/signup"

    def open(self):
        self.driver.get(self.url)

    # Potom Delete
    def accept_cookies(self):
        accept_cookies_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(HomePageLocators.ACCEPT_COOKIES_BUTTON)
        )
        accept_cookies_button.click()

    def is_account_information_text_visible(self):
        account_information_visible = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.ENTER_ACCOUNT_INFORMATION_TEXT)
        )
        return account_information_visible.is_displayed()

# if __name__ == "__main__":
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#     try:
#         account_information_page = AccountInformationPage(driver)
#         account_information_page.open()
#         account_information_page.accept_cookies()
#         account_information_page.is_account_information_visible()
#         time.sleep(3)
#
#     finally:
#         driver.quit()
