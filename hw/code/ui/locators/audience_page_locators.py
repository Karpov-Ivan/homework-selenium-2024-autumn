from selenium.webdriver.common.by import By

class AudienceLocators:
    TAB_AUDIENCE = (By.XPATH, "//*[@data-route='audience']")
    CREATE_AUDIENCE = (By.XPATH, "//*[@data-testid='create-audience']")
    AUDIENCE_CREATION_ELEMENT = (By.CLASS_NAME, "vkuiTitle--level-2") # (By.XPATH, "//h2[text()='Создание аудитории']")
    SAVE_AUDIENCE = (By.CLASS_NAME, "ModalFooterSimple_container__rteom")
    SAVE_AUDIENCE_BUTTTON = (By.CLASS_NAME, "vkuiButton--mode-primary")

    ADD_SOURCE = (By.CLASS_NAME, "vkuiButton--stretched")
    TURN_SOURCE_ELEMENT = (By.CLASS_NAME, "vkuiTitle--level-2") # (By.XPATH, "//h2[text()='Включить источник']")

    KEYWORDS = (By.XPATH, "//span[text()='Ключевые фразы']")
    KEYWORDS_HEAD = (By.CLASS_NAME, "vkuiTitle--level-2") # (By.XPATH, "//h2[text()='Ключевые фразы']")
    KEYWORDS_DIV_BUTTON = (By.CLASS_NAME, "ModalFooterSimple_container__rteom")
    KEYWORDS_DIV_BUTTON_SAVE = (By.CLASS_NAME, "vkuiButton--mode-primary")
    KEYWORDS_DIV_BUTTON_CANCELLATION = (By.CLASS_NAME, "vkuiButton--mode-secondary")
    KEYWORDS_INPUT = (By.CSS_SELECTOR, 'div.ModalSidebarPage_content__2mBu8')
    KEYWORDS_INPUT_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Введите фразу и нажмите Enter"]')
    KEYWORDS_CHECK_VALUE = (By.CSS_SELECTOR, 'div.InfoRow_content__LN5Bb')
    KEYWORDS_INPUT_PERIOD = (By.XPATH, '//input[@value="12"]')
    CORRECTED_PERIOD_LESS_ONE = (By.XPATH, '//input[@value="1"]')
    CORRECTED_PERIOD_MORE_THIRTY = (By.XPATH, '//input[@value="30"]')

    LIST_ADD_SOURCES = (By.CLASS_NAME, 'CreateSegmentModal_content__Q5QuZ')
    DELETE_ICON = (By.CSS_SELECTOR, 'svg.vkuiIcon--delete_outline_20.Header_delete__aQ32O')
    DELETE_WINDOW = (By.CLASS_NAME, 'ModalConfirm_wrapper__hdfG4')
    DELETE_BUTTON = (By.CLASS_NAME, 'vkuiButton--appearance-negative')
    EDIT_ICON = (By.CSS_SELECTOR, 'svg.vkuiIcon--write_outline_20 Header_button__SuQAE')
    CROSS_BUTTON = (By.CLASS_NAME, 'vkuiIconButton--sizeY-none')
    CROSS_MENU = (By.CLASS_NAME, 'ModalConfirm_title__9vHh8')
    ABORT_MENU = (By.CLASS_NAME, 'ModalConfirm_buttons__ape2n')
    ABORT_MENU_BUTTON = (By.CLASS_NAME, 'vkuiButton--mode-primary')

    SHARING_AUDIENCE_BUTTON = (By.CLASS_NAME, 'sharingButton_button__K6Oqi')
    DELETE_AUDIENCE_BUTTON = (By.CLASS_NAME, 'RemoveItemsButton_button__6OoPq')
    SHARING_AUDIENCE = (By.CSS_SELECTOR, 'input.vkuiCheckbox__input')
    SHARING_DELETE_WINDOW = (By.CLASS_NAME, 'vkuiPanelHeader__content-in')
    DELETE_AUDIENCE = (By.CSS_SELECTOR, 'input.vkuiCheckbox__input')
    DELETE_AUDIENCE_BUTTON_MENU = (By.CLASS_NAME, 'RemoveItemsModal_footer__pfEgN')
    DELETE_AUDIENCE_BUTTON_IN_MENU = (By.CLASS_NAME, 'vkuiButton--mode-primary')

    LISTS_USERS = (By.ID, "tab_audience.users_list")
    DOWNLOAD_LIST = (By.XPATH, "//*[@data-testid='download-list']")
    DOWNLOAD_HEAD = (By.CLASS_NAME, "ModalSidebarPage_title__Uu-FC")

    OFFLINE_CONVERSIONS = (By.ID, "tab_audience.offline_conversion")

