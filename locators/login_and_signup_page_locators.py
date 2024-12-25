from selenium.webdriver.common.by import By

class LoginAndSignUpPageLocators:
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    NAME_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")