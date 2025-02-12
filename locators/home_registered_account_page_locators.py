from selenium.webdriver.common.by import By

class HomeRegisteredAccountPageLocators:
    LOGGED_IN_AS_TEXT = (By.XPATH, "//a[contains(., 'Logged in as')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/delete_account']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")