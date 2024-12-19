import pytest
import base_case
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("setup", "login_data")
class TestAudience(base_case.BaseCase):
    authorize = True

    def test_open(self, audience_page, login_data):
        is_open = audience_page.is_opened()
        assert is_open, "The audience tab did not open as expected."

    def test_create_audience(self, audience_page, login_data):
        audience_page.create_audience()
        check_creation_menu = audience_page.checking_open_audience_creation_menu()
        assert check_creation_menu, "Audience creation menu is not displayed"

    def test_add_source(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        check_add_source_menu = audience_page.checking_open_add_source_menu()
        assert check_add_source_menu, "Power on menu of the source is not displayed"

    def test_keywords(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        check_keywords_menu = audience_page.checking_open_keywords_menu()
        assert check_keywords_menu, "Keywords menu is not displayed"

    def test_keywords_button_save_not_active(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        check_keywords_button_save_not_active = audience_page.checking_keywords_button_save_not_active()
        assert check_keywords_button_save_not_active, "Button is active and should not be active"

    def test_keywords_period(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        audience_page.search_period(0)
        check_search_period_less_one = audience_page.check_search_period_less_one()
        assert check_search_period_less_one, "Period is not equal to 1"
        audience_page.search_period(40)
        check_search_period_more_thirty = audience_page.check_search_period_more_thirty()
        assert check_search_period_more_thirty, "Period is not equal to 30"

    def test_keywords_button_save(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        check_keywords_find = audience_page.keywords_find(value)
        assert check_keywords_find, f"The keyword is '{value}' not found"

    def test_source_deletion(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.source_deletion_icon()
        audience_page.source_deletion()
        check_source_deletion = audience_page.check_source_deletion()
        assert check_source_deletion, "The source has not been deleted"

    def test_source_edit(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        audience_page.source_edit_icon()
        check_keywords_menu = audience_page.checking_open_keywords_menu()
        check_find_value_keywords = audience_page.find_value_keywords(value)
        assert check_keywords_menu, "Keywords menu is not displayed"
        assert check_find_value_keywords, f"there is no meaning in the keywords '{value}'"

    def test_cross_button(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        check_visibility = audience_page.create_audience_click_cross_button_check_visibility()
        assert check_visibility, "This element is not visible"
        audience_page.create_audience_click_cross_button()
        check_abort_creation_window = audience_page.check_abort_creation_window()
        assert check_abort_creation_window, "Menu for interrupting the audience did not appear"
        audience_page.abort_audience_creation_click()
        check_open_audience_creation_menu = audience_page.checking_open_audience_creation_menu()
        assert check_open_audience_creation_menu, "Audience creation menu is not displayed"

    def test_save_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        check_visibility = audience_page.save_audience_check_visibility()
        assert check_visibility, "This element is not visible"
        audience_page.save_audience()
        check_open = audience_page.is_opened()
        assert check_open, "The audience tab did not open as expected."

    def test_inactive_share_and_delete_buttons(self, audience_page, login_data):
        check_inactive_share = audience_page.check_inactive_share()
        check_inactive_delete = audience_page.check_inactive_delete()
        assert check_inactive_share, "Button share is active and should not be active"
        assert check_inactive_delete, "Button delete is active and should not be active"

    def test_share_buttons(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        check_visibility = audience_page.save_audience_check_visibility()
        assert check_visibility, "This element is not visible"
        audience_page.save_audience()
        audience_page.selected_audiece()
        check_visibility = audience_page.share_audience_check_visibility()
        assert check_visibility, "This element is not visible"
        audience_page.share_audience()
        check_share_window = audience_page.checking_share_window()
        assert check_share_window, "There is no given title in the menu or the menu has not opened"

    def test_delete_buttons(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        check_visibility = audience_page.save_audience_check_visibility()
        assert check_visibility, "This element is not visible"
        audience_page.save_audience()
        audience_page.selected_audiece()
        check_delete_audience = audience_page.delete_audience()
        assert check_delete_audience, "This element is not visible"
        check_delete_window = audience_page.checking_delete_window()
        assert check_delete_window, "There is no given title in the menu or the menu has not opened"
        audience_page.delete_audience_click()

    def test_lists_users(self, audience_page, login_data):
        audience_page.open_lists_users()
        audience_page.download_list()
        check_visibility = audience_page.check_download_list_check_visibility()
        check_download_list = audience_page.check_download_list()
        assert check_visibility, "This element is not visible"
        assert check_download_list, "The user list download menu did not open"

    def test_offline_conversions(self, audience_page, login_data):
        audience_page.open_offline_conversions()
        audience_page.download_list()
        check_visibility = audience_page.check_offline_conversions_check_visibility()
        check_offline_conversions = audience_page.check_offline_conversions()
        assert check_visibility, "This element is not visible"
        assert check_offline_conversions, "The menu for downloading the list of users in the offline conference did not open"
