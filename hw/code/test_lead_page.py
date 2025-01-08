import os
import pytest
import time
import functools
from base_case import BaseCase
from dotenv import load_dotenv
from ui.config_for_lead import FORM_RECOVERMENT_NAME, FORM_ARCHIVATION_NAME, FORM_CREATION_NAME, FORM_MODIFICATION_NAME, FORM_NOT_MODIFIED


load_dotenv()

def tear_down_creation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        my_lead_page = kwargs.get('my_lead_page') or args[1]
        my_lead_page.archive_form_creation()
        return result

    return wrapper

def tear_down_modification(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        my_lead_page = kwargs.get('my_lead_page') or args[1]
        my_lead_page.archive_form_modification()
        return result

    return wrapper

def tear_down_recover(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        my_lead_page = kwargs.get('my_lead_page') or args[1]
        my_lead_page.archive_form_recovering()
        return result

    return wrapper


@pytest.fixture
def login_data():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }


@pytest.mark.usefixtures("setup", "login_data")
class TestLeadPage(BaseCase):

    @tear_down_creation
    def test_new_form_creation(self, my_lead_page, login_data):
        my_lead_page.click_new_button()
        my_lead_page.fill_logo()

        my_lead_page.fill_1_form_name(FORM_CREATION_NAME)

        my_lead_page.fill_1_name('aa')
        my_lead_page.fill_1_heading('aa')
        my_lead_page.fill_1_description('aa')

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a')
        my_lead_page.fill_4_address('a')

        my_lead_page.click_save()

        form = my_lead_page.get_lead_form_name_creation()
        assert form == FORM_CREATION_NAME, "Форма не была создана!"

    def test_form_deletion(self, my_lead_page, login_data):
        my_lead_page.create_form(FORM_ARCHIVATION_NAME)

        my_lead_page.hover_form_deletion()
        my_lead_page.click_archive()

        my_lead_page.click_archive_confirmation()

        form = my_lead_page.get_lead_form_name_deletion()
        assert (not form or form != FORM_ARCHIVATION_NAME), 'Форма не была заархивирована!'

    @tear_down_modification
    def test_form_modification(self, my_lead_page, login_data):
        my_lead_page.create_form(FORM_NOT_MODIFIED)

        my_lead_page.hover_form_modification()
        my_lead_page.click_modify()

        my_lead_page.fill_1_form_name(FORM_MODIFICATION_NAME)

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a')
        my_lead_page.fill_4_address('a')

        my_lead_page.click_save()

        form = my_lead_page.get_lead_form_name_modification()
        assert form == FORM_MODIFICATION_NAME, "Форма не была отредактирована!"

    @tear_down_recover
    def test_form_recover(self, my_lead_page, login_data):
        my_lead_page.create_form(FORM_RECOVERMENT_NAME)

        my_lead_page.archive_form_recovering()

        my_lead_page.switch_to_archive()

        my_lead_page.hover_form_recover()
        my_lead_page.click_recover()
        my_lead_page.click_recover_confirmation()

        my_lead_page.switch_to_active()

        form = my_lead_page.get_lead_form_name_recovering()
        assert form == FORM_RECOVERMENT_NAME, "Форма не была восстановлена!"
