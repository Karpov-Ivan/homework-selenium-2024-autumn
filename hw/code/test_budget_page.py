import os
import time

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

        assert my_budget_page.is_opened()

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
        assert my_budget_page.get_text_from_input() == ""

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
        assert my_budget_page.get_text_from_input_without_vat() == ""

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