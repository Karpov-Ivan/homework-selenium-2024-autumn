from selenium.webdriver.common.by import By


class BudgetPageLocators:
    TAB_BUDGET = (By.XPATH, "//span[contains(text(), 'Бюджет')]")
    BUTTON_RECHARGE = (By.CLASS_NAME, "vkuiButton__in")

    POPUP_RECHARGE = (By.CLASS_NAME, "vkuiTitle--level-3")
    INPUT_PAYMENT_AMOUNT = (By.NAME, "amount")
    CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Закрыть"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiTypography--normalize.vkuiFormItem__bottom.vkuiFootnote")
    ICON_HELP = (By.CLASS_NAME, "Hint_hintTrigger__ixYRu")
    POPUP_HEADER = (By.XPATH, "//div[text()='Сумма к оплате']")
    POPUP_LINK = (By.XPATH, "//a[@href='https://ads.vk.com/help/articles/billing#min']")