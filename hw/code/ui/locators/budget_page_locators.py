from selenium.webdriver.common.by import By


class BudgetPageLocators:
    TAB_BUDGET = (By.XPATH, "//span[contains(text(), 'Бюджет')]")
    BUTTON_RECHARGE = (By.CLASS_NAME, "vkuiButton__in")
    BUTTON_RECHARGE_POPUP = (By.CSS_SELECTOR, ".CreateInvoiceModal_button__DhY5V.vkuiButton.vkuiButton--size-l.vkuiButton--mode-primary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-none.vkuiTappable.vkuiInternalTappable.vkuiTappable--hasHover.vkuiTappable--hasActive.vkui-focus-visible")

    INPUT_PAYMENT_AMOUNT = (By.NAME, "amount")
    INPUT_PAYMENT_AMOUNT_WITHOUT_VAT = (By.NAME, "amountWithoutVat")

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiTypography--normalize.vkuiFormItem__bottom.vkuiFootnote")

    TAB_BONUS_PROGRAM = (By.XPATH, "//span[contains(text(), 'Бонусная программа')]")
    ACTIVATE_PROMOCODE_BUTTON = (By.XPATH, "//button[contains(@class, 'CouponBanner_button') and .//span[text()='Активировать промокод']]")

    INPUT_PROMOCODE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiInput__el.vkuiText.vkuiText--sizeY-none")
    BUTTON_PROMOCODE = (By.XPATH, "//button[@type='submit' and contains(@class, 'vkuiButton') and span/span[text()='Активировать']]")