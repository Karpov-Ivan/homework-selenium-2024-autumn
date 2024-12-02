from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.lead_page import LeadPage
from hw.code.ui.locators.auth_locators import AuthLocators
from selenium.webdriver.support import expected_conditions as EC

class AuthPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = AuthLocators()

    def __init__(self, driver):
        self.driver = driver

    def login_lead(self, login, password):
        self.driver.get(self.url)

        self.click(self.locators.LOGIN_BUTTON_LINK, 10)
        self.click(self.locators.MAIL_RU_AUTH_BUTTON, 10)

        login_input = self.wait(10).until(EC.element_to_be_clickable(self.locators.MAIL_RU_LOGIN))
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.MAIL_RU_NEXT_BUTTON, 10)
        self.click(self.locators.MAIL_RU_ANOTHER_LOGIN_BUTTON, 10)

        password_input = self.wait(10).until(EC.element_to_be_clickable(self.locators.MAIL_RU_PASSWORD))
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON, 10)

        return LeadPage(self.driver)
    
    