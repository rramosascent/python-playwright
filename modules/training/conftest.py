import pytest
import asyncio
from playwright.sync_api import Playwright
from playwright.async_api import async_playwright

def pytest_addoption(parser):
    parser.addoption("--tbrowser", action="store", help="chrome")
    parser.addoption("--header-opt", action="store", help="chrome")
@pytest.fixture(scope="class")
def setup(request, playwright: Playwright):
    internet_browser = request.config.getoption("--tbrowser")
    execution_header = request.config.getoption("--header-opt")

    match execution_header:
        case 'headless':
            match internet_browser:
                case 'firefox':
                    browser = playwright.firefox.launch(headless=True)
                case 'webkit':
                    browser = playwright.webkit.launch(headless=True)
                case _:
                    browser = playwright.chromium.launch(headless=True)
        case _:
            match internet_browser:
                case 'firefox':
                    browser = playwright.firefox.launch(headless=False)
                case 'webkit':
                    browser = playwright.webkit.launch(headless=False)
                case _:
                    browser = playwright.chromium.launch(headless=False)

    driver = browser.new_page()
    # driver.goto("http://112.199.119.250:82/ECP/auth/login")
    request.cls.driver = driver
    yield
    driver.close()

