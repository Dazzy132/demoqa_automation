import time

import allure
import pytest

from data.generator import generated_textbox_data
from pages.config import Config
from pages.elements_page import TextBoxPage, CheckBoxPage
from tests.base import BaseTest


@allure.suite("Elements")
class TestElements(BaseTest):

    @allure.feature("TestBox")
    class TestTextBox:

        @allure.title("Check TextBox")
        def test_text_bow(self, driver):
            text_box_page = TextBoxPage(driver, url=Config.TEST_BOX_PAGE)
            text_box_page.open()

            text_box_input_data = next(generated_textbox_data())
            text_box_page.fill_text_box_fields(text_box_input_data)

            assert text_box_input_data == text_box_page.check_output_textbox_data()

        @allure.title("Test incorrect email")
        @pytest.mark.parametrize(
            "email", ["email", "@domain.com"]
        )
        def test_incorrect_email(self, driver, email):
            """Проверка на не корректный email"""
            text_box_page = TextBoxPage(driver, url="https://demoqa.com/text-box")
            text_box_page.open()

            text_box_input_data = next(generated_textbox_data())
            text_box_input_data.email = email
            text_box_page.fill_text_box_fields(text_box_input_data)

            assert text_box_page.find_element(
                ("xpath", "//input[@id='userEmail' and contains(@class, 'field-error')]")
            ).is_displayed()

    class TestCheckBox:

        def test_check_boxes(self, driver):
            check_box_page = CheckBoxPage(driver, url=Config.CHECK_BOX_PAGE)
            check_box_page.open()
            check_box_page.click_expand_checkboxes_button()
            check_box_page.click_random_checkboxes()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_checkboxes = check_box_page.get_output_checkboxes()

            assert input_checkboxes == output_checkboxes
