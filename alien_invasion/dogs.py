class Dog:
    def __init__(self, name):
        self.name = name

    def set_sound(self, sound):
        self.sound = sound

    def speak(self):
        print(self.name, "Says....", self.sound)


    


chini = Dog("Chini")
rose = Dog("Rose")

print(chini.name)
print(rose.name)

chini.set_sound("Bho..Bho")
rose.set_sound("Woof...Woof")


chini.speak()
rose.speak()