from selenium.webdriver.common.by import By

class AddAccountInformationPageLocators:
    # ENTER ACCOUNT INFORMATION
    ENTER_ACCOUNT_INFORMATION_TEXT = (By.XPATH, "//b[contains(text(), 'Enter Account Information')]")

    FIRST_TITLE_RADIO_BUTTON = (By.ID, "id_gender1") # Mr
    SECOND_TITLE_RADIO_BUTTON = (By.ID, "id_gender2") # Mrs
    PASSWORD_INPUT = (By.ID, "password")

    # Date of birth
    DAYS_DROPDOWN = (By.ID, "days")
    MONTHS_DROPDOWN = (By.ID, "months")
    YEARS_DROPDOWN = (By.ID, "years")

    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")

    # ADDRESS INFORMATION
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS_ONE_INPUT = (By.ID, "address1")
    ADDRESS_TWO_INPUT = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = By.ID, "mobile_number"
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-qa='create-account']")
