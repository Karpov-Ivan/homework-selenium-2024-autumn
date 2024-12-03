from selenium.webdriver.common.by import By


class LeadPageLocators:
    TAB_LEAD = (By.XPATH, "//span[contains(text(), 'Лид-формы и опросы')]")
    BUTTON_NEW = (By.CLASS_NAME, "vkuiButton__in")
    VK_ADS_LOGO = (By.XPATH, "//img[@alt='Logo']")

    POPUP_NEW = (By.CLASS_NAME, "ModalRoot_componentWrapper__uzHTL")
    INPUT_1_NAME = (By.XPATH, "//input[@placeholder='Название компании']")
    INPUT_1_HEADING = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    INPUT_1_DESCRIPTION = (By.XPATH, "//input[@placeholder='Введите описание']")
    INPUT_1_BIG_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Расскажите о вашем предложении']")
    INPUT_1_4 = (By.XPATH, "(//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'])[4]")
    INPUT_1_AMOUNT = (By.XPATH, "//input[@value='500']")
    INPUT_1_BONUS = (By.XPATH, "//input[@placeholder='Бонус']")
    INPUT_1_LOGO = (By.XPATH, "//input[@accept='.jpg,.jpeg,.png,.mp4,.mpeg,.avi,.mov,video/quicktime,.zip,.mp3']")

    BUTTON_COMPACT = (By.XPATH, "//label[h4[div[span[contains(text(), 'Компактный')]]]]")
    BUTTON_MORE_TEXT = (By.XPATH, "//label[h4[div[span[contains(text(), 'Больше текста')]]]]")
    BUTTON_MAGNET = (By.XPATH, "//label[h4[div[span[contains(text(), 'Лид-магнит')]]]]")
    BUTTON_SKIDKA = (By.XPATH, "//label[div[div[div[span[contains(text(), 'Скидка')]]]]]")
    BUTTON_BONUS = (By.XPATH, "//label[div[div[div[span[contains(text(), 'Бонус')]]]]]")
    BUTTON_PERCENT = (By.XPATH, "//h4[contains(text(), '%')]")

    BUTTON_LOGO = (By.XPATH, "//div[@class='vkuiSimpleCell vkuiSimpleCell--sizeY-none vkuiCellButton vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']")
    ITEM_LOGO = (By.XPATH, "//div[@class='ImageItem_imageItem__WiiIG ImageItem_active__1fy0f']")

    BUTTON_CONTINUE = (By.XPATH, "//button[@title='Продолжить']")
    BUTTON_CANCEL = (By.XPATH, "//span[contains(text(), 'Отмена')]")
    BUTTON_BACK = (By.XPATH, "//span[contains(text(), 'Назад')]")
    CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Close"]')

    ERROR_1_NAME = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Название компании']]]")
    ERROR_1_HEADING = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Текст заголовка']]]")
    ERROR_1_DESCRIPTION = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите описание']]]")
    ERROR_1_BIG_DESCRIPTION = (By.XPATH, "//span[preceding-sibling::span[textarea[@placeholder='Расскажите о вашем предложении']]]")
    ERROR_1_BONUS = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Бонус']]]")
    ERROR_1_LOGO = (By.XPATH, "//span[preceding-sibling::div[@class='vkuiSimpleCell vkuiSimpleCell--sizeY-none vkuiCellButton vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']]")
    ERROR_1_SKIDKA_FOR_101 = (By.XPATH, "//div[contains(text(), 'Укажите скидку не больше 100%')]")
    ERROR_1_SKIDKA_FOR_0 = (By.XPATH, "//div[contains(text(), 'Значение должно быть больше нуля')]")

    POPUP_QUESTION = (By.XPATH, "Questions_questionsDroppable__ha76F")

    BUTTON_2_ADD_QUESTION = (By.XPATH, "//span[contains(text(), 'Добавить вопрос')]")
    BUTTON_2_ADD_CONTACT = (By.XPATH, "//span[contains(text(), 'Добавить контактные данные')]")
    BUTTON_2_BIN = (By.XPATH, "//div[@class='Question_questionHeaderRight__h2kGw']")
    BUTTON_2_BIN_NAME = (By.XPATH, "//button[@data-id='first_name']")
    BUTTON_2_BIN_PHONE = (By.XPATH, "//button[@data-id='phone']")
    BUTTON_2_BIN_CITY = (By.XPATH, "//button[@data-id='city']")
    BUTTON_2_BIN_ANSWER = (By.XPATH, "//button[@class='vkuiIconButton vkuiIconButton--sizeY-none Answer_removeBtn__brkWX vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']")
    BUTTON_2_SHABLON = (By.XPATH, "//span[contains(text(), 'Ответ из шаблона')]")
    BUTTON_2_NOTHING_ANSWER = (By.XPATH, "//h5[contains(text(), '«Ничего из перечисленного»')]")
    BUTTON_2_ANSWER_TYPE = (By.XPATH, "//div[contains(text(), 'Выбор одного ответа')]")
    BUTTON_2_FREE_ANSWER = (By.XPATH, "//span[contains(text(), 'Ответ в произвольной форме')]")
    BUTTON_2_ADD_ANSWER = (By.XPATH, "//span[contains(text(), 'Добавить ответ')]")

    ERROR_2_QUESTION_ICON = (By.XPATH, "//div[@class='Hint_hintTrigger__ixYRu Question_errorIconWrap__0UsDI']")
    ERROR_2_QUESTION_TEXT = (By.XPATH, "//div[@class='Tooltip_tooltipContainer__P1b-O']")
    ERROR_2_CONTACT = (By.XPATH, "(//p[@class='vkuiTypography vkuiTypography--normalize vkuiBanner__text vkuiText vkuiText--sizeY-none'])[2]")

    INPUT_QUESTION = (By.XPATH, "//textarea[@placeholder='Напишите вопрос']")
    INPUT_2_ANSWER_1 = (By.XPATH, "(//input[@placeholder='Введите ответ'])[1]")
    INPUT_2_ANSWER_2 = (By.XPATH, "(//input[@placeholder='Введите ответ'])[2]")
    INPUT_2_ANSWER_3 = (By.XPATH, "(//input[@placeholder='Введите ответ'])[3]")

    POPUP_CONTACT = (By.XPATH, "//div[@class='vkuiModalPage__in']")
    POPUP_LIST_BUTTON = (By.XPATH, "//span[contains(text(), 'Город')]")
    POPUP_ADD_BUTTON = (By.XPATH, "//span[text()='Добавить']")

    INPUT_3_HEADING = (By.XPATH, "//input[@value='Спасибо за ответы!']")
    INPUT_3_HEADING_ALT = (By.XPATH, "(//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'])[1]")
    INPUT_3_DESCRIPTION = (By.XPATH, "//input[@value='Заявка отправлена']")
    INPUT_3_SITE = (By.XPATH, "(//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'])[3]")
    INPUT_3_PHONE = (By.XPATH, "//input[@placeholder='+7......']")
    INPUT_3_PROMO = (By.XPATH, "//input[@placeholder='Введите промокод']")

    BUTTON_3_SITE = (By.XPATH, "//span[contains(text(), 'Добавить сайт')]")
    BUTTON_3_PHONE = (By.XPATH, "//span[contains(text(), 'Добавить телефон')]")
    BUTTON_3_PROMO = (By.XPATH, "//span[contains(text(), 'Добавить промокод')]")

    ERROR_3_HEADING = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[1]")
    ERROR_3_DESCRIPTION = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[2]")
    ERROR_3_SITE = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[3]")
    ERROR_3_PHONE = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[4]")
    ERROR_3_PROMO = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[5]")

    BUTTON_4_EMAIL = (By.XPATH, "//span[contains(text(), 'Уведомлять о новых заявках по email')]")
    BUTTON_4_VKMESSENGER = (By.XPATH, "//span[contains(text(), 'Уведомлять о новых заявках в VK Messenger')]")
    BUTTON_4_NECESSARY_QUESTIONS = (By.XPATH, "//span[contains(text(), 'Обязательные вопросы')]")

    INPUT_4_FIO = (By.XPATH, "//input[@placeholder='Введите фамилию, имя и отчество']")
    INPUT_4_ADDRESS = (By.XPATH, "//input[@placeholder='Введите адрес']")
    INPUT_4_EMAIL = (By.XPATH, "//input[@placeholder='Введите email']")
    INPUT_4_INN = (By.XPATH, "//input[@placeholder='Введите ИНН']")
    INPUT_4_EMAIL_FOR_NOTIFICATION = (By.XPATH, "//input[@placeholder='email@example.com']")
    
    ERROR_4_FIO = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите фамилию, имя и отчество']]]")
    ERROR_4_ADDRESS = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите адрес']]]")
    ERROR_4_EMAIL = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите email']]]")
    ERROR_4_INN = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите ИНН']]]")
    ERROR_4_EMAIL_FOR_NOTIFICATION = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='email@example.com']]]")

    BUTTON_SAVE = (By.XPATH, "//button[@title='Сохранить']")
    MODAL_PAGE = (By.XPATH, "//div[@class='vkuiModalPage vkuiModalPage--desktop vkuiInternalModalPage--sizeX-regular vkuiModalPage--size-s ModalManagerPage_auto__5nb+P ModalManagerPage_withoutCloser__j8RcY']")
    MODAL_WARNING = (By.XPATH, "//h2[contains(text(), 'Сделать все вопросы обязательными?')]")
    MODAL_DRAFT = (By.XPATH, "//h2[contains(text(), 'Сохранить черновик лид-формы?')]")




