# kangaroo.py

from .animal import Animal


class Kangaroo(Animal):
    def __init__(self, name="Roo"):
        super().__init__(name, species="Kangaroo")

    def sound(self):
        return "thumps"

    def action(self):
        return "hops around happily."
