from hw.code.ui.locators.audience_page_locators import AudienceLocators
from hw.code.ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators

    def __init__(self, driver):
        self.driver = driver

    def open_audience_tab(self):
        self.click(self.locators.TAB_AUDIENCE, 10)

    def create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE, 10)

    def checking_open_audience_creation_menu(self):
        return self.is_element_present(self.locators.AUDIENCE_CREATION_ELEMENT, 10)

    def add_source(self):
        self.click(self.locators.ADD_SOURCE, 10)

    def checking_open_add_source_menu(self):
        return self.is_element_present(self.locators.TURN_SOURCE_ELEMENT, 10)

    def keywords(self):
        self.click(self.locators.KEYWORDS, 10)

    def checking_open_keywords_menu(self):
        return self.is_element_present(self.locators.KEYWORDS_HEAD, 10)

    def checking_keywords_button_save_not_active(self):
        return self.is_enabled(self.locators.KEYWORDS_DIV_BUTTON_SAVE, 10)

    def search_period(self, period):
        search_input = self.find(self.locators.KEYWORDS_INPUT_PERIOD, 10)
        search_input.clear()
        self.send_keys_tab(search_input, period)


    def check_search_period_less_one(self):
        input_element = self.find(self.locators.KEYWORDS_INPUT_PERIOD, 10)
        value = input_element.get_attribute('value')
        return value == "1"

    def check_search_period_more_thirty(self):
        input_element = self.find(self.locators.KEYWORDS_INPUT_PERIOD, 10)
        value = input_element.get_attribute('value')
        return value == "30"

    def keywords_input(self, value):
        textarea = self.find(self.locators.KEYWORDS_INPUT_TEXTAREA)
        textarea.send_keys(value)

    def keywords_button_save(self):
        div_elements = self.driver.find_elements(self.locators.KEWORDS_BURRON_SAVE[0], self.locators.KEWORDS_BURRON_SAVE[1])
        second_div = div_elements[1]
        button = second_div.find_element(self.locators.KEYWORDS_DIV_BUTTON_SAVE[0], self.locators.KEYWORDS_DIV_BUTTON_SAVE[1])
        button.click()

    def keywords_find(self, value):
        div_elements = self.driver.find_elements(self.locators.KEYWORDS_CHECK_VALUE[0], self.locators.KEYWORDS_CHECK_VALUE[1])
        pre_last_div = div_elements[-2]
        text = pre_last_div.text
        return text == value

    def source_deletion_icon(self):
        buttons = self.driver.find_elements(self.locators.DELETE_ICON[0], self.locators.DELETE_ICON[1])
        button = buttons[-1]
        self.click_action(button)

    def source_deletion(self):
        delete_buttons = self.driver.find_elements(self.locators.DELETE_BUTTON[0], self.locators.DELETE_BUTTON[1])
        delete_button = delete_buttons[-1]
        delete_button.click()

    def check_source_deletion(self):
        elements = self.driver.find_elements(self.locators.DELETE_ICON[0], self.locators.DELETE_ICON[1])
        if len(elements) != 0:
            return False
        return True

    def source_edit_icon(self):
        buttons = self.driver.find_elements(self.locators.EDIT_ICON[0], self.locators.EDIT_ICON[1])
        print(len(buttons))
        button = buttons[-1]
        self.click_action(button)

    def find_value_keywords(self, value):
        textarea = self.find(self.locators.KEYWORDS_INPUT_TEXTAREA)
        return value in textarea.text

    def create_audience_click_cross_button_check_visibility(self):
        return self.find_with_visibility_of_element_located(self.locators.CROSS_BUTTON, 10)

    def create_audience_click_cross_button(self):
        button = self.driver.find_element(self.locators.CROSS_BUTTON[0], self.locators.CROSS_BUTTON[1])
        button.click()

    def check_abort_creation_window(self):
        return self.find(self.locators.CROSS_MENU)

    def abort_audience_creation_click(self):
        button = self.driver.find_element(self.locators.ABORT_MENU_BUTTON[0], self.locators.ABORT_MENU_BUTTON[1])
        button.click()

    def save_audience_check_visibility(self):
        return self.find_with_visibility_of_element_located(self.locators.SAVE_AUDIENCE_BUTTON, 10)

    def save_audience(self):
        button = self.driver.find_element(self.locators.SAVE_AUDIENCE_BUTTON[0], self.locators.SAVE_AUDIENCE_BUTTON[1])
        button.click()

    def check_inactive_share(self):
        return not self.is_enabled(self.locators.SHARING_AUDIENCE_BUTTON, 10)

    def check_inactive_delete(self):
        return not self.is_enabled(self.locators.DELETE_AUDIENCE_BUTTON, 10)

    def selected_audiece(self):
        checkboxs = self.driver.find_elements(self.locators.SHARING_AUDIENCE[0], self.locators.SHARING_AUDIENCE[1])
        checkbox = checkboxs[-1]
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def share_audience_check_visibility(self):
        return self.find_with_visibility_of_element_located(self.locators.SHARING_AUDIENCE_BUTTON, 10)

    def share_audience(self):
        button = self.driver.find_element(self.locators.SHARING_AUDIENCE_BUTTON[0], self.locators.SHARING_AUDIENCE_BUTTON[1])
        button.click()


    def checking_share_window(self):
        return self.find(self.locators.SHARING_AUDIENCE_HEAD)

    def delete_audience_check_visibility(self):
        return self.find_with_visibility_of_element_located(self.locators.DELETE_AUDIENCE_BUTTON, 10)

    def delete_audience(self):
        button = self.driver.find_element(self.locators.DELETE_AUDIENCE_BUTTON[0],self.locators.DELETE_AUDIENCE_BUTTON[1])
        button.click()

    def checking_delete_window(self):
        return self.find(self.locators.DELETE_AUDIENCE_WINDOW)

    def delete_audience_click(self):
        second_button = self.driver.find_element(self.locators.DELETE_AUDIENCE_BUTTON_MENU[0], self.locators.DELETE_AUDIENCE_BUTTON_MENU[1])
        second_button.click()

    def open_lists_users(self):
        self.click(self.locators.LISTS_USERS)

    def download_list(self):
        self.click(self.locators.DOWNLOAD_LIST)

    def check_download_list_check_visibility(self):
        return self.find_with_visibility_of_element_located(self.locators.DOWNLOAD_HEAD, 10)

    def check_download_list(self):
        elem = self.find(self.locators.DOWNLOAD_HEAD, 10)
        return elem.text == "Загрузить список"

    def open_offline_conversions(self):
        self.click(self.locators.OFFLINE_CONVERSIONS)

    def check_offline_conversions_check_visibility(self):
        return self.find_with_visibility_of_element_located(self.locators.DOWNLOAD_HEAD, 10)

    def check_offline_conversions(self):
        elem = self.find(self.locators.DOWNLOAD_HEAD)
        return elem.text == "Загрузить список пользователей"

