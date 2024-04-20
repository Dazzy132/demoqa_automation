import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import get_browser_options


@pytest.fixture(scope="function", autouse=True)
def driver():
    """Фикстура для получения браузера"""

    service = Service(ChromeDriverManager().install())
    browser_options = get_browser_options()
    driver = Chrome(service=service, options=browser_options)

    yield driver

    driver.quit()

