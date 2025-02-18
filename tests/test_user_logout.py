import pytest
from pages.home_page import HomePage
from helpers.auth import login_user
from logging_config import logger

@pytest.mark.usefixtures("driver")
class TestFullUserFlowAfterLogin:
    def user_logout(self):
        logger.info("Initiating user logout process.")
        account_logout_page = HomePage(self.driver)

        logger.info("Clicking on the 'Logout' button.")
        account_logout_page.logout_button_click()

        logger.info("User successfully logged out.")

    @pytest.mark.parametrize("email, password", [
        ("helloworldd2281@gmail.com", "Wozor119"),
        ("worldhelloo1191@gmail.com", "Wozor119")
    ])
    def test_user_login_and_delete_user(self, email, password):
        logger.info(f"Starting test case for user with email: {email}.")

        logger.info("Attempting to log in.")
        login_user(self.driver, email, password)
        logger.info(f"User {email} successfully logged in.")

        logger.info("Proceeding to log out.")
        self.user_logout()
        logger.info(f"User {email} successfully logged out. Test case completed.")