import time
import math
from hw.code.ui.locators.audience_page_locators import AudienceLocators
from hw.code.ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators

    def __init__(self, driver):
        self.driver = driver

    def create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE, 10)

    def add_source(self):
        self.click(self.locators.ADD_SOURCE, 10)

    def keywords(self):
        self.click(self.locators.KEYWORDS, 10)

    def keywords_input(self, value):
        textarea = self.find(self.locators.KEYWORDS_INPUT_TEXTAREA, 10)
        textarea.send_keys(value)

    def keywords_button_save(self):
        self.presence_of_all_elements_located(self.locators.KEWORDS_BURRON_SAVE, 10)
        div_elements = self.driver.find_elements(self.locators.KEWORDS_BURRON_SAVE[0], self.locators.KEWORDS_BURRON_SAVE[1])
        second_div = div_elements[1]
        button = second_div.find_element(self.locators.KEYWORDS_DIV_BUTTON_SAVE[0], self.locators.KEYWORDS_DIV_BUTTON_SAVE[1])
        button.click()

    def input_name_audience(self, name):
        title_input = self.find(self.locators.INPUT_NAME_AUDIENCE, 10)
        self.element_to_be_clickable(self.locators.INPUT_NAME_AUDIENCE, 10)
        title_input.clear()
        title_input.send_keys(name)

    def check_audience_save(self):
        self.presence_of_all_elements_located(self.locators.CHECK_AUDIENCE_SAVE_TITLE, 10)
        titles = self.driver.find_elements(self.locators.CHECK_AUDIENCE_SAVE_TITLE[0], self.locators.CHECK_AUDIENCE_SAVE_TITLE[1])
        return titles[math.floor(len(titles) / 2)].text

    def check_audience_delete(self, name):
        self.presence_of_all_elements_located(self.locators.CHECK_AUDIENCE_SAVE_TITLE, 10)
        titles = self.driver.find_elements(self.locators.CHECK_AUDIENCE_SAVE_TITLE[0], self.locators.CHECK_AUDIENCE_SAVE_TITLE[1])
        for i in range(len(titles)):
            if titles[i].text == name:
                return False

        return True

    def open_edit_menu_button(self):
        button = self.driver.find_element(self.locators.OPEN_EDIT_WINDOW_BUTTON[0], self.locators.OPEN_EDIT_WINDOW_BUTTON[1])
        self.click_action(button)

    def keywords_edit_input(self, new_value):
        input = self.find_with_visibility_of_element_located(self.locators.KEYWORDS_INPUT_TEXTAREA, 10)
        input.clear()
        input.send_keys(new_value)

    def click_edit_icon(self):
        self.element_to_be_clickable(self.locators.EDIT_ICON, 10)
        buttons = self.driver.find_elements(self.locators.EDIT_ICON[0], self.locators.EDIT_ICON[1])
        button = buttons[-1]
        self.click_action(button)

    def community_subscribers(self):
        self.click(self.locators.COMMUNITY_SUBSCRIBERS, 10)

    def community_subscribers_input(self, community):
        self.presence_of_all_elements_located(self.locators.COMMUNITY_SUBSCRIBERS_INPUT, 10)
        inputs = self.driver.find_elements(self.locators.COMMUNITY_SUBSCRIBERS_INPUT[0], self.locators.COMMUNITY_SUBSCRIBERS_INPUT[1])
        input = inputs[1]
        input.send_keys(community)

    def all_community_vk(self):
        self.click(self.locators.ALL_COMMUNITY_VK, 10)

    def create_all_community_vk_list(self):
        self.element_to_be_clickable(self.locators.CREATE_ALL_COMMUNITY_VK, 10)
        self.click(self.locators.CREATE_ALL_COMMUNITY_VK, 10)
        self.element_to_be_clickable(self.locators.CLICK_BODY, 10)
        self.click(self.locators.CLICK_BODY, 10)

    def community_subscribers_button_save(self):
        self.presence_of_all_elements_located(self.locators.KEWORDS_BURRON_SAVE, 10)
        div_elements = self.driver.find_elements(self.locators.KEWORDS_BURRON_SAVE[0],self.locators.KEWORDS_BURRON_SAVE[1])
        second_div = div_elements[1]
        button = second_div.find_element(self.locators.KEYWORDS_DIV_BUTTON_SAVE[0],self.locators.KEYWORDS_DIV_BUTTON_SAVE[1])
        button.click()

    def community_subscribers_edit_input(self):
        self.presence_of_all_elements_located(self.locators.CANCEL_BUTTON, 10)
        headers = self.driver.find_elements(self.locators.CANCEL_BUTTON[0], self.locators.CANCEL_BUTTON[1])
        header = headers[1]
        header.click()

    def save_audience(self):
        self.click(self.locators.SAVE_AUDIENCE_BUTTON, 10)

    def selected_audiece(self):
        checkboxs = self.driver.find_elements(self.locators.SELECT_AUDIENCE[0], self.locators.SELECT_AUDIENCE[1])
        checkbox = checkboxs[-1]
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def open_delete_audience_menu(self):
        self.click(self.locators.DELETE_AUDIENCE_BUTTON, 10)

    def delete_audience_click(self):
        div = self.driver.find_element(self.locators.DELETE_AUDIENCE_BUTTON_MENU_DIV[0], self.locators.DELETE_AUDIENCE_BUTTON_MENU_DIV[1])
        button = div.find_element(self.locators.DELETE_AUDIENCE_BUTTON_IN_MENU[0], self.locators.DELETE_AUDIENCE_BUTTON_IN_MENU[1])
        button.click()
