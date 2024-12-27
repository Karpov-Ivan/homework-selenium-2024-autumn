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

    def fill_payment_amount(self, amount):
        self.enter_text(BudgetPageLocators.INPUT_PAYMENT_AMOUNT, amount)

    def get_text_from_input(self):
        return self.get_element_value(BudgetPageLocators.INPUT_PAYMENT_AMOUNT)

    def get_error_message_min(self):
        error = self.find(BudgetPageLocators.ERROR_MESSAGE_MIN_VALUE)
        return error.text

    def get_error_message_max(self):
        error = self.find(BudgetPageLocators.ERROR_MESSAGE_MAX_VALUE)
        return error.text

    def fill_payment_amount_without_vat(self, decimal):
        self.enter_text(BudgetPageLocators.INPUT_PAYMENT_AMOUNT_WITHOUT_VAT, decimal)

    def get_text_from_input_without_vat(self):
        return self.get_element_value(BudgetPageLocators.INPUT_PAYMENT_AMOUNT_WITHOUT_VAT)

    def click_recharge_button_popup(self):
        self.click(BudgetPageLocators.BUTTON_RECHARGE_POPUP)

    def open_bonus_program_tab(self):
        self.click(BudgetPageLocators.TAB_BONUS_PROGRAM)

    def click_activate_promocode(self):
        self.click(BudgetPageLocators.ACTIVATE_PROMOCODE_BUTTON)

    def enter_promo_code(self, promo_code):
        self.enter_text(BudgetPageLocators.INPUT_PROMOCODE, promo_code)

    def get_promo_code_input_value(self):
        return self.get_element_value(BudgetPageLocators.INPUT_PROMOCODE)

    def click_activate_promo_code_button(self):
        self.click(BudgetPageLocators.BUTTON_PROMOCODE)

    def get_error_message_promocode(self):
        error = self.find(BudgetPageLocators.ERROR_MESSAGE_PROMOCODE)
        return error.text
