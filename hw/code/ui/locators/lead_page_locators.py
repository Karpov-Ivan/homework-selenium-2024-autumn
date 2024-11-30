from selenium.webdriver.common.by import By


class LeadPageLocators:
    TAB_LEAD = (By.XPATH, "//span[contains(text(), 'Лид-формы и опросы')]")
    BUTTON_NEW = (By.CLASS_NAME, "vkuiButton__in")

    POPUP_NEW = (By.CLASS_NAME, "ModalRoot_componentWrapper__uzHTL")
    INPUT_1_NAME = (By.XPATH, "//input[@placeholder='Название компании']")
    INPUT_1_HEADING = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    INPUT_1_DESCRIPTION = (By.XPATH, "//input[@placeholder='Введите описание']")
    INPUT_1_BIG_DESCRIPTION = (By.XPATH, "//input[@placeholder='Расскажите о вашем предложении']")
    INPUT_1_AMOUNT = (By.XPATH, "(//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'])[4]")

    BUTTON_COMPACT = (By.XPATH, "//label[h4[div[span[contains(text(), 'Компактный')]]]]")
    BUTTON_MORE_TEXT = (By.XPATH, "//label[h4[div[span[contains(text(), 'Больше текста')]]]]")
    BUTTON_MAGNET = (By.XPATH, "//label[h4[div[span[contains(text(), 'Лид-магнит')]]]]")
    BUTTON_SKIDKA = (By.XPATH, "//label[div[div[span[contains(text(), 'Скидка')]]]]")
    BUTTON_BONUS = (By.XPATH, "//label[div[div[span[contains(text(), 'Бонус')]]]]")

    ERROR_1_NAME = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Название компании']]]")
    ERROR_1_HEADING = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Текст заголовка']]]")
    ERROR_1_DESCRIPTION = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите описание']]]")
    ERROR_1_BIG_DESCRIPTION = (By.XPATH, "//span[preceding-sibling::span[textarea[@placeholder='Расскажите о вашем предложении']]]")
    ERROR_1_BONUS = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Бонус']]]")
    ERROR_1_AMOUNT = (By.XPATH, "//span[preceding-sibling::div[div[span[.//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'] and position()=4]]]]")
