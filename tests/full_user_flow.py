import pytest
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.account_information_page import AccountInformationPage
from pages.account_created_page import AccountCreatedPage
from pages.home_registered_account_page import HomeRegisteredAccountPage
from pages.account_deleted_page import AccountDeletedPage
from pages.home_page import HomePage
from pages.login_and_signup_page import LoginAndSignUpPage

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def register_user(driver, name, email):
    home_page = HomePage(driver)
    login_and_signup_page = LoginAndSignUpPage(driver)

    home_page.open()
    home_page.accept_cookies()
    home_page.click_login_and_signup()

    assert login_and_signup_page.is_new_user_signup_text_visible(), "'New User Signup!' text is not visible"
    login_and_signup_page.fill_signup_form(name=name, email=email)
    login_and_signup_page.click_signup_button()

def complete_account_information(driver):
    account_information_page = AccountInformationPage(driver)

    assert account_information_page.is_account_information_text_visible(), "'ENTER ACCOUNT INFORMATION' text is not visible"

    account_information_page.fill_account_information(password="Wozor119")
    account_information_page.fill_address_information(
        first_name="Denis",
        last_name="Sss",
        company="HelloWorld",
        address_one="Hobujaama 2",
        address_two="Something",
        state="Harjumaa",
        city="Tallinn",
        zipcode="14512",
        mobile_number="+372555555"
    )

def delete_user_account(driver):
    account_created_page = AccountCreatedPage(driver)
    home_registered_account_page = HomeRegisteredAccountPage(driver)
    account_deleted_page = AccountDeletedPage(driver)

    assert account_created_page.account_created_text_visible(), "'ACCOUNT CREATED!' text is not visible"
    account_created_page.continue_button_click()

    assert home_registered_account_page.logged_in_as_text_visible(), "'Logged in as username' text is not visible"
    home_registered_account_page.delete_account()

    account_deleted_page.account_deleted_text_visible()
    account_deleted_page.continue_button_click()

# Main test
@pytest.mark.parametrize("name, email", [
    ("Marko", "test12313@gmail.com"),
    ("Anna", "test22131312@gmail.com")
])
def test_register_and_delete_user(driver, name, email):
    register_user(driver, name=name, email=email)
    complete_account_information(driver)
    delete_user_account(driver)
