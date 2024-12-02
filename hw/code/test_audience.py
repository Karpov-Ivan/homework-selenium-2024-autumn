import time

import pytest
import os
import base_case

@pytest.fixture(scope='session')
def credentials():
    return {
        "login": os.getenv("LOGIN"),
        "password": os.getenv("PASSWORD")
    }

class TestAudience(base_case.BaseCase):
    authorize = True

    def test_open(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        assert main_page.is_opened()

    def test_create_audience(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.checking_open_audience_creation_menu()

    def test_add_source(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.checking_open_add_source_menu()

    def test_keywords(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        main_page.checking_open_keywords_menu()

    def test_keywords_button_save_not_active(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        main_page.checking_keywords_button_save_not_active()

    def test_keywords_button_cancellation(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        main_page.keywords_button_cancellation()
        main_page.checking_open_audience_creation_menu()
        time.sleep(10)

    def test_keywords_period(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        main_page.search_period_less_one(0)
        main_page.check_search_period_less_one()
        main_page.search_period_more_thirty(40)
        main_page.check_search_period_more_thirty()

    def test_keywords_button_save(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        value = "футбол"
        main_page.keywords_input(value)
        main_page.keywords_button_save()
        main_page.keywords_find(value)

    def test_source_deletion(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        value = "футбол"
        main_page.keywords_input(value)
        main_page.keywords_button_save()
        main_page.source_deletion_icon()
        main_page.source_deletion()

    def test_source_edit(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        value = "футбол"
        main_page.keywords_input(value)
        main_page.keywords_button_save()
        main_page.source_edit_icon()
        main_page.checking_open_keywords_menu()
        main_page.find_value_keywords(value)

    def test_cross_button(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        value = "футбол"
        main_page.keywords_input(value)
        main_page.keywords_button_save()
        main_page.create_audience_click_cross_button()
        main_page.check_abort_creation_window()
        main_page.abort_audience_creation_click()
        main_page.checking_open_audience_creation_menu()

    def test_save_audience(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.create_audience()
        main_page.add_source()
        main_page.keywords()
        value = "футбол"
        main_page.keywords_input(value)
        main_page.keywords_button_save()
        main_page.save_audience()
        main_page.checking_open_audience_creation_menu()

    def test_inactive_share_and_delete_buttons(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.check_inactive_share()
        main_page.check_inactive_delete()

    def test_share_buttons(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.share_audience()
        main_page.checking_share_window()

    def test_delete_buttons(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.delete_audience()
        main_page.checking_delete_window()
        main_page.delete_audience_click()

    def test_lists_users(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.open_lists_users()
        main_page.download_list()
        main_page.check_download_list()

    def test_offline_conversions(self):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
        main_page.open_audience_tab()
        main_page.open_offline_conversions()
        main_page.download_list()
        main_page.check_offline_conversions()
