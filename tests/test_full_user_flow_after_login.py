import pytest
from pages.home_registered_account_page import HomeRegisteredAccountPage
from pages.account_deleted_page import AccountDeletedPage
from helpers.auth import login_user
from logging_config import logger

@pytest.mark.usefixtures("driver")
class TestFullUserFlowAfterLogin:
    def delete_user_account(self):
        logger.info("Starting account deletion process.")
        home_registered_account_page = HomeRegisteredAccountPage(self.driver)
        account_deleted_page = AccountDeletedPage(self.driver)

        logger.info("Clicking the 'Delete Account' button.")
        home_registered_account_page.delete_account()

        logger.info("Verifying 'ACCOUNT DELETED!' text is visible.")
        account_deleted_page.account_deleted_text_visible()

    @pytest.mark.parametrize("email, password", [
        ("helloworld228@gmail.com", "Wozor119"),
        ("worldhello119@gmail.com", "Wozor119")
    ])
    def test_user_login_and_delete_user(self, email, password):
        logger.info(f"Starting test case for user.")
        login_user(self.driver, email, password)
        logger.info(f"Starting user account deletion process")
        self.delete_user_account()
        logger.info("User account deletion completed successfully.")