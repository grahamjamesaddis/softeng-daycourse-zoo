
# elephant.py

from .animal import Animal


class Salamander(Animal):
    def __init__(self, name="Sally"):
        super().__init__(name, species="Salamander")

    def sound(self):
        return "Sssshhh"

    def action(self):
        return "slithers!"
