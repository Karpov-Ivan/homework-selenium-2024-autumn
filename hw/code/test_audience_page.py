import pytest
import base_case
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("setup", "login_data")
class TestAudience(base_case.BaseCase):
    authorize = True

    def test_keywords_button_save(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        title = "Новая аудитория"
        audience_page.input_name_audience(title)
        audience_page.save_audience()
        check_title = audience_page.check_audience_save()
        assert check_title == title, f"The Title audience is '{title}' not found (test save)"
        audience_page.selected_audiece()
        audience_page.open_delete_audience_menu()
        audience_page.delete_audience_click()
        check_delete = audience_page.check_audience_delete(title)
        assert check_delete, f"The audience {title} did not leave"

    def test_keywords_button_edit(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        value = "футбол"
        audience_page.keywords_input(value)
        audience_page.keywords_button_save()
        title = "Новая аудитория"
        audience_page.input_name_audience(title)
        audience_page.save_audience()
        check_title = audience_page.check_audience_save()
        assert check_title == title, f"The Title audience is '{title}' not found (test edit)"

        audience_page.open_edit_menu_button()
        audience_page.click_edit_icon()
        new_value = "волейбол"
        audience_page.keywords_edit_input(new_value)
        audience_page.keywords_button_save()
        new_title = "Обновленная аудитория"
        audience_page.input_name_audience(new_title)
        audience_page.save_audience()
        check_title = audience_page.check_audience_save()
        assert check_title == new_title, f"The Title audience is '{new_title}' not found (test edit)"

    def test_community_subscribers_button_save(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.community_subscribers()
        community = "КФ МГТУ им. Н. Э. Баумана"
        audience_page.community_subscribers_input(community)
        audience_page.all_community_vk()
        audience_page.create_all_community_vk_list()
        audience_page.community_subscribers_button_save()
        title = "Новая аудитория с сообществами"
        audience_page.input_name_audience(title)
        audience_page.save_audience()
        check_title = audience_page.check_audience_save()
        assert check_title == title, f"The Title audience is '{title}' not found (test save)"
        audience_page.selected_audiece()
        audience_page.open_delete_audience_menu()
        audience_page.delete_audience_click()
        check_delete = audience_page.check_audience_delete(title)
        assert check_delete, f"The audience {title} did not leave"

    def test_community_subscribers_button_edit(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.community_subscribers()
        community = "КФ МГТУ им. Н. Э. Баумана"
        audience_page.community_subscribers_input(community)
        audience_page.all_community_vk()
        audience_page.create_all_community_vk_list()
        audience_page.community_subscribers_button_save()
        title = "Новая аудитория с сообществами"
        audience_page.input_name_audience(title)
        audience_page.save_audience()
        check_title = audience_page.check_audience_save()
        assert check_title == title, f"The Title audience is '{title}' not found (test save)"

        audience_page.open_edit_menu_button()
        audience_page.click_edit_icon()
        audience_page.community_subscribers_edit_input()
        new_community = "VK Технопарк"
        audience_page.community_subscribers_input(new_community)
        audience_page.all_community_vk()
        audience_page.create_all_community_vk_list()
        audience_page.community_subscribers_button_save()
        new_title = "Обновленная аудитория с сообществами"
        audience_page.input_name_audience(new_title)
        audience_page.save_audience()
        check_title = audience_page.check_audience_save()
        assert check_title == new_title, f"The Title audience is '{new_title}' not found (test save)"
