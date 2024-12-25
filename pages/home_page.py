from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.automationexercise.com/"

    def open(self):
        self.driver.get(self.url)

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

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()
        # home_page.click_login_and_signup()
    finally:
        driver.quit()
