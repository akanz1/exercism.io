import random
from string import ascii_letters as alphabet
from typing import List


class Robot:
    def __init__(self):
        self.used_names = []
        self.name = Robot.assign_name(self)

    def assign_name(self):
        while True:
            potential_name = "".join(
                [
                    "".join(random.choices(alphabet.upper(), k=2)),
                    str(random.randint(100, 999)),
                ]
            )
            if potential_name not in self.used_names:
                self.used_names.append(potential_name)
                return potential_name

    def reset(self):
        self.name = Robot.assign_name(self)
