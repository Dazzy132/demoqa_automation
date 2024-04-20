from dataclasses import dataclass


@dataclass
class TextBoxData:
    full_name: str
    email: str
    current_address: str
    permanent_address: str

    # def __eq__(self, other):
    #     if not isinstance(other, TextBoxData):
    #         return False
    #     return (
    #             self.full_name == other.full_name and
    #             self.email == other.email and
    #             self.current_address == other.current_address and
    #             self.permanent_address == other.permanent_address
    #     )
