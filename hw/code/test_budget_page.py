import os
import pytest
from base_case import BaseCase
from dotenv import load_dotenv


load_dotenv()


@pytest.mark.usefixtures("setup", "login_data")
class TestBudgetPage(BaseCase):

    def test_open_budget_tab(self, budget_page, login_data):
        assert budget_page.is_opened(), "The budget tab did not open as expected."

    def test_recharge_button_opens_popup(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.check_popup_present()

    def test_close_popup_by_clicking_close_button(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.click_popup_close_button()
        budget_page.check_popup_closed()

    def test_fill_payment_amount_validation(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount("abc")
        assert budget_page.get_text_from_input() == "", "Non-numeric input was not cleared as expected."

    def test_recharge_amount_too_low(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount(500)
        budget_page.check_error_message("Минимальная сумма 600,00 ₽")

    def test_recharge_amount_too_high(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount(200001)
        budget_page.check_error_message("уменьшите сумму")

    def test_open_popup_and_check_text(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.click_button_help()
        budget_page.check_help_popup_present()

    def test_click_on_link_in_popup(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.click_button_help()
        budget_page.check_link_help_popup("https://ads.vk.com/help/articles/billing#min")

    def test_non_numeric_input_decimal(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount_without_vat("abc")
        assert budget_page.get_text_from_input_without_vat() == "", (
            "The non-numeric input was not cleared in the 'without VAT' field."
        )

    def test_numeric_input_without_vat(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount_without_vat("800")
        assert budget_page.get_text_from_input() == "960 ₽", "Expected 960 for input 800"

        budget_page.fill_payment_amount_without_vat(1333)
        assert budget_page.get_text_from_input() == "1\xa0599,6 ₽", "Expected 1599,6 for input 1333"

        budget_page.fill_payment_amount_without_vat("1110,83")
        assert budget_page.get_text_from_input() == "1\xa0333 ₽", "Expected 1333 for input 1110,83"

        budget_page.fill_payment_amount_without_vat("1300,17")
        assert budget_page.get_text_from_input() == "1\xa0560,2 ₽", "Expected 1560,20 for input 1300,17"

    def test_positive_input_no_errors(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount_without_vat("800")
        assert not budget_page.is_error_present(), "No error message should appear for valid input"

    def test_recharge_amount_below_min(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount_without_vat("499")
        budget_page.click_recharge_button_popup()
        budget_page.check_error_message("Минимальная сумма 600,00 ₽")

    def test_recharge_amount_above_max(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount_without_vat("166667")
        budget_page.click_recharge_button_popup()
        budget_page.check_error_message("уменьшите сумму")

    def test_open_popup_and_check_text_2(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.click_button_help_2()
        budget_page.check_help_popup_present_2()

    def test_click_on_link_in_popup_2(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.click_button_help_2()
        budget_page.check_link_help_popup("https://ads.vk.com/help/articles/billing#min")

    def test_valid_payment_opens_next_modal(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount("600")
        budget_page.click_recharge_button_popup()

    def test_bonus_program_page(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()

        assert self.driver.current_url == "https://ads.vk.com/hq/budget/bonus", "URL does not match Bonus Program page"

        budget_page.check_element_bonus_program_page()

    def test_activate_promocode_popup_opens(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()

        budget_page.click_activate_promocode()

        budget_page.check_activate_promocode_popup()

    def test_close_promocode_popup(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()

        budget_page.click_activate_promocode()

        budget_page.click_close_activate_promocode()

    def test_input_all_characters_in_promo_code_field(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()

        budget_page.click_activate_promocode()

        promo_code = "abc123!@#"
        budget_page.enter_promo_code(promo_code)
        assert budget_page.get_promo_code_input_value() == promo_code, "The input field should accept all entered characters."

    def test_error_on_invalid_promo_code(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()

        budget_page.click_activate_promocode()

        invalid_promo_code = "INVALIDCODE"
        budget_page.enter_promo_code(invalid_promo_code)
        budget_page.click_activate_promo_code_button()

        assert budget_page.is_error_message_displayed(), (
            "Expected an error message to inform the user about the invalid promo code."
        )