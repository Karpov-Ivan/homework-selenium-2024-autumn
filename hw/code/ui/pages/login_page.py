import time

from hw.code.ui.locators.login_page_locators import LoginPageLocators
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.budget_page import BudgetPage
from hw.code.ui.pages.lead_page import LeadPage


class LoginPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = LoginPageLocators

    def go_to_cabinet(self):
        self.click(self.locators.CABINET_BUTTON)

    def click_mail(self):
        self.click(self.locators.MAIL_BUTTON)

    def enter_username(self, username):
        self.enter_text(self.locators.USERNAME_INPUT, username)

    def click_next_button(self):
        self.click(self.locators.NEXT_BUTTON)

    def click_continue_button(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_no_vkid_button(self):
        self.click(self.locators.NO_VKID_BUTTON)

    def click_in_another_way_button(self):

        self.click(self.locators.OTHER_BUTTON)

    def click_password_button(self):
        self.click(self.locators.PASSWORD_BUTTON)

    def enter_password(self, password):
        self.enter_text(self.locators.PASSWORD_INPUT, password)

    def click_continue_button_2(self):
        self.click(self.locators.CONTINUE_BUTTON_2)

    def click_continue_mail(self):
        self.click(self.locators.CONTINUE_BUTTON_MAIN)

    def login(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_continue_button()
        self.click_in_another_way_button()
        self.click_password_button()
        self.enter_password(password)
        self.click_continue_button_2()

        return BudgetPage(self.driver)
    
    def login_for_lead(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_no_vkid_button()
        #self.click_in_another_way_button()
        #self.click_password_button()
        self.enter_password(password)
        self.click_continue_mail()
        time.sleep(50)

        return LeadPage(self.driver)