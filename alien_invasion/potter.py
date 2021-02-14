class Magician:
    def __init__(self, name, house, ancestry, wealth):
        self.name = name
        self.house = house
        self.ancestry = ancestry
        self.wealth = wealth
        self.score = 0

    def show(self):
        print(f"My name is {self.name}. My house is {self.house}. My ancestry is {self.ancestry}. My parents were {self.wealth}.")
        print(f"My score is {self.score}")

    def set_score(self, new_score):
        self.score = new_score
    
harry_potter = Magician("Harry Potter", "Griffyndor", "Dad: Pure blood  Mom: Muggle born", "Rich")
ron = Magician("Ronald Weasley", "Griffyndor", "Dad: Pure blood  Mom: Pure blood", "Poor")

harry_potter.show()
ron.show()

harry_potter.set_score(10)
ron.set_score(5)


harry_potter.show()
ron.show()


