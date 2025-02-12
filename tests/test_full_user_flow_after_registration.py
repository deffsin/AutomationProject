import pytest

from pages.account_information_page import AccountInformationPage
from pages.account_created_page import AccountCreatedPage
from pages.home_registered_account_page import HomeRegisteredAccountPage
from pages.account_deleted_page import AccountDeletedPage
from pages.home_page import HomePage
from pages.login_and_signup_page import LoginAndSignUpPage

from logging_config import logger

# This is Test Case 1: Register User
@pytest.mark.usefixtures("driver")
class TestFullUserFlowAfterRegistration:
    def register_user(self, name, email):
        logger.info("Starting user registration process.")
        home_page = HomePage(self.driver)
        login_and_signup_page = LoginAndSignUpPage(self.driver)

        logger.info("Opening the home page.")
        home_page.open()
        logger.info("Accepting cookies on the home page.")
        home_page.accept_cookies()
        logger.info("Navigating to the login and signup page.")
        home_page.click_login_and_signup()

        logger.info("Verifying the presence of 'New User Signup!' text.")
        assert login_and_signup_page.is_new_user_signup_text_visible(), "'New User Signup!' text is not visible"
        logger.info("Filling out the signup form.")
        login_and_signup_page.fill_signup_form(name=name, email=email)
        logger.info(f"Clicking the signup button for user: {name} with email: {email}.")
        login_and_signup_page.click_signup_button()

    def complete_account_information(self):
        logger.info("Completing account information process.")
        account_information_page = AccountInformationPage(self.driver)

        logger.info("Verifying the presence of 'ENTER ACCOUNT INFORMATION' text.")
        assert account_information_page.is_account_information_text_visible(), "'ENTER ACCOUNT INFORMATION' text is not visible"

        logger.info("Filling in account information and address details.")
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

    def delete_user_account(self):
        logger.info("Starting account deletion process.")
        account_created_page = AccountCreatedPage(self.driver)
        home_registered_account_page = HomeRegisteredAccountPage(self.driver)
        account_deleted_page = AccountDeletedPage(self.driver)

        logger.info("Verifying 'ACCOUNT CREATED!' text is visible.")
        assert account_created_page.account_created_text_visible(), "'ACCOUNT CREATED!' text is not visible"
        logger.info("Clicking the 'Continue' button after account creation.")
        account_created_page.continue_button_click()

        logger.info("Verifying user is logged in as their username.")
        assert home_registered_account_page.logged_in_as_text_visible(), "'Logged in as username' text is not visible"
        logger.info("Clicking the 'Delete Account' button.")
        home_registered_account_page.delete_account()

        logger.info("Verifying 'ACCOUNT DELETED!' text is visible.")
        account_deleted_page.account_deleted_text_visible()
        logger.info("Clicking the 'Continue' button after account deletion.")
        account_deleted_page.continue_button_click()

    # Main test
    @pytest.mark.parametrize("name, email", [
        ("Marko", "helloworld228@gmail.com"),
        ("Anna", "worldhello119@gmail.com")
    ])
    def test_register_and_delete_user(self, name, email):
        logger.info(f"Starting test case for user: {name} with email: {email}.")
        self.register_user(name=name, email=email)
        logger.info("User registration completed successfully.")
        self.complete_account_information()
        logger.info("Account information completed successfully.")
        self.delete_user_account()
        logger.info("User account deletion completed successfully.")
