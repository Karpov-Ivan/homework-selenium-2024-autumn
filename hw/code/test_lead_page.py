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