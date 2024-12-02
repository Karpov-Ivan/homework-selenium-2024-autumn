from hw.code.ui.locators.audience_locators import AudienceLocators
from hw.code.ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = "https://ads.vk.com/"
    locators = AudienceLocators

    def __init__(self, driver):
        self.driver = driver

    def open_audience_tab(self):
        self.click(self.locators.TAB_AUDIENCE)

    def create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE)

    def checking_open_audience_creation_menu(self):
        assert self.check_presence_element(self.locators.AUDIENCE_CREATION_ELEMENT), "Audience creation menu is not displayed"

    def add_source(self):
        self.click(self.locators.ADD_SOURCE)

    def checking_open_add_source_menu(self):
        assert self.check_presence_element(self.locators.TURN_SOURCE_ELEMENT), "Power on menu of the source is not displayed"

    def keywords(self):
        self.click(self.locators.KEYWORDS)

    def checking_open_keywords_menu(self):
        assert self.check_presence_element(self.locators.KEYWORDS_HEAD), "Keywords menu is not displayed"

    def checking_keywords_button_save_not_active(self):
        elem = self.find(self.locators.KEYWORDS_DIV_BUTTON).find_element(self.locators.KEYWORDS_DIV_BUTTON_SAVE[0], self.locators.KEYWORDS_DIV_BUTTON_SAVE[1]), "Button turned out to be active, while it should be inactive"
        assert not elem.is_enabled(), "Button is active and should not be active"

    def search_period_less_one(self, period):
        search_input = self.find(self.locators.KEYWORDS_INPUT_PERIOD)
        search_input.send_keys(period)

    def check_search_period_less_one(self):
        assert self.find(self.locators.CORRECTED_PERIOD_LESS_ONE) == 1, "Period is not equal to 1"

    def search_period_more_thirty(self, period):
        search_input = self.find(self.locators.CORRECTED_PERIOD_LESS_ONE)
        search_input.send_keys(period)

    def check_search_period_more_thirty(self):
        assert self.find(self.locators.CORRECTED_PERIOD_MORE_THIRTY) == 30, "Period is not equal to 30"

    def keywords_button_cancellation(self):
        modal_footer = self.find(self.locators.KEYWORDS_DIV_BUTTON).find_element(self.locators.KEYWORDS_DIV_BUTTON_CANCELLATION[0],self.locators.KEYWORDS_DIV_BUTTON_CANCELLATION[1])
        modal_footer.click()

    def keywords_input(self, value):
        textareas = self.find(self.locators.KEYWORDS_INPUT).find_element(self.locators.KEYWORDS_INPUT_TEXTAREA[0],self.locators.KEYWORDS_INPUT_TEXTAREA[1])
        first_textarea = textareas[0]
        first_textarea.send_keys(value)

    def keywords_button_save(self):
        save_button = self.find(self.locators.KEYWORDS_DIV_BUTTON).find_element(self.locators.KEYWORDS_DIV_BUTTON_SAVE[0], self.locators.KEYWORDS_DIV_BUTTON_SAVE[1])
        save_button.click()

    def keywords_find(self, value):
        key_phrases_elements = self.find(self.locators.KEYWORDS_CHECK_VALUE)
        found = False
        for element in key_phrases_elements:
            if value in element.text:
                found = True
                break

        assert found, f"The keyword is '{value}' not found"

    def source_deletion_icon(self):
        elements = self.find(self.locators.LIST_ADD_SOURCES).find_elements(self.locators.DELETE_ICON[0], self.locators.DELETE_ICON[1])
        element = elements[-1]
        element.click()

    def source_deletion(self):
        self.click(self.locators.DELETE_BUTTON)

    def source_edit_icon(self):
        elements = self.find(self.locators.LIST_ADD_SOURCES).find_elements(self.locators.EDIT_ICON[0], self.locators.EDIT_ICON[1])
        element = elements[-1]
        element.click()

    def find_value_keywords(self, value):
        textareas = self.find(self.locators.KEYWORDS_INPUT).find_element(self.locators.KEYWORDS_INPUT_TEXTAREA[0], self.locators.KEYWORDS_INPUT_TEXTAREA[1])
        first_textarea = textareas[0].text
        assert value in first_textarea, f"there is no meaning in the keywords '{value}'"

    def create_audience_click_cross_button(self):
        self.click(self.locators.CROSS_BUTTON)

    def check_abort_creation_window(self):
        assert self.find(self.locators.CROSS_MENU)

    def abort_audience_creation_click(self):
        element = self.find(self.locators.ABORT_MENU).find_elements(self.locators.ABORT_MENU_BUTTON[0],self.locators.ABORT_MENU_BUTTON[1])
        element.click()

    def save_audience(self):
        element = self.find(self.locators.SAVE_AUDIENCE).find_elements(self.locators.SAVE_AUDIENCE_BUTTTON[0],self.locators.SAVE_AUDIENCE_BUTTTON[1])
        element.click()

    def check_inactive_share(self):
        elem = self.find(self.locators.SHARING_AUDIENCE_BUTTON)
        assert not elem.is_enabled(), "Button is active and should not be active"

    def check_inactive_delete(self):
        elem = self.find(self.locators.DELETE_AUDIENCE_BUTTON)
        assert not elem.is_enabled(), "Button is active and should not be active"

    def share_audience(self):
        checkboxs = self.driver.find_element(self.locators.SHARING_AUDIENCE[0], self.locators.SHARING_AUDIENCE[1])
        checkbox = checkboxs[1]
        checkbox.click()
        elem = self.find(self.locators.SHARING_AUDIENCE_BUTTON)
        elem.click()

    def checking_share_window(self):
        assert self.find(self.locators.SHARING_DELETE_WINDOW), "There is no given title in the menu or the menu has not opened"

    def delete_audience(self):
        checkboxs = self.driver.find_element(self.locators.DELETE_AUDIENCE[0], self.locators.DELETE_AUDIENCE[1])
        checkbox = checkboxs[1]
        checkbox.click()
        elem = self.find(self.locators.DELETE_AUDIENCE_BUTTON)
        elem.click()

    def checking_delete_window(self):
        assert self.find(self.locators.SHARING_DELETE_WINDOW), "There is no given title in the menu or the menu has not opened"

    def delete_audience_click(self):
        menu_button = self.find(self.locators.DELETE_AUDIENCE_BUTTON_MENU).find_element(self.locators.DELETE_AUDIENCE_BUTTON_IN_MENU[0], self.locators.DELETE_AUDIENCE_BUTTON_IN_MENU[1])
        menu_button.click()

    def open_lists_users(self):
        self.click(self.locators.LISTS_USERS)

    def download_list(self):
        self.click(self.locators.DOWNLOAD_LIST)

    def check_download_list(self):
        elem = self.find(self.locators.DOWNLOAD_HEAD)
        assert elem.text == "Загрузить список", "The user list download menu did not open"

    def open_offline_conversions(self):
        self.click(self.locators.OFFLINE_CONVERSIONS)

    def check_offline_conversions(self):
        elem = self.find(self.locators.DOWNLOAD_HEAD)
        assert elem.text == "Загрузить список пользователей", "The menu for downloading the list of users in the offline conference did not open"

