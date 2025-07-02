
# elephant.py

from .animal import Animal


class Elephant(Animal):
    def __init__(self, name="Ellie"):
        super().__init__(name, species="Elephant")

    def sound(self):
        return "toots"

    def action(self):
        return "remembers everything!"
