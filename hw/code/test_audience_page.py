import pytest
import base_case
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("setup", "login_data")
class TestAudience(base_case.BaseCase):
    authorize = True

    def test_open(self, audience_page, login_data):
        assert audience_page.is_opened(), "The audience tab did not open as expected."

    def test_create_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.checking_open_audience_creation_menu()

    def test_add_source(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.checking_open_add_source_menu()

    def test_keywords(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        audience_page.checking_open_keywords_menu()

    def test_keywords_button_save_not_active(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        audience_page.checking_keywords_button_save_not_active()

    def test_keywords_period(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        audience_page.search_period(0)
        audience_page.check_search_period_less_one()
        audience_page.search_period(40)
        audience_page.check_search_period_more_thirty()

    def test_keywords_button_save(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.keywords_find(value)

    def test_source_deletion(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.source_deletion_icon()
        audience_page.source_deletion()
        audience_page.check_source_deletion()

    def test_source_edit(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.source_edit_icon()
        audience_page.checking_open_keywords_menu()
        audience_page.find_value_keywords(value)

    def test_cross_button(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.create_audience_click_cross_button()
        audience_page.check_abort_creation_window()
        audience_page.abort_audience_creation_click()
        audience_page.checking_open_audience_creation_menu()

    def test_save_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.checking_open_audience_creation_menu()

    def test_inactive_share_and_delete_buttons(self, audience_page, login_data):
        audience_page.check_inactive_share()
        audience_page.check_inactive_delete()

    def test_share_buttons(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.selected_audiece()
        audience_page.share_audience()
        audience_page.checking_share_window()

    def test_delete_buttons(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.selected_audiece()
        audience_page.delete_audience()
        audience_page.checking_delete_window()
        audience_page.delete_audience_click()

    def test_lists_users(self, audience_page, login_data):
        audience_page.open_lists_users()
        audience_page.download_list()
        audience_page.check_download_list()

    def test_offline_conversions(self, audience_page, login_data):
        audience_page.open_offline_conversions()
        audience_page.download_list()
        audience_page.check_offline_conversions()
