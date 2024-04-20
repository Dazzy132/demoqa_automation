import allure

from data.generator import generated_textbox_data
from pages.elements_page import TextBoxPage
from tests.base import BaseTest


@allure.suite("Elements")
class TestElements(BaseTest):

    @allure.feature("TestBox")
    class TestTextBox:

        @allure.title("Check TextBox")
        def test_text_bow(self, driver):
            text_box_page = TextBoxPage(driver, url="https://demoqa.com/text-box")
            text_box_page.open()

            text_box_input_data = next(generated_textbox_data())
            text_box_page.fill_text_box_fields(text_box_input_data)

            assert text_box_input_data == text_box_page.check_output_textbox_data()
