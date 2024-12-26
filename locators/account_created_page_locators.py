from selenium.webdriver.common.by import By

class AccountCreatedPageLocators:
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[contains(text(), 'Account Created')]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")