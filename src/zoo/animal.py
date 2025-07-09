class Animal:
    def __init__(self, name, species):
        self.name = type(self).__name__
        self.species = species

    def sound(self):
        raise NotImplementedError("Each animal must define its own sound.")

    def action(self):
        raise NotImplementedError("Each animal must define a unique action.")

    def describe(self):
        return f"{self.name} the {self.species} says {self.sound()} and {self.action()}"
