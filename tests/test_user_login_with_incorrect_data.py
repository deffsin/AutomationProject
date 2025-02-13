import pytest

from pages.home_page import HomePage
from pages.login_and_register_page import LoginAndRegisterPage

from logging_config import logger

# This is Test Case 3: Login User with incorrect email and password
@pytest.mark.usefixtures("driver")
class TestUserLoginWithIncorrectData:
    def login_user_with_incorrect_data(self, email, password):
        logger.info("Starting user signing in process with incorrect email and password.")
        home_page = HomePage(self.driver)
        login_and_signup_page = LoginAndRegisterPage(self.driver)

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

        logger.info("Verifying the presence of 'Your email or password is incorrect' text.")
        login_and_signup_page.login_error_text_visible()
        assert login_and_signup_page.login_error_text_visible(), "'Your email or password is incorrect' text is not visible"

    @pytest.mark.parametrize("email, password", [
        ("redmorrelo@gmail.com", "Wozor119s"),
        ("testtestik228119@gmail.com", "Wozor119s")
    ])
    def test_user_login_with_incorrect_data(self, email, password):
        logger.info(f"Starting test case for user.")
        self.login_user_with_incorrect_data(email=email, password=password)