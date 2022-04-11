class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1:
            return False

        if len([num for num in self.card_num if not num.isdigit()]):
            return False

        even_nums = [int(num) for num in self.card_num[-2::-2]]
        odd_nums = [int(num) for num in self.card_num[::-2]]
        doubled = [num * 2 if num * 2 <= 9 else num * 2 - 9 for num in even_nums]
        return sum([*doubled, *odd_nums]) % 10 == 0
