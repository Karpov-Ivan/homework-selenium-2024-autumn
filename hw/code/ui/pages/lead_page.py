import time
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from ..locators.lead_page_locators import LeadPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class LeadPage(BasePage):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadPageLocators

    def __init__(self, driver):
        self.driver = driver

    def open_lead_tab(self):
        self.click(self.locators.TAB_LEAD)

    def click_new_button(self):
        self.click(LeadPageLocators.BUTTON_NEW)

    def check_popup_present(self):
        assert self.is_element_present(LeadPageLocators.POPUP_NEW), "New lead form popup not displayed"

    def click_popup_close_button(self):
        self.click(LeadPageLocators.CLOSE_BUTTON_LOCATOR)

    def check_popup_closed(self):
        time.sleep(1)
        assert not self.is_element_present(LeadPageLocators.POPUP_NEW), "New lead form popup displayed"

    def fill_1_name(self, name):
        self.enter_text(LeadPageLocators.INPUT_1_NAME, name)

    def fill_1_heading(self, heading):
        self.enter_text(LeadPageLocators.INPUT_1_HEADING, heading)

    def fill_1_description(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_DESCRIPTION, description)

    def fill_1_big_description(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_BIG_DESCRIPTION, description)

    def fill_1_bonus(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_BONUS, description)

    def fill_1_skidka(self, description):
        self.enter_text(LeadPageLocators.INPUT_1_AMOUNT, description)

    def click_1_compact_button(self):
        self.click(LeadPageLocators.BUTTON_COMPACT)

    def click_1_more_text_button(self):
        self.click(LeadPageLocators.BUTTON_MORE_TEXT)

    def click_1_magnet_button(self):
        self.click(LeadPageLocators.BUTTON_MAGNET)

    def click_1_skidka_button(self):
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
        assert self.is_element_present(LeadPageLocators.INPUT_1_HEADING), "Heading field not displayed"

    def check_big_description_present(self):
        assert self.is_element_present(LeadPageLocators.INPUT_1_BIG_DESCRIPTION), "Big description field not displayed"

    def check_skidka_present(self):
        assert self.is_element_present(LeadPageLocators.BUTTON_SKIDKA), "Bonus form not displayed"
        assert not self.is_element_present(LeadPageLocators.INPUT_1_BONUS), "Bonus field not displayed"

    def check_bonus_present(self):
        assert self.is_element_present(LeadPageLocators.INPUT_1_BONUS), "Bonus field not displayed"

    def check_error_1_name_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_1_NAME)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_1_description_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_1_DESCRIPTION)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_1_heading_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_1_HEADING)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_1_big_description_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_1_BIG_DESCRIPTION)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_1_bonus_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_1_BONUS)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_1_skidka_message_for_101(self):
        assert self.is_element_present(LeadPageLocators.ERROR_1_SKIDKA_FOR_101), "No error for more than 100 percent"

    def check_error_1_skidka_message_for_0(self):
        assert self.is_element_present(LeadPageLocators.ERROR_1_SKIDKA_FOR_0), "No error for 0 skidka"

    def check_error_1_logo_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_1_LOGO)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def switch_to_page_2(self):
        self.click(LeadPageLocators.BUTTON_LOGO)
        self.click(LeadPageLocators.ITEM_LOGO)

        time.sleep(1)

        self.fill_1_name('aa')
        self.fill_1_heading('aa')
        self.fill_1_description('aa')

        self.click_continue()

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

    def check_error_2_question_message(self, expected_message):
        error_icon = self.find(LeadPageLocators.ERROR_2_QUESTION_ICON)

        action = ActionChains(self.driver)
        action.move_to_element(error_icon).perform()

        error = self.find(LeadPageLocators.ERROR_2_QUESTION_TEXT)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_2_contact_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_2_CONTACT)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_question_closed(self):
        time.sleep(1)
        assert not self.is_element_present(LeadPageLocators.POPUP_QUESTION), "Question form popup displayed"

    def check_3_answer_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.INPUT_2_ANSWER_3), "3 answer is not displayed"

    def check_3_answer_not_present(self):
        time.sleep(1)
        assert not self.is_element_present(LeadPageLocators.INPUT_2_ANSWER_3), "3 answer is displayed"

    def check_contact_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.BUTTON_2_BIN_NAME), "Contact is not displayed"

    def check_3_answer_value(self, expected_value):
        input = self.find(LeadPageLocators.INPUT_2_ANSWER_3)
        assert input.get_attribute("value") == expected_value, f"Expected '{expected_value}', got '{input.text}'"

    def check_no_answer_present(self):
        time.sleep(1)
        assert not self.is_element_present(LeadPageLocators.INPUT_2_ANSWER_1), "3 answer is not displayed"

    def check_2_popup_opened(self):
        assert self.is_element_present(LeadPageLocators.POPUP_CONTACT), "Contact form popup not displayed"

    def click_popup_list_button(self):
        self.click(LeadPageLocators.POPUP_LIST_BUTTON)

    def click_popup_add_button(self):
        self.click(LeadPageLocators.POPUP_ADD_BUTTON)

    def check_2_popup_add_contact(self):
        assert self.is_element_present(LeadPageLocators.BUTTON_2_BIN_CITY), "Contact form popup not displayed"

    def check_3_heading_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.INPUT_3_HEADING), "Heading is not displayed"

    def check_3_site_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.INPUT_3_SITE), "Site is not displayed"

    def check_3_phone_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.INPUT_3_PHONE), "Phone is not displayed"

    def check_3_promo_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.INPUT_3_PROMO), "Promo is not displayed"

    def click_3_click_site(self):
        self.click(LeadPageLocators.BUTTON_3_SITE)

    def click_3_click_phone(self):
        self.click(LeadPageLocators.BUTTON_3_PHONE)

    def click_3_click_promo(self):
        self.click(LeadPageLocators.BUTTON_3_PROMO)

    def fill_3_heading(self, heading):
        self.enter_text(LeadPageLocators.INPUT_3_HEADING, heading)

    def fill_3_heading_alt(self, heading):
        self.enter_text(LeadPageLocators.INPUT_3_HEADING_ALT, heading)
        time.sleep(1)

    def clear_3_heading(self):
        heading=self.find(LeadPageLocators.INPUT_3_HEADING)
        heading.clear()

    def fill_3_description(self, description):
        self.enter_text(LeadPageLocators.INPUT_3_DESCRIPTION, description)

    def fill_3_site(self, site):
        self.enter_text(LeadPageLocators.INPUT_3_SITE, site)
        time.sleep(1)

    def fill_3_phone(self, phone):
        self.enter_text(LeadPageLocators.INPUT_3_PHONE, phone)
        time.sleep(1)

    def fill_3_promo(self, promo):
        self.enter_text(LeadPageLocators.INPUT_3_PROMO, promo)

    def check_error_3_heading_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_3_HEADING)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_3_description_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_3_DESCRIPTION)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_3_site_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_3_SITE)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_3_phone_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_3_PHONE)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_3_promo_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_3_PROMO)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_4_button_email_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.BUTTON_4_EMAIL), "Button for email notification is not displayed"

    def check_4_input_email_notification_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.INPUT_4_EMAIL_FOR_NOTIFICATION), "Input for email notification is not displayed"

    def check_4_modal_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.MODAL_PAGE), "Modal page is not displayed"

    def check_4_warning_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.MODAL_WARNING), "Warning is not displayed"

    def check_draft_present(self):
        time.sleep(1)
        assert self.is_element_present(LeadPageLocators.MODAL_DRAFT), "Draft is not displayed"

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

    def check_error_4_fio_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_4_FIO)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_4_address_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_4_ADDRESS)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_4_email_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_4_EMAIL)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def check_error_4_inn_message(self, expected_message):
        error = self.find(LeadPageLocators.ERROR_4_INN)
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    