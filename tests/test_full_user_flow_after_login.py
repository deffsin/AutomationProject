import pytest

from pages.home_registered_account_page import HomeRegisteredAccountPage
from pages.account_deleted_page import AccountDeletedPage
from pages.home_page import HomePage
from pages.login_and_signup_page import LoginAndSignUpPage

from logging_config import logger

# This is Test Case 2: Login User with correct email and password
@pytest.mark.usefixtures("driver")
class TestFullUserFlowAfterLogin:
    def login_user(self, email, password):
        logger.info("Starting user signing in process.")
        home_page = HomePage(self.driver)
        login_and_signup_page = LoginAndSignUpPage(self.driver)
        home_registered_account_page = HomeRegisteredAccountPage(self.driver)

        logger.info("Opening the home page")
        home_page.open()
        logger.info("Accepting cookies on the home page.")
        home_page.accept_cookies()
        logger.info("Checking visibility of home page")
        assert home_page.is_home_page_visible(), "'Home page' is not visible"

        logger.info("Navigating to the login and signup page.")
        home_page.click_login_and_signup()
        logger.info("Verifying the presence of 'Login to your account' text.")
        assert login_and_signup_page.is_login_to_your_account_visible(), "'Login to your account!' text is not visible"
        logger.info("Filling out the login form")
        login_and_signup_page.fill_login_form(email=email, password=password)
        logger.info(f"Clicking the login button for user with email: {email} and password: {password}.")
        login_and_signup_page.click_login_button()

        logger.info("Verifying the presence of 'Logged in as username' text.")
        assert home_registered_account_page.logged_in_as_text_visible() , "'Logged in as username' text is not visible"

    def delete_user_account(self):
        logger.info("Starting account deletion process.")
        home_registered_account_page = HomeRegisteredAccountPage(self.driver)
        account_deleted_page = AccountDeletedPage(self.driver)

        logger.info("Clicking the 'Delete Account' button.")
        home_registered_account_page.delete_account()

        logger.info("Verifying 'ACCOUNT DELETED!' text is visible.")
        account_deleted_page.account_deleted_text_visible()

    @pytest.mark.parametrize("email, password", [
        ("redmorrelo@gmail.com", "Wozor119"),
        ("testwzcg2211wqw312@gmail.com", "Wozor119")
    ])
    def test_user_login_and_delete_user(self, email, password):
        logger.info(f"Starting test case for user.")
        self.login_user(email=email, password=password)
        logger.info(f"Starting user account deletion process")
        self.delete_user_account()
        logger.info("User account deletion completed successfully.")