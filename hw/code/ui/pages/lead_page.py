import time
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from ..locators.lead_page_locators import LeadPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


class LeadPage(BasePage):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadPageLocators

    def __init__(self, driver):
        self.driver = driver

    def open_lead_tab(self):
        self.click(self.locators.TAB_LEAD, 100)

    def click_new_button(self):
        self.click(LeadPageLocators.BUTTON_NEW)

    def click_popup_close_button(self):
        self.click(LeadPageLocators.CLOSE_BUTTON_LOCATOR)

    def fill_1_form_name(self, name):
        self.enter_text(LeadPageLocators.INPUT_1_FORM_NAME, name, 10)

    def fill_1_name(self, name):
        self.enter_text(LeadPageLocators.INPUT_1_NAME, name, 10)

    def fill_1_heading(self, heading):
        self.enter_text(LeadPageLocators.INPUT_1_HEADING, heading)

    def fill_1_description(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_DESCRIPTION, description)

    def fill_1_big_description(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_BIG_DESCRIPTION, description)

    def fill_1_bonus(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_BONUS, description)

    def fill_1_discount(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_AMOUNT, description)

    def click_1_compact_button(self):
        self.click(LeadPageLocators.BUTTON_COMPACT)

    def click_1_more_text_button(self):
        self.click(LeadPageLocators.BUTTON_MORE_TEXT)

    def click_1_magnet_button(self):
        self.click(LeadPageLocators.BUTTON_MAGNET)

    def click_1_discount_button(self):
        self.click(LeadPageLocators.BUTTON_SKIDKA)

    def click_1_bonus_button(self):
        self.click(LeadPageLocators.BUTTON_BONUS)

    def click_1_percent_button(self):
        self.click(LeadPageLocators.BUTTON_PERCENT)

    def click_cancel(self):
        self.click(LeadPageLocators.BUTTON_CANCEL)

    def click_continue(self):
        self.click(LeadPageLocators.BUTTON_CONTINUE)

    def click_back(self):
        self.click(LeadPageLocators.BUTTON_BACK)

    def click_save(self):
        self.click(LeadPageLocators.BUTTON_SAVE)

    def click_popup_close_button(self):
        self.click(LeadPageLocators.CLOSE_BUTTON_LOCATOR)

    def check_heading_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_1_HEADING)

    def check_big_description_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_1_BIG_DESCRIPTION)

    def check_discount_present(self):
        return self.is_element_present(LeadPageLocators.BUTTON_SKIDKA)

    def check_bonus_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_1_BONUS)

    def check_error_1_name_message(self):
        error = self.find(LeadPageLocators.ERROR_1_NAME)
        return error.text 

    def check_error_1_description_message(self):
        error = self.find(LeadPageLocators.ERROR_1_DESCRIPTION)
        return error.text

    def check_error_1_heading_message(self):
        error = self.find(LeadPageLocators.ERROR_1_HEADING)
        return error.text

    def check_error_1_big_description_message(self):
        error = self.find(LeadPageLocators.ERROR_1_BIG_DESCRIPTION)
        return error.text

    def check_error_1_bonus_message(self):
        error = self.find(LeadPageLocators.ERROR_1_BONUS)
        return error.text

    def check_error_1_discount_message_for_101(self):
        return self.is_element_present(LeadPageLocators.ERROR_1_SKIDKA_FOR_101)

    def check_error_1_discount_message_for_0(self):
        return self.is_element_present(LeadPageLocators.ERROR_1_SKIDKA_FOR_0)
    
    def fill_logo(self):
        self.click(LeadPageLocators.BUTTON_LOGO)
        self.click(LeadPageLocators.ITEM_LOGO)
    
    def create_form(self, form_name):
        self.click_new_button()
        self.fill_logo()

        self.fill_1_form_name(form_name)

        self.fill_1_name('aa')
        self.fill_1_heading('aa')
        self.fill_1_description('aa')

        self.click_continue()

        self.click_continue()

        self.click_continue()

        self.fill_4_fio('a')
        self.fill_4_address('a')

        self.click_save()

    def get_lead_form_name_creation(self):
        name = self.find(LeadPageLocators.LEAD_FORM_NAME_FOR_CREATE, 10)
        return name.text
        
    def get_lead_form_name_deletion(self):
        name = self.find(LeadPageLocators.LEAD_FORM_NAME_FOR_ARCHIVE, 10)
        try:
            return name.text
        except StaleElementReferenceException:
            return None
        
    def get_lead_form_name_modification(self):
        name = self.find(LeadPageLocators.LEAD_FORM_NAME_FOR_MODIFY, 10)
        return name.text

    def hover_form_deletion(self):
        form = self.find(LeadPageLocators.LEAD_FORM_NAME_FOR_ARCHIVE, 10)

        action = ActionChains(self.driver)
        action.move_to_element(form).perform()

    def hover_form_modification(self):
        form = self.find(LeadPageLocators.LEAD_FORM_NAME_NOT_MODIFIED, 10)

        action = ActionChains(self.driver)
        action.move_to_element(form).perform()

    def click_archive(self):
        self.click(LeadPageLocators.LEAD_FORM_ARCHIVE, 10)

    def click_modify(self):
        self.click(LeadPageLocators.LEAD_FORM_MODIFY, 10)

    def click_archive_confirmation(self):
        self.click(LeadPageLocators.ARCHIVE_CONFIRMATION, 10)

    def archive_form_creation(self):
        form = self.find(LeadPageLocators.LEAD_FORM_NAME_FOR_CREATE)

        action = ActionChains(self.driver)
        action.move_to_element(form).perform()

        self.click(LeadPageLocators.LEAD_FORM_ARCHIVE)
        self.click(LeadPageLocators.ARCHIVE_CONFIRMATION)

    def archive_form_modification(self):
        form = self.find(LeadPageLocators.LEAD_FORM_NAME_FOR_MODIFY)

        action = ActionChains(self.driver)
        action.move_to_element(form).perform()

        self.click(LeadPageLocators.LEAD_FORM_ARCHIVE)
        self.click(LeadPageLocators.ARCHIVE_CONFIRMATION)

    def fill_2_question(self, description):
        self.enter_text(LeadPageLocators.INPUT_QUESTION, description)

    def fill_2_answer_1(self, description):
        self.enter_text(LeadPageLocators.INPUT_2_ANSWER_1, description)

    def fill_2_answer_2(self, description):
        self.enter_text(LeadPageLocators.INPUT_2_ANSWER_2, description)

    def click_2_add_question_button(self):
        self.click(LeadPageLocators.BUTTON_2_ADD_QUESTION)

    def click_2_add_contact_button(self):
        self.click(LeadPageLocators.BUTTON_2_ADD_CONTACT)
    
    def click_2_bin(self):
        self.click(LeadPageLocators.BUTTON_2_BIN)

    def click_2_bin_name(self):
        self.click(LeadPageLocators.BUTTON_2_BIN_NAME)

    def click_2_bin_phone(self):
        self.click(LeadPageLocators.BUTTON_2_BIN_PHONE)

    def click_2_shablon(self):
        self.click(LeadPageLocators.BUTTON_2_SHABLON)

    def click_2_nothing_answer(self):
        self.click(LeadPageLocators.BUTTON_2_NOTHING_ANSWER)

    def click_2_answer_type(self):
        self.click(LeadPageLocators.BUTTON_2_ANSWER_TYPE)

    def click_2_free_answer(self):
        self.click(LeadPageLocators.BUTTON_2_FREE_ANSWER)

    def click_2_bin_answer(self):
        self.click(LeadPageLocators.BUTTON_2_BIN_ANSWER)

    def click_2_add_answer(self):
        self.click(LeadPageLocators.BUTTON_2_ADD_ANSWER)

    def check_error_2_question_message(self):
        error_icon = self.find(LeadPageLocators.ERROR_2_QUESTION_ICON)

        action = ActionChains(self.driver)
        action.move_to_element(error_icon).perform()

        error = self.find(LeadPageLocators.ERROR_2_QUESTION_TEXT)
        return error.text

    def check_error_2_contact_message(self):
        error = self.find(LeadPageLocators.ERROR_2_CONTACT)
        return error.text

    def check_3_answer_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_2_ANSWER_3, 10)

    def check_3_answer_not_present(self):
        return not self.is_element_present(LeadPageLocators.INPUT_2_ANSWER_3, 10)

    def check_contact_present(self):
        return self.is_element_present(LeadPageLocators.BUTTON_2_BIN_NAME, 10)

    def check_3_answer_value(self, expected_value):
        input = self.find(LeadPageLocators.INPUT_2_ANSWER_3)
        return input.get_attribute("value")

    def check_no_answer_present(self):
        return not self.is_element_present(LeadPageLocators.INPUT_2_ANSWER_1, 10)

    def click_popup_list_button(self):
        self.click(LeadPageLocators.POPUP_LIST_BUTTON)

    def click_popup_add_button(self):
        self.click(LeadPageLocators.POPUP_ADD_BUTTON)

    def check_2_popup_add_contact(self):
        return self.is_element_present(LeadPageLocators.BUTTON_2_BIN_CITY)

    def check_3_heading_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_3_HEADING, 10)

    def check_3_site_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_3_SITE, 10)

    def check_3_phone_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_3_PHONE, 10)

    def check_3_promo_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_3_PROMO, 10)

    def click_3_click_site(self):
        self.click(LeadPageLocators.BUTTON_3_SITE)

    def click_3_click_phone(self):
        self.click(LeadPageLocators.BUTTON_3_PHONE)

    def click_3_click_promo(self):
        self.click(LeadPageLocators.BUTTON_3_PROMO)

    def fill_3_heading(self, heading):
        self.enter_text(LeadPageLocators.INPUT_3_HEADING, heading)

    def clear_3_heading(self):
        heading=self.find(LeadPageLocators.INPUT_3_HEADING)
        heading.clear()

    def fill_3_description(self, description):
        self.enter_text(LeadPageLocators.INPUT_3_DESCRIPTION, description)

    def fill_3_site(self, site):
        self.enter_text(LeadPageLocators.INPUT_3_SITE, site)

    def fill_3_phone(self, phone):
        self.enter_text(LeadPageLocators.INPUT_3_PHONE, phone)

    def fill_3_promo(self, promo):
        self.enter_text(LeadPageLocators.INPUT_3_PROMO, promo)

    def check_error_3_heading_message(self):
        error = self.find(LeadPageLocators.ERROR_3_HEADING)
        return error.text

    def check_error_3_description_message(self):
        error = self.find(LeadPageLocators.ERROR_3_DESCRIPTION)
        return error.text

    def check_error_3_site_message(self):
        error = self.find(LeadPageLocators.ERROR_3_SITE)
        return error.text

    def check_error_3_phone_message(self):
        error = self.find(LeadPageLocators.ERROR_3_PHONE)
        return error.text

    def check_error_3_promo_message(self):
        error = self.find(LeadPageLocators.ERROR_3_PROMO)
        return error.text

    def check_4_button_email_present(self):
        return self.is_element_present(LeadPageLocators.BUTTON_4_EMAIL, 10)

    def check_4_input_email_notification_present(self):
        return self.is_element_present(LeadPageLocators.INPUT_4_EMAIL_FOR_NOTIFICATION, 10)

    def check_4_warning_present(self):
        return self.is_element_present(LeadPageLocators.MODAL_WARNING, 10)

    def check_draft_present(self):
        return self.is_element_present(LeadPageLocators.MODAL_DRAFT, 10)

    def click_4_click_necessary_question(self):
        self.click(LeadPageLocators.BUTTON_4_NECESSARY_QUESTIONS)

    def click_4_button_email(self):
        self.click(LeadPageLocators.BUTTON_4_EMAIL)

    def fill_4_fio(self, promo):
        self.enter_text(LeadPageLocators.INPUT_4_FIO, promo)

    def fill_4_address(self, promo):
        self.enter_text(LeadPageLocators.INPUT_4_ADDRESS, promo)

    def fill_4_email(self, promo):
        self.enter_text(LeadPageLocators.INPUT_4_EMAIL, promo)

    def fill_4_inn(self, promo):
        self.enter_text(LeadPageLocators.INPUT_4_INN, promo)

    def check_error_4_fio_message(self):
        error = self.find(LeadPageLocators.ERROR_4_FIO)
        return error.text

    def check_error_4_address_message(self):
        error = self.find(LeadPageLocators.ERROR_4_ADDRESS)
        return error.text

    def check_error_4_email_message(self):
        error = self.find(LeadPageLocators.ERROR_4_EMAIL)
        return error.text

    def check_error_4_inn_message(self):
        error = self.find(LeadPageLocators.ERROR_4_INN)
        return error.text

    