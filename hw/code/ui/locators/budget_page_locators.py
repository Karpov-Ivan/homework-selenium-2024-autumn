from selenium.webdriver.common.by import By


class BudgetPageLocators:
    #BUDGET_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(text(), 'Бюджет')]")
    BUDGET_BUTTON = (By.CLASS_NAME, "vkuiSimpleCell__content")