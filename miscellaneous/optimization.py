

class Food:

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.calories = weight

    def getValue(self):
        return self.value


    def getCost(self):
        return self.value

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.calories) + ">"


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i],values[i], calories[i]))

    return menu


def greedy(string ="Hello, World!"):
    print(string)









