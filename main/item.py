class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.profitability = value / weight

    def print_info(self):
        print("Item name: " + self.name + " Weight: " + str(self.weight) + " Value: " + str(self.value)
              + " Profitability: " + str(self.profitability))





