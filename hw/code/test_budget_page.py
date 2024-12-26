import pytest
from base_case import BaseCase
from dotenv import load_dotenv


load_dotenv()


@pytest.mark.usefixtures("setup", "login_data")
class TestBudgetPage(BaseCase):

    def test_fill_payment_amount_with_number(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount(1000)

        expected = "1\xa0000 ₽"
        result = budget_page.get_text_from_input()

        assert result == expected, f"Expected '{expected}', got '{result}'"

    def test_fill_payment_amount_with_text(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount("abc")

        expected = ""
        result = budget_page.get_text_from_input()

        assert result == expected, "Non-numeric input was not cleared as expected"

    def test_fill_payment_amount_too_low(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount(500)

        expected_message = "Минимальная сумма 600,00 ₽"
        error_text = budget_page.get_error_message()

        assert error_text == expected_message, f"Expected '{expected_message}', got '{error_text}'"

    def test_fill_payment_amount_too_high(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount(200001)

        expected_message = "уменьшите сумму"
        error_text = budget_page.get_error_message()

        assert error_text == expected_message, f"Expected '{expected_message}', got '{error_text}'"

    def test_test_fill_payment_amount_without_vat_with_number(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount_without_vat(1000)

        expected = "1\xa0000 ₽"
        result = budget_page.get_text_from_input_without_vat()

        assert result == expected, f"Expected '{expected}', got '{result}'"

    def test_test_fill_payment_amount_without_vat_with_text(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount_without_vat("abc")

        expected = ""
        result = budget_page.get_text_from_input_without_vat()

        assert result == expected, "Non-numeric input was not cleared as expected"

    def test_fill_payment_amount_without_vat_too_low(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount_without_vat(499)
        budget_page.click_recharge_button_popup()

        expected_message = "Минимальная сумма 600,00 ₽"
        error_text = budget_page.get_error_message()

        assert error_text == expected_message, f"Expected '{expected_message}', got '{error_text}'"

    def test_fill_payment_amount_without_vat_too_high(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount_without_vat(166667)
        budget_page.click_recharge_button_popup()

        expected_message = "уменьшите сумму"
        error_text = budget_page.get_error_message()

        assert error_text == expected_message, f"Expected '{expected_message}', got '{error_text}'"

    def test_numeric_input_without_vat(self, budget_page, login_data):
        budget_page.click_recharge_button()

        budget_page.fill_payment_amount_without_vat("800")
        expected = "960 ₽"
        result = budget_page.get_text_from_input()
        assert result == expected, f"Expected '{expected}', got '{result}'"

        budget_page.fill_payment_amount_without_vat("1333")
        expected = "1\xa0599,6 ₽"
        result = budget_page.get_text_from_input()
        assert result == expected, f"Expected '{expected}', got '{result}'"

        budget_page.fill_payment_amount_without_vat("1110,83")
        expected = "1\xa0333 ₽"
        result = budget_page.get_text_from_input()
        assert result == expected, f"Expected '{expected}', got '{result}'"

        budget_page.fill_payment_amount_without_vat("1300,17")
        expected = "1\xa0560,2 ₽"
        result = budget_page.get_text_from_input()
        assert result == expected, f"Expected '{expected}', got '{result}'"

    def test_valid_payment_opens_next_modal(self, budget_page, login_data):
        budget_page.click_recharge_button()
        budget_page.fill_payment_amount("600")
        budget_page.click_recharge_button_popup()

    def test_input_all_characters_in_promo_code_field(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()
        budget_page.click_activate_promocode()

        promo_code = "abc123!@#"
        budget_page.enter_promo_code(promo_code)

        result = budget_page.get_promo_code_input_value()

        assert result == promo_code, f"Expected '{promo_code}', got '{result}'"

    def test_error_on_invalid_promo_code(self, budget_page, login_data):
        budget_page.open_bonus_program_tab()
        budget_page.click_activate_promocode()

        invalid_promo_code = "INVALIDCODE"
        budget_page.enter_promo_code(invalid_promo_code)
        budget_page.click_activate_promo_code_button()

        expected = "Промокод не может быть активирован"
        result = budget_page.get_error_message_displayed()

        assert result == expected, f"Expected '{expected}', got '{result}'"
