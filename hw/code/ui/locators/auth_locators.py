from selenium.webdriver.common.by import By
from hw.code.ui.locators.base_locators import BaseLocators

class AuthLocators(BaseLocators):
    LOGIN_BUTTON_LINK = (By.CLASS_NAME, 'ButtonCabinet_primary__LCfol')
    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//*[@data-test-id='oAuthService_mail_ru']")
    MAIL_RU_LOGIN = (By.NAME, 'username')
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    MAIL_RU_ANOTHER_LOGIN_BUTTON = (By.XPATH, "//*[@data-test-id='bind-screen-vkid-change-restore-type-btn']") # auth-screen-vkid-change-restore-type-btn
    MAIL_RU_SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")
    CONTINUE_VK_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and @type='submit']")
    CONTINUE_BUTTON = (By.XPATH, "//*[@data-test-id='continue-as-button']")