from pages.home_page import HomePage
from pages.login_and_register_page import LoginAndSignUpPage
from pages.home_registered_account_page import HomeRegisteredAccountPage
from logging_config import logger

# User login with correct email and password
# This func is used in the different files
def login_user(driver, email, password):
    logger.info("Starting user signing in process.")
    home_page = HomePage(driver)
    login_and_signup_page = LoginAndSignUpPage(driver)
    home_registered_account_page = HomeRegisteredAccountPage(driver)

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
    assert home_registered_account_page.logged_in_as_text_visible(), "'Logged in as username' text is not visible"
