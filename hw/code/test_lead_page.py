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


    #ошибки в форме
    # def test_error_maximum_symbols_1(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.fill_1_name('a'*37)
    #     my_lead_page.fill_1_description('a'*44)
    #     my_lead_page.fill_1_heading('a'*52)

    #     my_lead_page.click_1_more_text_button()
    #     my_lead_page.fill_1_big_description('a'*351)

    #     my_lead_page.click_1_magnet_button()
    #     my_lead_page.click_1_bonus_button()
    #     my_lead_page.fill_1_bonus('a'*38)

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_1_name_message()
    #     error2 = my_lead_page.check_error_1_heading_message()
    #     error3 = my_lead_page.check_error_1_bonus_message()
    #     assert error1 == 'Превышена максимальная длина поля'
    #     assert error2 == 'Превышена максимальная длина поля'
    #     assert error3 == 'Превышена максимальная длина поля'

    #     my_lead_page.click_1_more_text_button()
    #     error4 = my_lead_page.check_error_1_big_description_message()
    #     assert error4 == 'Превышена максимальная длина поля'

    #     my_lead_page.click_1_compact_button()
    #     error5 = my_lead_page.check_error_1_description_message()
    #     assert error5 == 'Превышена максимальная длина поля'

    # def test_error_empty_fields_1(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.click_1_magnet_button()
    #     my_lead_page.click_1_bonus_button()

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_1_name_message()
    #     error2 = my_lead_page.check_error_1_heading_message()
    #     error3 = my_lead_page.check_error_1_bonus_message()

    #     assert error1 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error1}'"
    #     assert error2 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error2}'"
    #     assert error3 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error3}'"

    #     my_lead_page.click_1_more_text_button()
    #     error5 = my_lead_page.check_error_1_big_description_message()
    #     assert error5 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error5}'"

    #     my_lead_page.click_1_compact_button()
    #     error6 = my_lead_page.check_error_1_description_message()
    #     assert error6 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error6}"

    # def test_error_big_description_perenoc_1(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.click_1_more_text_button()
    #     my_lead_page.fill_1_big_description('a\n\n\na')

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_1_big_description_message()
    #     assert error1 == 'Используйте перенос строки не больше 2 раз подряд', f"Expected 'Используйте перенос строки не больше 2 раз подряд', got '{error1}'"

    # def test_error_more_100_percent_1(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.click_1_magnet_button()
    #     my_lead_page.click_1_percent_button()
    #     my_lead_page.fill_1_discount(101)

    #     my_lead_page.click_continue()

    #     error = my_lead_page.check_error_1_discount_message_for_101()
    #     assert error, 'no error for more than 100 percent'

    # def test_error_0_percent_1(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.click_1_magnet_button()
    #     my_lead_page.click_1_percent_button()
    #     my_lead_page.fill_1_discount(0)

    #     my_lead_page.click_continue()

    #     error = my_lead_page.check_error_1_discount_message_for_0()
    #     assert error, 'no error for 0 discount'

    # def test_error_2_empty_question(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_add_question_button()

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_2_question_message()
    #     assert error1 == 'Вопрос должен быть не пустым и содержать минимум 2 ответа', f"Expected 'Вопрос должен быть не пустым и содержать минимум 2 ответа', got '{error1}'"

    # def test_error_2_empty_contact(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_bin_phone()
    #     my_lead_page.click_2_bin_name()

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_2_contact_message()
    #     assert error1 == 'Минимальное количество полей: 1', f"Expected 'Минимальное количество полей: 1', got '{error1}'"

    # def test_2_shablon(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_add_question_button()

    #     my_lead_page.click_2_shablon()
    #     my_lead_page.click_2_nothing_answer()

    #     answer_present = my_lead_page.check_3_answer_present()
    #     assert answer_present, 'answer not present'
    #     error1 = my_lead_page.check_3_answer_value()
    #     assert error1 == 'Ничего из перечисленного', f"Expected 'Ничего из перечисленного', got '{error1}'"

    # def test_2_free_answer(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_add_question_button()

    #     my_lead_page.click_2_answer_type()
    #     my_lead_page.click_2_free_answer()

    #     answer_not_present = my_lead_page.check_no_answer_present()
    #     assert answer_not_present, 'answer is presented'

    # def test_2_add_answer(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_add_question_button()

    #     my_lead_page.click_2_add_answer()

    #     answer_present = my_lead_page.check_3_answer_present()
    #     assert answer_present, 'answer not present'

    # def test_2_delete_answer(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_add_question_button()

    #     my_lead_page.click_2_add_answer()

    #     answer_present = my_lead_page.check_3_answer_present()

    #     assert answer_present, 'answer not present'

    #     my_lead_page.click_2_bin_answer()

    #     answer_not_present = my_lead_page.check_3_answer_not_present()

    #     assert answer_not_present, 'answer is still presented'

    # def test_error_2_add_contact(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_2_add_contact_button()

    #     my_lead_page.click_popup_list_button()
    #     my_lead_page.click_popup_add_button()

    #     contact_added = my_lead_page.check_2_popup_add_contact()
    #     assert contact_added, 'contact is not added'

    # def test_3_empty_fields(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_3_click_site()
    #     my_lead_page.click_3_click_phone()
    #     my_lead_page.click_3_click_promo()

    #     my_lead_page.fill_3_heading('a'*26)
        
    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_3_heading_message()
    #     assert error1 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error1}'"

    # def test_3_maximum_symbols(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_3_click_site()
    #     my_lead_page.click_3_click_phone()
    #     my_lead_page.click_3_click_promo()

    #     my_lead_page.fill_3_heading('a'*26)
    #     my_lead_page.fill_3_description('a'*161)
    #     my_lead_page.fill_3_promo('a'*31)

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_3_heading_message()
    #     error2 = my_lead_page.check_error_3_description_message()
    #     error3 = my_lead_page.check_error_3_promo_message()

    #     assert error1 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error1}'"
    #     assert error2 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error2}'"
    #     assert error3 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error3}'"

    # def test_3_phone_field(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_3_click_site()
    #     my_lead_page.click_3_click_phone()
    #     my_lead_page.click_3_click_promo()

    #     my_lead_page.fill_3_phone('aааааа')

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_3_phone_message()
    #     assert error1 == 'Телефон должен начинаться с + и содержать только цифры', f"Expected 'Телефон должен начинаться с + и содержать только цифры', got '{error1}'"

    # def test_3_site_field(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_3_click_site()
    #     my_lead_page.click_3_click_phone()
    #     my_lead_page.click_3_click_promo()

    #     my_lead_page.fill_3_site('aааааа')

    #     my_lead_page.click_continue()

    #     error1 = my_lead_page.check_error_3_site_message()
    #     assert error1 == 'Невалидный url', f"Expected 'Невалидный url', got '{error1}'"

    # def test_error_4_email(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_continue()

    #     my_lead_page.fill_4_email('aaaaaaa')

    #     my_lead_page.click_save()

    #     error1 = my_lead_page.check_error_4_email_message()
    #     assert error1 == 'Некорректный email адрес', f"Expected 'Некорректный email адрес', got '{error1}'"

    # def test_error_4_maximum_symbols(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_continue()

    #     my_lead_page.fill_4_fio('a'*257)
    #     my_lead_page.fill_4_address('a'*257)
    #     my_lead_page.fill_4_inn('a'*33)

    #     my_lead_page.click_save()

    #     error1 = my_lead_page.check_error_4_fio_message()
    #     error2 = my_lead_page.check_error_4_address_message()
    #     error3 = my_lead_page.check_error_4_inn_message()

    #     assert error1 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error1}'"
    #     assert error2 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error2}'"
    #     assert error3 == 'Превышена максимальная длина поля', f"Expected 'Превышена максимальная длина поля', got '{error3}'"

    # def test_error_4_empty_fields(self, my_lead_page, login_data):
    #     my_lead_page.click_new_button()

    #     my_lead_page.switch_to_page_2()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_continue()

    #     my_lead_page.click_save()

    #     error1 = my_lead_page.check_error_4_fio_message()
    #     error2 = my_lead_page.check_error_4_address_message()

    #     assert error1 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error1}'"
    #     assert error2 == 'Обязательное поле', f"Expected 'Обязательное поле', got '{error2}'"

