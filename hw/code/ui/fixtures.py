import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.login_page import LoginPage
from hw.code.ui.pages.budget_page import BudgetPage
from hw.code.ui.pages.auth_page import AuthPage
from hw.code.ui.pages.lead_page import LeadPage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()

    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_data():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    driver.get(LoginPage.url)
    return LoginPage(driver=driver)

@pytest.fixture
def auth_page(driver):
    driver.get(AuthPage.url)
    return AuthPage(driver=driver)

@pytest.fixture
def budget_page(login_page, login_data):
    my_budget_page = login_page.login(login_data["username"], login_data["password"])
    my_budget_page.open_budget_tab()
    return my_budget_page

@pytest.fixture
def lead_page(driver):
    driver.get(LeadPage.url)
    return LeadPage(driver=driver)
