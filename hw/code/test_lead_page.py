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
        page_opened = my_lead_page.is_opened()
        assert page_opened, 'New lead form not present'

    def test_new_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()
        popup = my_lead_page.check_popup_present()
        assert popup, "New lead form popup not displayed"


    def test_close_popup_by_clicking_close_button(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_popup_close_button()
        
        popup = my_lead_page.check_popup_present()
        assert not popup, "New lead form popup not displayed"

    def test_close_popup_by_clicking_cancel_button(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_cancel()
        popup = my_lead_page.check_popup_present()
        assert not popup, "New lead form popup not displayed"

    def test_more_text_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_more_text_button()

        big_desc_present = my_lead_page.check_big_description_present()

        assert big_desc_present, 'big description not present'

    def test_magnet_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()

        disc_present = my_lead_page.check_discount_present()

        assert disc_present, 'discount not present'

    def test_bonus_button_opens_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_bonus_button()

        bonus_present = my_lead_page.check_bonus_present()

        assert bonus_present, 'bonus not present'

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

        error1 = my_lead_page.check_error_1_name_message()
        error2 = my_lead_page.check_error_1_heading_message()
        error3 = my_lead_page.check_error_1_bonus_message()
        assert error1 == 'Превышена максимальная длина поля'
        assert error2 == 'Превышена максимальная длина поля'
        assert error3 == 'Превышена максимальная длина поля'

        my_lead_page.click_1_more_text_button()
        error4 = my_lead_page.check_error_1_big_description_message()
        assert error4 == 'Превышена максимальная длина поля'

        my_lead_page.click_1_compact_button()
        error5 = my_lead_page.check_error_1_description_message()
        assert error5 == 'Превышена максимальная длина поля'

    def test_error_empty_fields_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_bonus_button()

        my_lead_page.click_continue()

        error1 = my_lead_page.check_error_1_name_message()
        error2 = my_lead_page.check_error_1_heading_message()
        error3 = my_lead_page.check_error_1_bonus_message()
        error4 = my_lead_page.check_error_1_logo_message()

        assert error1 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error1}'"
        assert error2 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error2}'"
        assert error3 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error3}'"
        assert error4 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error4}'"

        my_lead_page.click_1_more_text_button()
        error5 = my_lead_page.check_error_1_big_description_message()
        assert error5 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error5}'"

        my_lead_page.click_1_compact_button()
        error6 = my_lead_page.check_error_1_description_message()
        assert error6 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error6}"

    def test_error_big_description_perenoc_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_more_text_button()
        my_lead_page.fill_1_big_description('a\n\n\na')

        my_lead_page.click_continue()

        error1 = my_lead_page.check_error_1_big_description_message()
        assert error1 == 'Используйте перенос строки не больше 2 раз подряд', f"Expected 'Используйте перенос строки не больше 2 раз подряд', got '{error1}'"

    def test_error_more_100_percent_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_percent_button()
        my_lead_page.fill_1_discount(101)

        my_lead_page.click_continue()

        error = my_lead_page.check_error_1_discount_message_for_101()
        assert error, 'no error for more than 100 percent'

    def test_error_0_percent_1(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.click_1_magnet_button()
        my_lead_page.click_1_percent_button()
        my_lead_page.fill_1_discount(0)

        my_lead_page.click_continue()

        error = my_lead_page.check_error_1_discount_message_for_0()
        assert error, 'no error for 0 discount'

    def test_switch_to_page_2(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        contact_present = my_lead_page.check_contact_present()
        assert contact_present, 'contact menu not present'

    def test_error_2_empty_question(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_continue()

        error1 = my_lead_page.check_error_2_question_message()
        assert error1 == 'Вопрос должен быть не пустым и содержать минимум 2 ответа', f"Expected 'Вопрос должен быть не пустым и содержать минимум 2 ответа', got '{error1}'"

    def test_close_question(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_bin()

        quest_closed = my_lead_page.check_question_closed()
        assert quest_closed, 'question is still presented'

    def test_error_2_empty_contact(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_bin_phone()
        my_lead_page.click_2_bin_name()

        my_lead_page.click_continue()

        error1 = my_lead_page.check_error_2_contact_message()
        assert error1 == 'Минимальное количество полей: 1', f"Expected 'Минимальное количество полей: 1', got '{error1}'"

    def test_2_shablon(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_shablon()
        my_lead_page.click_2_nothing_answer()

        answer_present = my_lead_page.check_3_answer_present()
        assert answer_present, 'answer not present'
        error1 = my_lead_page.check_3_answer_value()
        assert error1 == 'Ничего из перечисленного', f"Expected 'Ничего из перечисленного', got '{error1}'"

    def test_2_free_answer(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_answer_type()
        my_lead_page.click_2_free_answer()

        answer_not_present = my_lead_page.check_no_answer_present()
        assert answer_not_present, 'answer is presented'

    def test_2_add_answer(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_add_answer()

        answer_present = my_lead_page.check_3_answer_present()
        assert answer_present, 'answer not present'

    def test_2_delete_answer(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_question_button()

        my_lead_page.click_2_add_answer()

        answer_present = my_lead_page.check_3_answer_present()

        assert answer_present, 'answer not present'

        my_lead_page.click_2_bin_answer()

        answer_not_present = my_lead_page.check_3_answer_not_present()

        assert answer_not_present, 'answer is still presented'

    def test_error_2_contact_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_contact_button()

        popup = my_lead_page.check_2_popup_opened()
        assert popup, 'popup not present'

    def test_error_2_add_contact(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_2_add_contact_button()

        my_lead_page.click_popup_list_button()
        my_lead_page.click_popup_add_button()

        contact_added = my_lead_page.check_2_popup_add_contact()
        assert contact_added, 'contact is not added'

    def test_2_back_button(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_back()

        heading_1_page_present = my_lead_page.check_heading_present()

        assert heading_1_page_present, "heading field not displayed"

    def test_switch_to_page_3(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        heading_3_page_present = my_lead_page.check_3_heading_present()

        assert heading_3_page_present, 'can not switch to page 3'

    def test_3_buttons(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        site_field = my_lead_page.check_3_site_present()
        phone_field = my_lead_page.check_3_phone_present()
        promo_field = my_lead_page.check_3_promo_present()

        assert site_field, 'site field is not presented'
        assert phone_field, 'phone field is not presented'
        assert promo_field, 'promo field is not presented'

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

        error1 = my_lead_page.check_error_3_heading_message()
        assert error1 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error1}'"

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

        error1 = my_lead_page.check_error_3_heading_message()
        error2 = my_lead_page.check_error_3_description_message()
        error3 = my_lead_page.check_error_3_promo_message()

        assert error1 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error1}'"
        assert error2 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error2}'"
        assert error3 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error3}'"

    def test_3_phone_field(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.fill_3_phone('aааааа')

        my_lead_page.click_continue()

        error1 = my_lead_page.check_error_3_phone_message()
        assert error1 == 'Телефон должен начинаться с + и содержать только цифры', f"Expected 'Телефон должен начинаться с + и содержать только цифры', got '{error1}'"

    def test_3_site_field(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_3_click_site()
        my_lead_page.click_3_click_phone()
        my_lead_page.click_3_click_promo()

        my_lead_page.fill_3_site('aааааа')

        my_lead_page.click_continue()

        error1 = my_lead_page.check_error_3_site_message()
        assert error1 == 'Невалидный url', f"Expected 'Невалидный url', got '{error1}'"

    def test_switch_to_page_4(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        button_page_4 = my_lead_page.check_4_button_email_present()

        assert button_page_4, 'can not switch to page 4'

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

        warning = my_lead_page.check_4_warning_present()
        assert warning, 'warning is not present'

    def test_draft(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_popup_close_button()

        draft = my_lead_page.check_draft_present()
        assert draft, 'draft popup is not present'

    def test_4_email_input_popup(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_4_button_email()

        input_email = my_lead_page.check_4_input_email_notification_present()
        assert input_email, 'email field not present'

    def test_error_4_email(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_email('aaaaaaa')

        my_lead_page.click_save()

        error1 = my_lead_page.check_error_4_email_message()
        assert error1 == 'Некорректный email адрес', f"Expected 'Некорректный email адрес', got '{error1}'"

    def test_error_4_maximum_symbols(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a'*257)
        my_lead_page.fill_4_address('a'*257)
        my_lead_page.fill_4_inn('a'*33)

        my_lead_page.click_save()

        error1 = my_lead_page.check_error_4_fio_message()
        error2 = my_lead_page.check_error_4_address_message()
        error3 = my_lead_page.check_error_4_inn_message()

        assert error1 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error1}'"
        assert error2 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error2}'"
        assert error3 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error3}'"

    def test_error_4_empty_fields(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.click_save()

        error1 = my_lead_page.check_error_4_fio_message()
        error2 = my_lead_page.check_error_4_address_message()

        assert error1 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error1}'"
        assert error2 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error2}'"

    def test_save_lead_form(self, my_lead_page, login_data):
        my_lead_page.click_new_button()

        my_lead_page.switch_to_page_2()

        my_lead_page.click_continue()

        my_lead_page.click_continue()

        my_lead_page.fill_4_fio('a')
        my_lead_page.fill_4_address('a')

        my_lead_page.click_save()

        popup = my_lead_page.check_popup_present()
        assert not popup, "New lead form popup not displayed"
