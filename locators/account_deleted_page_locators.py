from selenium.webdriver.common.by import By

class AccountDeletedPageLocators:
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[contains(text(), 'Account Deleted!')]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")