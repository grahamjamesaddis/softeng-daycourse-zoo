from zoo.elephant import Elephant
from zoo.kangaroo import Kangaroo
from zoo.salamander import Salamander

def test_elephant():
    assert Elephant().describe() == "Ellie the Elephant says toots and remembers everything!"


def test_kangaroo():
    assert Kangaroo().describe() == "Roo the Kangaroo says thumps and hops around happily."

def test_salamander():
    assert Salamander.describe() == "Sally the Salamander says Sssshh and slithers!"
