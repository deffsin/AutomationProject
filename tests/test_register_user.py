import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_and_signup_page import LoginAndSignUpPage
from locators.login_and_signup_page_locators import LoginAndSignUpPageLocators


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_signup(driver):
    name = "Name"
    email = "qedjqwn@gmail.com"
    home_page = HomePage(driver)
    login_and_signup_page = LoginAndSignUpPage(driver)

    home_page.open()
    home_page.accept_cookies()
    home_page.click_login_and_signup()
    assert login_and_signup_page.is_new_user_signup_visible(), "Text 'New User Signup!' in not displayed"
    login_and_signup_page.fill_signup_form(name=name, email=email)
    login_and_signup_page.click_signup_button()
