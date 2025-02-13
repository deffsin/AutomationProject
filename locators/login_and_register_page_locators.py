from selenium.webdriver.common.by import By

class LoginAndRegisterPageLocators:
    # Login
    LOGIN_TO_YOUR_ACCOUNT_TEXT = (By.XPATH, "//h2[contains(text(), 'Login to your account')]")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_ERROR_MESSAGE_TEXT = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    # Register
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    NAME_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")