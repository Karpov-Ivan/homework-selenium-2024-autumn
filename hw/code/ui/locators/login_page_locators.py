from selenium.webdriver.common.by import By


class LoginPageLocators:
    CABINET_BUTTON = (By.CLASS_NAME, "ButtonCabinet_primary__LCfol")
    MAIL_BUTTON = (By.CSS_SELECTOR, "[data-test-id='oAuthService_mail_ru']")
    USERNAME_INPUT = (By.NAME, "username")
    NEXT_BUTTON = (By.CSS_SELECTOR, "[data-test-id='next-button']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='auth-screen-vkid-btn']")
    NO_VKID_BUTTON = (By.XPATH, "//span[text()='Войти другим способом']") #bind-screen-vkid-change-restore-type-btn
    NO_VKID_BUTTON_2 = (By.CSS_SELECTOR, "[data-test-id='auth-screen-vkid-change-restore-type-btn']")
    OTHER_BUTTON = (By.CSS_SELECTOR, "[data-test-id='other-verification-methods']")
    PASSWORD_BUTTON = (By.CSS_SELECTOR, "[data-test-id='verificationMethod_password']")
    RESERVE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='verificationMethod_reserve_code']")
    RESERVE_INPUT = (By.NAME, "otp")
    PASSWORD_INPUT = (By.NAME, "password")
    CONTINUE_BUTTON_2 = (By.XPATH, '//button[span/span/span[text()="Продолжить"]]')
    CONTINUE_BUTTON_MAIN = (By.XPATH, "//button[span[text()='Войти']]")
    CONTINUE_BUTTON_MAIN_2 = (By.XPATH, "//button[span[text()='Sign in']]")

