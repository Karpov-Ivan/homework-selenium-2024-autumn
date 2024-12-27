from selenium.webdriver.common.by import By


class BudgetPageLocators:
    TAB_BUDGET = (By.XPATH, "//span[contains(text(), 'Бюджет')]")
    BUTTON_RECHARGE = (By.CLASS_NAME, "vkuiButton__in")
    BUTTON_RECHARGE_POPUP = (By.XPATH, "//button[@type='submit' and .//span[text()='Пополнить счёт']]")

    INPUT_PAYMENT_AMOUNT = (By.NAME, "amount")
    INPUT_PAYMENT_AMOUNT_WITHOUT_VAT = (By.NAME, "amountWithoutVat")

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiTypography--normalize.vkuiFormItem__bottom.vkuiFootnote")

    TAB_BONUS_PROGRAM = (By.XPATH, "//span[contains(text(), 'Бонусная программа')]")
    ACTIVATE_PROMOCODE_BUTTON = (By.XPATH, "//button[contains(@class, 'CouponBanner_button') and .//span[text()='Активировать промокод']]")

    INPUT_PROMOCODE = (By.XPATH, "//input[@placeholder='Введите промокод']")
    BUTTON_PROMOCODE = (By.XPATH, "//button[@type='submit' and contains(@class, 'vkuiButton') and span/span[text()='Активировать']]")