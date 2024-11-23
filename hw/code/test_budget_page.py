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

    def test_click_budget(self, login_page, login_data):
        my_budget_page = login_page.login(login_data["username"], login_data["password"])
        my_budget_page.click_budget()