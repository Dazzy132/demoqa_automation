class TextBoxLocators:
    # Input Fields
    full_name = ("xpath", "//input[@id='userName']")
    email = ("xpath", "//input[@id='userEmail']")
    current_address = ("xpath", "//textarea[@id='currentAddress']")
    permanent_address = ("xpath", "//textarea[@id='permanentAddress']")

    # Button
    submit_button = ("xpath", "//button[@id='submit']")

    # Output data
    output_full_name = ("xpath", "//p[@id='name']")
    output_email = ("xpath", "//p[@id='email']")
    output_current_address = ("xpath", "//p[@id='currentAddress']")
    output_permanent_address = ("xpath", "//p[@id='permanentAddress']")


class CheckBoxLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@title='Expand all']")
    ITEM_LIST = ("xpath", "//span[@class='rct-title']")
    # CSS SELECTOR. Потому что по XPATH не находится.
    CHECKED_ITEMS = ("css selector", "svg[class='rct-icon rct-icon-check']")
    # Искать в текущем узле, в родительских элементах span с классом rct-text
    CHECKED_ITEM_TITLE = ("xpath", ".//ancestor::span[@class='rct-text']")
    OUTPUT_DATA = ("xpath", "//span[@class='text-success']")

