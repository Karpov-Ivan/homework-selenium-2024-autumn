from selenium.webdriver.common.by import By


class BudgetPageLocators:
    TAB_BUDGET = (By.XPATH, "//span[contains(text(), 'Бюджет')]")
    BUTTON_RECHARGE = (By.CLASS_NAME, "vkuiButton__in")
    BUTTON_RECHARGE_POPUP = (By.XPATH, "//button[@type='submit' and .//span[text()='Пополнить счёт']]")

    INPUT_PAYMENT_AMOUNT = (By.NAME, "amount")
    INPUT_PAYMENT_AMOUNT_WITHOUT_VAT = (By.NAME, "amountWithoutVat")

    ERROR_MESSAGE_MIN_VALUE = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and contains(text(), "Минимальная сумма 600,00 ₽")]')
    ERROR_MESSAGE_MAX_VALUE = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and contains(text(), "уменьшите сумму")]')
    ERROR_MESSAGE_PROMOCODE = (By.XPATH, '//span[contains(@class, "vkuiFormItem__bottom") and contains(text(), "Промокод не может быть активирован")]')

    TAB_BONUS_PROGRAM = (By.XPATH, "//span[contains(text(), 'Бонусная программа')]")
    ACTIVATE_PROMOCODE_BUTTON = (By.XPATH, "//button[contains(@class, 'CouponBanner_button') and .//span[text()='Активировать промокод']]")

    INPUT_PROMOCODE = (By.XPATH, "//input[@placeholder='Введите промокод']")
    BUTTON_PROMOCODE = (By.XPATH, "//button[@type='submit' and contains(@class, 'vkuiButton') and span/span[text()='Активировать']]")