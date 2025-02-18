from selenium.webdriver.common.by import By

class HomePageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']")
    HOME_BUTTON = (By.XPATH, "//i[@class='fa fa-home']")
    LOGIN_AND_SIGNUP_BUTTON = (By.XPATH, "//a[@href='/login']")

    # If account is created, user can see these locators
    LOGGED_IN_AS_TEXT = (By.XPATH, "//a[contains(., 'Logged in as')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/delete_account']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    # After account deletion, user can see this locator
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[contains(text(), 'Account Deleted!')]")