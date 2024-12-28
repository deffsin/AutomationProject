from selenium.webdriver.common.by import By

class HomePageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']")
    HOME_BUTTON = (By.XPATH, "//i[@class='fa fa-home']")
    LOGIN_AND_SIGNUP_BUTTON = (By.XPATH, "//a[@href='/login']")