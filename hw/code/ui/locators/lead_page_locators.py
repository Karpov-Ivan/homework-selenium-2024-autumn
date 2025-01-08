from selenium.webdriver.common.by import By
from string import Template
from ..config_for_lead import FORM_RECOVERMENT_NAME, FORM_ARCHIVATION_NAME, FORM_CREATION_NAME, FORM_MODIFICATION_NAME, FORM_NOT_MODIFIED

placeholder_template = Template("//input[@placeholder='${placeholder}']")
contains_text_template = Template("//span[contains(text(), '${text}')]")

class LeadPageLocators:
    TAB_LEAD = (By.XPATH, contains_text_template.substitute(text='Лид-формы и опросы'))
    BUTTON_NEW = (By.XPATH, contains_text_template.substitute(text='Создать лид-форму'))
    VK_ADS_LOGO = (By.XPATH, "//img[@alt='Logo']")

    INPUT_1_FORM_NAME = (By.XPATH, placeholder_template.substitute(placeholder='Название лид-формы'))
    INPUT_1_NAME = (By.XPATH, placeholder_template.substitute(placeholder='Название компании'))
    INPUT_1_HEADING = (By.XPATH, placeholder_template.substitute(placeholder='Текст заголовка'))
    INPUT_1_DESCRIPTION = (By.XPATH, placeholder_template.substitute(placeholder='Введите описание'))
    INPUT_1_BIG_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Расскажите о вашем предложении']")
    INPUT_1_BONUS = (By.XPATH, placeholder_template.substitute(placeholder='Бонус'))
    INPUT_1_LOGO = (By.XPATH, "//input[@accept='.jpg,.jpeg,.png,.mp4,.mpeg,.avi,.mov,video/quicktime,.zip,.mp3']")

    BUTTON_COMPACT = (By.XPATH, contains_text_template.substitute(text='Компактный'))
    BUTTON_MORE_TEXT = (By.XPATH, contains_text_template.substitute(text='Больше текста'))
    BUTTON_MAGNET = (By.XPATH, contains_text_template.substitute(text='Лид-магнит'))
    BUTTON_SKIDKA = (By.XPATH, contains_text_template.substitute(text='Скидка'))
    BUTTON_BONUS = (By.XPATH, contains_text_template.substitute(text='Бонус'))
    BUTTON_PERCENT = (By.XPATH, "//h4[contains(text(), '%')]")

    BUTTON_LOGO = (By.XPATH, contains_text_template.substitute(text='Загрузить логотип'))
    ITEM_LOGO = (By.XPATH, "//div[contains(@class, 'ImageItem_active')]")

    BUTTON_CONTINUE = (By.XPATH, "//button[@title='Продолжить']")
    BUTTON_CANCEL = (By.XPATH, contains_text_template.substitute(text='Отмена'))
    BUTTON_BACK = (By.XPATH, contains_text_template.substitute(text='Назад'))
    CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Close"]')

    BUTTON_2_ADD_QUESTION = (By.XPATH, contains_text_template.substitute(text='Добавить вопрос'))
    BUTTON_2_ADD_CONTACT = (By.XPATH, contains_text_template.substitute(text='Добавить контактные данные'))
    BUTTON_2_BIN = (By.XPATH, "//div[contains(@class, 'Question_questionHeaderRight')]")
    BUTTON_2_BIN_NAME = (By.XPATH, "//button[@data-id='first_name']")
    BUTTON_2_BIN_PHONE = (By.XPATH, "//button[@data-id='phone']")
    BUTTON_2_BIN_CITY = (By.XPATH, "//button[@data-id='city']")
    BUTTON_2_BIN_ANSWER = (By.XPATH, "//button[contains(@class, 'Answer_removeBtn')]")
    BUTTON_2_SHABLON = (By.XPATH, contains_text_template.substitute(text='Ответ из шаблона'))
    BUTTON_2_NOTHING_ANSWER = (By.XPATH, "//h5[contains(text(), '«Ничего из перечисленного»')]")
    BUTTON_2_ANSWER_TYPE = (By.XPATH, "//div[contains(text(), 'Выбор одного ответа')]")
    BUTTON_2_FREE_ANSWER = (By.XPATH, contains_text_template.substitute(text='Ответ в произвольной форме'))
    BUTTON_2_ADD_ANSWER = (By.XPATH, contains_text_template.substitute(text='Добавить ответ'))

    INPUT_QUESTION = (By.XPATH, "//textarea[@placeholder='Напишите вопрос']")

    POPUP_LIST_BUTTON = (By.XPATH, contains_text_template.substitute(text='Город'))
    POPUP_ADD_BUTTON = (By.XPATH, "//span[text()='Добавить']")

    INPUT_3_HEADING = (By.XPATH, "//input[@value='Спасибо за ответы!']")
    INPUT_3_DESCRIPTION = (By.XPATH, "//input[@value='Заявка отправлена']")
    INPUT_3_SITE = (By.XPATH, "(//input[@type='text'])[4]")
    INPUT_3_PHONE = (By.XPATH, placeholder_template.substitute(placeholder='+7......'))
    INPUT_3_PROMO = (By.XPATH, placeholder_template.substitute(placeholder='Введите промокод'))

    BUTTON_3_SITE = (By.XPATH, contains_text_template.substitute(text='Добавить сайт'))
    BUTTON_3_PHONE = (By.XPATH, contains_text_template.substitute(text='Добавить телефон'))
    BUTTON_3_PROMO = (By.XPATH, contains_text_template.substitute(text='Добавить промокод'))

    BUTTON_4_EMAIL = (By.XPATH, contains_text_template.substitute(text='Уведомлять о новых заявках по email'))
    BUTTON_4_VKMESSENGER = (By.XPATH, contains_text_template.substitute(text='Уведомлять о новых заявках в VK Messenger'))
    BUTTON_4_NECESSARY_QUESTIONS = (By.XPATH, contains_text_template.substitute(text='Обязательные вопросы'))

    INPUT_4_FIO = (By.XPATH, placeholder_template.substitute(placeholder='Введите фамилию, имя и отчество'))
    INPUT_4_ADDRESS = (By.XPATH, placeholder_template.substitute(placeholder='Введите адрес'))
    INPUT_4_EMAIL = (By.XPATH, placeholder_template.substitute(placeholder='Введите email'))
    INPUT_4_INN = (By.XPATH, placeholder_template.substitute(placeholder='Введите ИНН'))
    INPUT_4_EMAIL_FOR_NOTIFICATION = (By.XPATH, placeholder_template.substitute(placeholder='email@example.com'))

    BUTTON_SAVE = (By.XPATH, "//button[@title='Сохранить']")
    MODAL_WARNING = (By.XPATH, "//h2[contains(text(), 'Сделать все вопросы обязательными?')]")
    MODAL_DRAFT = (By.XPATH, "//h2[contains(text(), 'Сохранить черновик лид-формы?')]")

    LEAD_FORM_NAME_FOR_CREATE = (By.XPATH, f"//h5[contains(@data-testid, 'lead_form_name__{FORM_CREATION_NAME}')]")
    LEAD_FORM_NAME_FOR_ARCHIVE = (By.XPATH, f"//h5[contains(@data-testid, 'lead_form_name__{FORM_ARCHIVATION_NAME}')]")
    LEAD_FORM_NAME_FOR_MODIFY = (By.XPATH, f"//h5[contains(@data-testid, 'lead_form_name__{FORM_MODIFICATION_NAME}')]")
    LEAD_FORM_NAME_NOT_MODIFIED = (By.XPATH, f"//h5[contains(@data-testid, 'lead_form_name__{FORM_NOT_MODIFIED}')]")
    LEAD_FORM_NAME_FOR_RECOVER = (By.XPATH, f"//h5[contains(@data-testid, 'lead_form_name__{FORM_RECOVERMENT_NAME}')]")
    LEAD_FORM_MODIFY = (By.XPATH, contains_text_template.substitute(text='Редактировать'))
    LEAD_FORM_ARCHIVE = (By.XPATH, contains_text_template.substitute(text='Архивировать'))
    LEAD_FORM_RECOVER = (By.XPATH, contains_text_template.substitute(text='Восстановить'))
    ARCHIVE_CONFIRMATION = (By.XPATH, "//span[text()='Архивировать' and @class='vkuiButton__content']")
    RECOVER_CONFIRMATION = (By.XPATH, "//span[text()='Восстановить' and @class='vkuiButton__content']")

    CHOOSE_INPUT = (By.XPATH, "//input[@data-testid='select-options']")
    ARCHIVE_CHOISE = (By.XPATH, contains_text_template.substitute(text='В архиве'))
    ACTIVE_CHOISE = (By.XPATH, contains_text_template.substitute(text='Активные'))




