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

    def test_open_lead_tab(self, my_lead_page, login_data):

        assert my_lead_page.is_opened()

    def test_new_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.check_popup_present()

    def test_close_popup_by_clicking_close_button(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_popup_close_button()
        my_lead_page.check_popup_closed()

    def test_close_popup_by_clicking_cancel_button(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_cancel()
        my_lead_page.check_popup_closed()

    def test_more_text_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.send_logo()

        time.wait(10)

        my_lead_page.click_1_more_text_button()

        my_lead_page.check_big_description_present()

    def test_magnet_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()

        my_lead_page.check_discount_present()

    def test_bonus_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_bonus_button()

        my_lead_page.check_bonus_present()

    def test_error_maximum_symbols_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.fill_1_name('a'*37)
        my_lead_page.fill_1_description('a'*44)
        my_lead_page.fill_1_heading('a'*52)

        my_lead_page.click_1_more_text_button()
        my_lead_page.fill_1_big_description('a'*351)

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_bonus_button()
        my_lead_page.fill_1_bonus('a'*38)

        my_lead_page.click_continue()

        my_lead_page.check_error_1_name_message('Превышена максимальная длина поля')
        my_lead_page.check_error_1_heading_message('Превышена максимальная длина поля')
        my_lead_page.check_error_1_bonus_message('Превышена максимальная длина поля')

        my_lead_page.click_1_more_text_button()
        my_lead_page.check_error_1_big_description_message('Превышена максимальная длина поля')

        my_lead_page.click_1_compact_button()
        my_lead_page.check_error_1_description_message('Превышена максимальная длина поля')

    def test_error_empty_fields_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_bonus_button()

        my_lead_page.click_continue()

        my_lead_page.check_error_1_name_message('Обязательное поле')
        my_lead_page.check_error_1_heading_message('Обязательное поле')
        my_lead_page.check_error_1_bonus_message('Обязательное поле')
        my_lead_page.check_error_1_logo_message('Обязательное поле')

        my_lead_page.click_1_more_text_button()
        my_lead_page.check_error_1_big_description_message('Обязательное поле')

        my_lead_page.click_1_compact_button()
        my_lead_page.check_error_1_description_message('Обязательное поле')

    def test_error_big_description_perenoc_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_more_text_button()
        my_lead_page.fill_1_big_description('a\n\n\na')

        my_lead_page.click_continue()

        my_lead_page.check_error_1_big_description_message('Используйте перенос строки не больше 2 раз подряд')

    def test_error_more_100_percent_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_percent_button()
        my_lead_page.fill_1_discount(101)

        my_lead_page.click_continue()

        my_lead_page.check_error_1_discount_message_for_101()

    def test_error_0_percent_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_percent_button()
        my_lead_page.fill_1_discount(0)

        my_lead_page.click_continue()

        my_lead_page.check_error_1_discount_message_for_0()

    def test_switch_to_page_2(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.check_contact_present()

    def test_error_2_empty_question(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_continue()

        my_lead_page.check_error_2_question_message('Вопрос должен быть не пустым и содержать минимум 2 ответа')

    def test_close_question(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_bin()

        my_lead_page.check_question_closed()

    def test_error_2_empty_contact(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_bin_phone()
        my_lead_page.click_2_bin_name()

        my_lead_page.click_continue()

        my_lead_page.check_error_2_contact_message('Минимальное количество полей: 1')

    def test_2_shablon(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_shablon()
        my_lead_page.click_2_nothing_answer()

        my_lead_page.check_3_answer_present()
        my_lead_page.check_3_answer_value('Ничего из перечисленного')

    def test_2_free_answer(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_answer_type()
        my_lead_page.click_2_free_answer()

        my_lead_page.check_no_answer_present()

    def test_2_add_answer(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_add_answer()

        my_lead_page.check_3_answer_present()

    def test_2_delete_answer(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_add_answer()

        my_lead_page.check_3_answer_present()

        my_lead_page.click_2_bin_answer()

        my_lead_page.check_3_answer_not_present()

    def test_error_2_contact_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_contact_button()

        my_lead_page.check_2_popup_opened()

    def test_error_2_add_contact(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_contact_button()

        my_lead_page.click_popup_list_button()
        my_lead_page.click_popup_add_button()

        my_lead_page.check_2_popup_add_contact()

    def test_2_back_button(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_back()

        my_lead_page.check_heading_present()

    def test_switch_to_page_3(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.check_3_heading_present()

    def test_3_buttons(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.check_3_site_present()
        my_lead_page.check_3_phone_present()
        my_lead_page.check_3_promo_present()

    def test_3_empty_fields(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.fill_3_heading('a'*26)
        
        my_lead_page.click_continue()

        my_lead_page.fill_3_heading_alt('')

        my_lead_page.click_continue()

        my_lead_page.check_error_3_heading_message('Обязательное поле')

    def test_3_maximum_symbols(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.fill_3_heading('a'*26)
        my_lead_page.fill_3_description('a'*161)
        my_lead_page.fill_3_promo('a'*31)

        my_lead_page.click_continue()

        my_lead_page.check_error_3_heading_message('Превышена максимальная длина поля')
        my_lead_page.check_error_3_description_message('Превышена максимальная длина поля')
        my_lead_page.check_error_3_promo_message('Превышена максимальная длина поля')

    def test_3_phone_field(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.fill_3_phone('aааааа')

        my_lead_page.click_continue()

        my_lead_page.check_error_3_phone_message('Телефон должен начинаться с + и содержать только цифры')

    def test_3_site_field(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.fill_3_site('aааааа')

        my_lead_page.click_continue()

        my_lead_page.check_error_3_site_message('Невалидный url')

    def test_switch_to_page_4(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.check_4_button_email_present()

    def test_4_button_necessary_questions(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()
        my_lead_page.fill_2_question('aaa')
        my_lead_page.fill_2_answer_1('aaa')
        my_lead_page.fill_2_answer_2('aaa')

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_4_click_necessary_question()
        my_lead_page.check_4_warning_present()

    def test_draft(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_popup_close_button()
        my_lead_page.check_draft_present()

    def test_4_email_input_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_4_button_email()
        my_lead_page.check_4_input_email_notification_present()

    def test_error_4_email(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_email('aaaaaaa')

        my_lead_page.click_save()

        my_lead_page.check_error_4_email_message('Некорректный email адрес')

    def test_error_4_maximum_symbols(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a'*257)
        my_lead_page.fill_4_address('a'*257)
        my_lead_page.fill_4_inn('a'*33)

        my_lead_page.click_save()

        my_lead_page.check_error_4_fio_message('Превышена максимальная длина поля')
        my_lead_page.check_error_4_address_message('Превышена максимальная длина поля')
        my_lead_page.check_error_4_inn_message('Превышена максимальная длина поля')

    def test_error_4_empty_fields(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_save()

        my_lead_page.check_error_4_fio_message('Обязательное поле')
        my_lead_page.check_error_4_address_message('Обязательное поле')

    def test_save_lead_form(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a')
        my_lead_page.fill_4_address('a')

        my_lead_page.click_save()

        my_lead_page.check_popup_closed()
