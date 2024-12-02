import os
import pytest
from base_case import BaseCase
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture
def login_data():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }


@pytest.mark.usefixtures("setup", "login_data")
class TestBudgetPage(BaseCase):

    def test_open_budget_tab(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()

        assert my_budget_page.is_opened(), "The budget tab did not open as expected."

    def test_recharge_button_opens_popup(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.check_popup_present()

    def test_close_popup_by_clicking_close_button(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.click_popup_close_button()
        my_budget_page.check_popup_closed()

    def test_fill_payment_amount_validation(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount("abc")
        assert my_budget_page.get_text_from_input() == "", "Non-numeric input was not cleared as expected."

    def test_recharge_amount_too_low(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount(500)
        my_budget_page.check_error_message("Минимальная сумма 600,00 ₽")

    def test_recharge_amount_too_high(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount(200001)
        my_budget_page.check_error_message("уменьшите сумму")

    def test_open_popup_and_check_text(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.click_button_help()
        my_budget_page.check_help_popup_present()

    def test_click_on_link_in_popup(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.click_button_help()
        my_budget_page.check_link_help_popup("https://ads.vk.com/help/articles/billing#min")

    def test_non_numeric_input_decimal(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount_without_vat("abc")
        assert my_budget_page.get_text_from_input_without_vat() == "", (
            "The non-numeric input was not cleared in the 'without VAT' field."
        )

    def test_numeric_input_without_vat(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount_without_vat("800")
        assert my_budget_page.get_text_from_input() == "960 ₽", "Expected 960 for input 800"

        my_budget_page.fill_payment_amount_without_vat(1333)
        assert my_budget_page.get_text_from_input() == "1\xa0599,6 ₽", "Expected 1599,6 for input 1333"

        my_budget_page.fill_payment_amount_without_vat("1110,83")
        assert my_budget_page.get_text_from_input() == "1\xa0333 ₽", "Expected 1333 for input 1110,83"

        my_budget_page.fill_payment_amount_without_vat("1300,17")
        assert my_budget_page.get_text_from_input() == "1\xa0560,2 ₽", "Expected 1560,20 for input 1300,17"

    def test_positive_input_no_errors(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount_without_vat("800")
        assert not my_budget_page.is_error_present(), "No error message should appear for valid input"

    def test_recharge_amount_below_min(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount_without_vat("499")
        my_budget_page.click_recharge_button_popup()
        my_budget_page.check_error_message("Минимальная сумма 600,00 ₽")

    def test_recharge_amount_above_max(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount_without_vat("166667")
        my_budget_page.click_recharge_button_popup()
        my_budget_page.check_error_message("уменьшите сумму")

    def test_open_popup_and_check_text_2(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.click_button_help_2()
        my_budget_page.check_help_popup_present_2()

    def test_click_on_link_in_popup_2(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.click_button_help_2()
        my_budget_page.check_link_help_popup("https://ads.vk.com/help/articles/billing#min")

    def test_valid_payment_opens_next_modal(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.click_recharge_button()

        my_budget_page.fill_payment_amount("600")
        my_budget_page.click_recharge_button_popup()

    def test_bonus_program_page(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()

        my_budget_page.open_bonus_program_tab()

        assert self.driver.current_url == "https://ads.vk.com/hq/budget/bonus", "URL does not match Bonus Program page"

        my_budget_page.check_element_bonus_program_page()

    def test_activate_promocode_popup_opens(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()

        my_budget_page.open_bonus_program_tab()

        my_budget_page.click_activate_promocode()

        my_budget_page.check_activate_promocode_popup()

    def test_close_promocode_popup(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()

        my_budget_page.open_bonus_program_tab()

        my_budget_page.click_activate_promocode()

        my_budget_page.click_close_activate_promocode()

    def test_input_all_characters_in_promo_code_field(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.open_bonus_program_tab()

        my_budget_page.click_activate_promocode()

        promo_code = "abc123!@#"
        my_budget_page.enter_promo_code(promo_code)
        assert my_budget_page.get_promo_code_input_value() == promo_code, "The input field should accept all entered characters."

    def test_error_on_invalid_promo_code(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.open_budget_tab()
        my_budget_page.open_bonus_program_tab()

        my_budget_page.click_activate_promocode()

        invalid_promo_code = "INVALIDCODE"
        my_budget_page.enter_promo_code(invalid_promo_code)
        my_budget_page.click_activate_promo_code_button()

        assert my_budget_page.is_error_message_displayed(), (
            "Expected an error message to inform the user about the invalid promo code."
        )