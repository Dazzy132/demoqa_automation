import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    @allure.step("Open browser")
    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator: tuple[str, str], timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple[str, str], timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element):
        # arguments[0] - это переданный элемент
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
