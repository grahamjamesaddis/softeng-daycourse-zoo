# zoo_showcase.py

import os
import inspect
import importlib

ANIMAL_DIR = os.path.dirname(__file__)
SKIP_FILES = {"base.py", "zoo_showcase.py", "__init__.py"}


def load_animals():
    animals = []
    for filename in os.listdir(ANIMAL_DIR):
        if not filename.endswith(".py") or filename in SKIP_FILES:
            continue

        module_name = filename[:-3]
        try:
            module = importlib.import_module(f"zoo.{module_name}")
        except Exception:
            continue

        for name, obj in inspect.getmembers(module, inspect.isclass):
            if name.lower() == module_name and hasattr(obj, "describe"):
                try:
                    animals.append(obj())
                except Exception:
                    continue
    return animals


def showcase():
    animals = load_animals()
    if not animals:
        print("No animals found in the zoo!")
        return

    print("🦁 Welcome to the CodeZoo!\n")
    for animal in animals:
        print("•", animal.describe())


if __name__ == "__main__":
    showcase()
