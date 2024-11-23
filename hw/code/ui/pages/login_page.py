from hw.code.ui.locators.login_page_locators import LoginPageLocators
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.budget_page import BudgetPage


class LoginPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = LoginPageLocators

    def go_to_cabinet(self):
        self.click(self.locators.CABINET_BUTTON)

    def enter_login(self, login):
        self.enter_text(self.locators.LOGIN_INPUT, login)

    def click_continue_button(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def enter_password(self, password):
        self.enter_text(self.locators.PASSWORD_INPUT, password)

    def click_continue_button_2(self):
        self.click(self.locators.CONTINUE_BUTTON_2)

    def click_name(self):
        self.click(self.locators.NAME_LOCATOR)

    def login(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.enter_login(username)
        self.click_continue_button()
        self.enter_password(password)
        self.click_continue_button_2()
        self.click_name()

        return BudgetPage(self.driver)