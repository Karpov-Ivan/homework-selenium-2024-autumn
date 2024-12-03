import time
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from ..locators.budget_page_locators import BudgetPageLocators


class BudgetPage(BasePage):
    url = "https://ads.vk.com/hq/budget/transactions"
    locators = BudgetPageLocators

    def __init__(self, driver):
        self.driver = driver

    def open_budget_tab(self):
        self.click(self.locators.TAB_BUDGET, 10)

    def click_recharge_button(self):
        self.click(BudgetPageLocators.BUTTON_RECHARGE)

    def check_popup_present(self):
        assert self.is_element_present(BudgetPageLocators.POPUP_RECHARGE), "Recharge popup not displayed"

    def check_popup_closed(self):
        assert not self.is_element_present(BudgetPageLocators.POPUP_RECHARGE, 10), "Recharge popup not displayed"

    def fill_payment_amount(self, amount):
        self.enter_text(BudgetPageLocators.INPUT_PAYMENT_AMOUNT, amount)

    def get_text_from_input(self):
        return self.get_element_value(BudgetPageLocators.INPUT_PAYMENT_AMOUNT)

    def click_popup_close_button(self):
        self.click(BudgetPageLocators.CLOSE_BUTTON_LOCATOR)

    def check_error_message(self, expected_message):
        error = self.find(BudgetPageLocators.ERROR_MESSAGE)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def click_button_help(self):
        self.click(BudgetPageLocators.ICON_HELP)

    def check_help_popup_present(self):
        assert self.is_element_present(BudgetPageLocators.POPUP_HEADER), "Popup header not found"

    def click_link_help_popup(self):
        self.click(BudgetPageLocators.POPUP_LINK)

    def check_link_help_popup(self, expected_url):
        current_window = self.driver.current_window_handle

        self.click_link_help_popup()

        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == expected_url)
        assert self.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {self.driver.current_url}"

    def fill_payment_amount_without_vat(self, decimal):
        self.enter_text(BudgetPageLocators.INPUT_PAYMENT_AMOUNT_WITHOUT_VAT, decimal)

    def get_text_from_input_without_vat(self):
        return self.get_element_value(BudgetPageLocators.INPUT_PAYMENT_AMOUNT_WITHOUT_VAT)

    def is_error_present(self):
        return self.is_element_present(BudgetPageLocators.ERROR_MESSAGE)

    def click_recharge_button_popup(self):
        self.click(BudgetPageLocators.BUTTON_RECHARGE_POPUP)

    def click_button_help_2(self):
        self.click(BudgetPageLocators.ICON_HELP_2)

    def check_help_popup_present_2(self):
        assert self.is_element_present(BudgetPageLocators.POPUP_HEADER_2), "Popup header not found"

    def open_bonus_program_tab(self):
        self.click(BudgetPageLocators.TAB_BONUS_PROGRAM)

    def check_element_bonus_program_page(self):
        assert self.is_element_present(
            BudgetPageLocators.ACTIVATE_PROMOCODE_BUTTON), "Activate Promocode button is not present"

        assert self.is_element_present(
            BudgetPageLocators.ACTIVATED_PROMOCODES_HEADER), "'Activated Promocodes' header is not present"

        assert self.is_element_present(
            BudgetPageLocators.PERSONAL_OFFERS_HEADER), "'Personal Offers' header is not present"

    def click_activate_promocode(self):
        self.click(BudgetPageLocators.ACTIVATE_PROMOCODE_BUTTON)

    def check_activate_promocode_popup(self):
        assert self.is_element_present(BudgetPageLocators.POPUP_HEADER_PROMOCODE), "Pop-up window not opened"

    def click_close_activate_promocode(self):
        self.click(BudgetPageLocators.CLOSE_BUTTON_LOCATOR)

    def enter_promo_code(self, promo_code):
        self.enter_text(BudgetPageLocators.INPUT_PROMOCODE, promo_code)

    def get_promo_code_input_value(self):
        return self.get_element_value(BudgetPageLocators.INPUT_PROMOCODE)

    def click_activate_promo_code_button(self):
        self.click(BudgetPageLocators.BUTTON_PROMOCODE)

    def is_error_message_displayed(self):
        return self.is_element_present(BudgetPageLocators.ERROR_MESSAGE_PROMOCODE)