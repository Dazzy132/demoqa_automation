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
