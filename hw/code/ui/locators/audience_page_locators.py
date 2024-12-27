from selenium.webdriver.common.by import By

class AudienceLocators:
    CREATE_AUDIENCE = (By.XPATH, "//*[@data-testid='create-audience']")
    TAB_AUDIENCE = (By.XPATH, "//*[@data-route='audience']")
    SAVE_AUDIENCE_BUTTON = (By.XPATH, '//*[@data-testid="submit"]')

    ADD_SOURCE = (By.XPATH, '//button[contains(text(), "Включить источник")]')

    KEYWORDS = (By.XPATH, "//span[text()='Ключевые фразы']")
    KEYWORDS_INPUT_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Введите фразу и нажмите Enter"]')
    INPUT_NAME_AUDIENCE = (By.CLASS_NAME, "vkuiText--sizeY-none")
    KEYWORDS_BUTTON_SAVE = (By.XPATH, '//*[@data-testid="submit"]')
    CHECK_AUDIENCE_SAVE_TITLE = (By.CLASS_NAME, "vkuiSubhead--sizeY-compact")
    OPEN_EDIT_WINDOW_BUTTON = (By.CLASS_NAME, "NameCell_wrapper")

    COMMUNITY_SUBSCRIBERS = (By.XPATH, "//span[text()='Подписчики сообществ']")
    COMMUNITY_SUBSCRIBERS_INPUT = (By.CLASS_NAME, "vkuiText--sizeY-none")
    ALL_COMMUNITY_VK = (By.CLASS_NAME, "GroupHeader_selectAll")
    CREATE_ALL_COMMUNITY_VK = (By.CLASS_NAME, "vkuiButton--size-s")
    CLICK_BODY = (By.XPATH, '//body')
    CANCEL_BUTTON = (By.CLASS_NAME, "vkuiHeadline--level-2")


    EDIT_ICON = (By.CLASS_NAME, 'vkuiIcon--write_outline_20')
    DELETE_AUDIENCE_BUTTON = (By.XPATH, '//*[@data-testid="remove-items-button"]')
    SELECT_AUDIENCE = (By.CSS_SELECTOR, "label.vkuiCheckbox > input.vkuiVisuallyHidden")
    DELETE_AUDIENCE_BUTTON_MENU_DIV = (By.CLASS_NAME, "vkuiModalPage__content-in")
    DELETE_AUDIENCE_BUTTON_IN_MENU = (By.CLASS_NAME, 'vkuiButton--mode-primary')
