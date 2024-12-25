import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.account_information_page import AccountInformationPage
from pages.home_page import HomePage
from pages.login_and_signup_page import LoginAndSignUpPage


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


def test_signup(driver):
    name = "Nameee"
    email = "testuser228119@example.com"

    home_page = HomePage(driver)
    login_and_signup_page = LoginAndSignUpPage(driver)
    account_information_page = AccountInformationPage(driver)

    home_page.open()
    home_page.accept_cookies()
    home_page.click_login_and_signup()

    # Text verification
    assert login_and_signup_page.is_new_user_signup_text_visible(), "Text 'New User Signup!' is not visible"

    login_and_signup_page.fill_signup_form(name=name, email=email)
    login_and_signup_page.click_signup_button()

    assert account_information_page.is_account_information_text_visible(), "Text 'ENTER ACCOUNT INFORMATION' is not visible"
