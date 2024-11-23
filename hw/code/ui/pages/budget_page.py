from .base_page import BasePage
from ..locators.budget_page_locators import BudgetPageLocators


class BudgetPage(BasePage):
    url = "https://ads.vk.com/hq/budget/transactions/"
    locators = BudgetPageLocators

    def __init__(self, driver):
        self.driver = driver

    def click_budget(self):
        self.click(self.locators.BUDGET_BUTTON)