import allure

from data import TextBoxData
from locators.elements_locator import TextBoxLocators
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
