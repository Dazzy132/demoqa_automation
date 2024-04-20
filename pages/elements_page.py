import random

import allure

from data import TextBoxData
from locators.elements_locator import TextBoxLocators, CheckBoxLocators
from pages.base import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    @allure.step('Fill in all Text Box Fields')
    def fill_text_box_fields(self, data: TextBoxData):
        self.find_element(self.locators.full_name).send_keys(data.full_name)
        self.find_element(self.locators.email).send_keys(data.email)
        self.find_element(self.locators.current_address).send_keys(data.current_address)
        self.find_element(self.locators.permanent_address).send_keys(data.permanent_address)

        self.find_element(self.locators.submit_button).click()

    @allure.step("Check output Text Box Fields")
    def check_output_textbox_data(self):
        output_full_name = self.find_element(self.locators.output_full_name).text.split(":")[1]
        output_email = self.find_element(self.locators.output_email).text.split(":")[1]
        output_current_address = self.find_element(self.locators.output_current_address).text.split(":")[1]
        output_permanent_address = self.find_element(self.locators.output_permanent_address).text.split(":")[1]

        return TextBoxData(
            full_name=output_full_name,
            email=output_email,
            current_address=output_current_address,
            permanent_address=output_permanent_address
        )


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    def click_expand_checkboxes_button(self):
        self.find_element(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkboxes(self):
        item_list = self.find_elements(self.locators.ITEM_LIST)
        count = 15

        while count > 0:
            item = item_list[random.randint(1, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.find_elements(self.locators.CHECKED_ITEMS)
        data = []

        for checked_item in checked_list:
            checked_item_title = checked_item.find_element(*self.locators.CHECKED_ITEM_TITLE)
            data.append(checked_item_title.text)

        return str(data).replace(" ", "").replace(".doc", "").lower()

    def get_output_checkboxes(self):
        output_checkboxes = self.find_elements(self.locators.OUTPUT_DATA)
        data = []
        for output_checkbox in output_checkboxes:
            data.append(output_checkbox.text)

        return str(data).replace(" ", "").lower()
