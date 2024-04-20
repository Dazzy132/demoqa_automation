class TextBoxLocators:
    # Input Fields
    FULL_NAME = ("xpath", "//input[@id='userName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")

    # Button
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    # Output data
    OUTPUT_FULL_NAME = ("xpath", "//p[@id='name']")
    OUTPUT_EMAIL = ("xpath", "//p[@id='email']")
    OUTPUT_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")


class CheckBoxLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    # CSS SELECTOR. Потому что по XPATH не находится.
    CHECKED_ITEMS = ("css selector", "svg[class='rct-icon rct-icon-check']")
    # Искать в текущем узле, в родительских элементах span с классом rct-text
    CHECKED_ITEM_TITLE = ("xpath", ".//ancestor::span[@class='rct-text']")
    OUTPUT_DATA = ("xpath", "//span[@class='text-success']")

