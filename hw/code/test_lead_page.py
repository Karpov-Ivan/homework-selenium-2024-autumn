import os
import pytest
from base_case import BaseCase
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture
def login_data():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }


@pytest.mark.usefixtures("setup", "login_data")
class TestLeadPage(BaseCase):

    def test_open_budget_tab(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()

        assert my_lead_page.is_opened()

    def test_new_button_opens_popup(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()
        my_lead_page.click_new_button()

        my_lead_page.check_popup_present()

    def test_close_popup_by_clicking_close_button(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()
        my_lead_page.click_new_button()

        my_lead_page.click_popup_close_button()
        my_lead_page.check_popup_closed()

    def test_close_popup_by_clicking_outside(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()
        my_lead_page.click_new_button()

        my_lead_page.click_outside()
        my_lead_page.check_popup_closed()

    def test_close_popup_by_clicking_cancel_button(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()
        my_lead_page.click_new_button()

        my_lead_page.click_cancel()
        my_lead_page.check_popup_closed()

    def test_more_text_button_opens_popup(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()
        my_lead_page.click_new_button()

        my_lead_page.click_1_more_text_button()

        my_lead_page.check_big_description_present()

    def test_more_text_button_opens_popup(self, login_page, login_data):
        my_lead_page = login_page.login_for_lead(login_data["username"], login_data["password"])
        my_lead_page.open_lead_tab()
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()

        my_lead_page.check_skidka_present()
    

    
        