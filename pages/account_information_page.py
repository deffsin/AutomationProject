from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.support.ui import Select
from locators.account_information_page_locators import AccountInformationPageLocators
from pages.base_page import BasePage

class AccountInformationPage(BasePage):
    def is_account_information_text_visible(self):
        account_information_visible = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.ENTER_ACCOUNT_INFORMATION_TEXT)
        )
        return account_information_visible.is_displayed()

    def fill_account_information(self, password):
        title_radio_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AccountInformationPageLocators.FIRST_TITLE_RADIO_BUTTON)
        )
        title_radio_button.click()

        assert title_radio_button.is_selected(), "Title radio button is not selected"


        password_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.PASSWORD_INPUT)
        )
        password_input.send_keys(password)

        self.choosing_date_of_birth()

        self.newsletter_and_special_offers_checkboxes()

    # Date of birth
    def choosing_date_of_birth(self):
        # Days dropdown
        day_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(AccountInformationPageLocators.DAYS_DROPDOWN)
        )
        select = Select(day_dropdown)
        select.select_by_index(3)

        # Months dropdown
        month_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(AccountInformationPageLocators.MONTHS_DROPDOWN)
        )
        select = Select(month_dropdown)
        select.select_by_index(5)

        # Years dropdown
        year_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(AccountInformationPageLocators.YEARS_DROPDOWN)
        )
        select = Select(year_dropdown)
        select.select_by_value("1999")

    def newsletter_and_special_offers_checkboxes(self):
        newsletter_checkbox = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AccountInformationPageLocators.NEWSLETTER_CHECKBOX)
        )
        newsletter_checkbox.click()
        assert newsletter_checkbox.is_selected(), "Newsletter checkbox is not selected"

        special_offers_checkbox = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AccountInformationPageLocators.SPECIAL_OFFERS_CHECKBOX)
        )
        special_offers_checkbox.click()
        assert special_offers_checkbox.is_selected(), "Newsletter checkbox is not selected"

    def fill_address_information(self, first_name: object, last_name: object, company: object, address_one: object, address_two: object, state: object, city: object, zipcode: object, mobile_number: object) -> object:
        first_name_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.FIRST_NAME_INPUT)
        )
        first_name_input.send_keys(first_name)

        last_name_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.LAST_NAME_INPUT)
        )
        last_name_input.send_keys(last_name)

        company_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.COMPANY_INPUT)
        )
        company_input.send_keys(company)

        address_one_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.ADDRESS_ONE_INPUT)
        )
        address_one_input.send_keys(address_one)

        address_two_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.ADDRESS_TWO_INPUT)
        )
        address_two_input.send_keys(address_two)

        country_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(AccountInformationPageLocators.COUNTRY_DROPDOWN)
        )
        select = Select(country_dropdown)
        select.select_by_index(4)

        state_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.STATE_INPUT)
        )
        state_input.send_keys(state)

        city_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.CITY_INPUT)
        )
        city_input.send_keys(city)

        zipcode_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.ZIPCODE_INPUT)
        )
        zipcode_input.send_keys(zipcode)

        mobile_number_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AccountInformationPageLocators.MOBILE_NUMBER_INPUT)
        )
        mobile_number_input.send_keys(mobile_number)

        create_account_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AccountInformationPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        create_account_button.click()