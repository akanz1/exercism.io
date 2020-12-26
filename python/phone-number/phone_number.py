class PhoneNumber:
    def __init__(self, number):
        self.number = self._validate_number(number)
        self.area_code = self.number[:3]

    @staticmethod
    def _validate_number(number):
        number = (
            number.lstrip("+1")
            .replace("-", "")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "")
            .replace(".", "")
        )
        if (
            not number.isdecimal()
            or len(number) != 10
            or number[0] in ["0", "1"]  # area code
            or number[3] in ["0", "1"]  # exchange code
        ):
            raise ValueError("Invalid Phone Number.")
        return number

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
