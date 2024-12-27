import os
import pytest
import time
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

    def test_new_form_creation(self, my_lead_page, login_data):
        my_lead_page.click_new_button()
        my_lead_page.fill_logo()

        my_lead_page.fill_1_form_name('Тест на создание формы')

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
        assert form == "Тест на создание формы", "Форма не была создана!"

        my_lead_page.archive_form_creation()

    def test_form_deletion(self, my_lead_page, login_data):
        my_lead_page.create_form('Тест на архивирование формы')

        my_lead_page.hover_form_deletion()
        my_lead_page.click_archive()

        my_lead_page.click_archive_confirmation()

        form = my_lead_page.get_lead_form_name_deletion()
        assert (not form or form != "Тест на архивирование формы"), 'Форма не была заархивирована!'

    def test_form_modification(self, my_lead_page, login_data):
        my_lead_page.create_form('Текст должен быть отредактирован')

        my_lead_page.hover_form_modification()
        my_lead_page.click_modify()

        my_lead_page.fill_1_form_name('Тест на редактирование формы')

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a')
        my_lead_page.fill_4_address('a')

        my_lead_page.click_save()

        form = my_lead_page.get_lead_form_name_modification()
        assert form == "Тест на редактирование формы", "Форма не была отредактирована!"

        my_lead_page.archive_form_modification()

    def test_form_recover(self, my_lead_page, login_data):
        my_lead_page.create_form('Тест на восстановление формы')

        my_lead_page.archive_form_recovering()

        my_lead_page.switch_to_archive()

        my_lead_page.hover_form_recover()
        my_lead_page.click_recover()
        my_lead_page.click_recover_confirmation()

        my_lead_page.switch_to_active()

        form = my_lead_page.get_lead_form_name_recovering()
        assert form == "Тест на восстановление формы", "Форма не была отредактирована!"

        my_lead_page.archive_form_recovering()
