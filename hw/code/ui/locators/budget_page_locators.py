from selenium.webdriver.common.by import By


class BudgetPageLocators:
    TAB_BUDGET = (By.XPATH, "//span[contains(text(), 'Бюджет')]")
    BUTTON_RECHARGE = (By.CLASS_NAME, "vkuiButton__in")
    BUTTON_RECHARGE_POPUP = (By.CSS_SELECTOR, ".CreateInvoiceModal_button__DhY5V.vkuiButton.vkuiButton--size-l.vkuiButton--mode-primary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-none.vkuiTappable.vkuiInternalTappable.vkuiTappable--hasHover.vkuiTappable--hasActive.vkui-focus-visible")

    POPUP_RECHARGE = (By.CLASS_NAME, "vkuiTitle--level-3")
    INPUT_PAYMENT_AMOUNT = (By.NAME, "amount")
    CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Закрыть"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiTypography--normalize.vkuiFormItem__bottom.vkuiFootnote")
    ICON_HELP = (By.CLASS_NAME, "Hint_hintTrigger__ixYRu")
    POPUP_HEADER = (By.XPATH, "//div[text()='Сумма к оплате']")
    POPUP_LINK = (By.XPATH, "//a[@href='https://ads.vk.com/help/articles/billing#min']")

    INPUT_PAYMENT_AMOUNT_WITHOUT_VAT = (By.NAME, "amountWithoutVat")
    ICON_HELP_2 = (By.XPATH, "(//div[@class='Hint_hintTrigger__ixYRu'])[2]")
    POPUP_HEADER_2 = (By.XPATH, "//div[text()='Сумма, поступающая на ваш счёт']")

    TAB_BONUS_PROGRAM = (By.XPATH, "//span[contains(text(), 'Бонусная программа')]")
    ACTIVATE_PROMOCODE_BUTTON = (By.XPATH, "//button[contains(@class, 'CouponBanner_button') and .//span[text()='Активировать промокод']]")
    ACTIVATED_PROMOCODES_HEADER = (By.XPATH, "//span[contains(@class, 'BonusProgram_header') and text()='Активированные промокоды']")
    PERSONAL_OFFERS_HEADER = (By.XPATH, "//span[contains(@class, 'BonusProgram_header') and text()='Персональные акции']")

    POPUP_HEADER_PROMOCODE = (By.XPATH, "//h2[contains(@class, 'ActivatePromoCodeModal_title') and text()='Активация промокода']")
    INPUT_PROMOCODE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiInput__el.vkuiText.vkuiText--sizeY-none")
    BUTTON_PROMOCODE = (By.XPATH, "//button[@type='submit' and contains(@class, 'vkuiButton') and span/span[text()='Активировать']]")
    ERROR_MESSAGE_PROMOCODE = (By.CSS_SELECTOR, ".vkuiTypography.vkuiTypography--normalize.vkuiFormItem__bottom.vkuiFootnote")