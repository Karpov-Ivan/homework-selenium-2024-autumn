from hw.code.ui.locators.login_page_locators import LoginPageLocators
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.budget_page import BudgetPage
from hw.code.ui.pages.lead_page import LeadPage
from hw.code.ui.pages.audience_page import AudiencePage


class LoginPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = LoginPageLocators

    def go_to_cabinet(self):
        self.click(self.locators.CABINET_BUTTON, 10)

    def click_mail(self):
        self.click(self.locators.MAIL_BUTTON, 10)

    def enter_username(self, username):
        self.enter_text(self.locators.USERNAME_INPUT, username, 10)

    def click_next_button(self):
        self.click(self.locators.NEXT_BUTTON, 10)

    def click_no_vkid_button(self):
        self.click(self.locators.NO_VKID_BUTTON, 10)

    def click_no_vkid_button_2(self):
        self.click(self.locators.NO_VKID_BUTTON_2, 10)

    def click_in_another_way_button(self):
        self.click(self.locators.OTHER_BUTTON, 10)

    def click_password_button(self):
        self.click(self.locators.PASSWORD_BUTTON, 10)

    def enter_password(self, password):
        self.enter_text(self.locators.PASSWORD_INPUT, password, 10)

    def click_continue_mail(self):
        self.click(self.locators.CONTINUE_BUTTON_MAIN, 10)

    def click_continue_mail_2(self):
        self.click(self.locators.CONTINUE_BUTTON_MAIN_2, 10)

    def login_for_budget(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_in_another_way_button()
        self.click_password_button()
        self.enter_password(password)
        self.click_continue_mail()

        return BudgetPage(self.driver)
    
    def login_for_lead(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_no_vkid_button()
        self.enter_password(password)
        self.click_continue_mail()

        return LeadPage(self.driver)

    def login_for_audience(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_no_vkid_button()
        self.enter_password(password)
        self.click_continue_mail()

        return AudiencePage(self.driver)
