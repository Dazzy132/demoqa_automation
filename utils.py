from selenium.webdriver import ChromeOptions


def get_browser_options(headless=False, no_sandbox=False, disable_shm=False):
    """Универсальная настройка браузера для любой ситуации"""
    browser_options = ChromeOptions()
    browser_options.add_argument("--window-size=1920,1080")

    if headless:
        browser_options.mobile_options("--headless")    # Полезно для Docker
    if no_sandbox:
        browser_options.add_argument("--no-sandbox")    # Полезно для Docker
    if disable_shm:
        browser_options.add_argument("--disable-dev-shm-usage")    # Полезно для Docker

    return browser_options
