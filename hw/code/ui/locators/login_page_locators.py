from selenium.webdriver.common.by import By


class LoginPageLocators:
    CABINET_BUTTON = (By.CLASS_NAME, "ButtonCabinet_primary__LCfol")
    LOGIN_INPUT = (By.NAME, "login")
    CONTINUE_BUTTON = (By.XPATH, "//span[contains(text(), 'Продолжить')]")
    DIFFERENT_BUTTON = (By.XPATH, "//span[contains(text(), 'Подтвердить другим способом')]")
    PASSWORD_BUTTON = (By.XPATH, "//span[contains(text(), 'Пароль')]")
    PASSWORD_INPUT = (By.NAME, "password")
    CONTINUE_BUTTON_2 = (By.XPATH, "//button[contains(@class, 'vkuiButton') and @type='submit']")
    NAME_LOCATOR = (By.CLASS_NAME, "vkuiSimpleCell__middle")
