from main.item import Item

class Knapsack:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.knapsack_weight = 0
        self.items_list = []

    def get_items_list(self):
        return self.items_list

    def add_item(self, Item):
        self.items_list.append(Item)
        self.knapsack_weight = self.knapsack_weight + Item.weight

    def print_info(self):
        print("Max weight: " + str(self.max_weight) + " Currently weight: " + str(self.knapsack_weight))
        for x in self.items_list:
            x.print_info()
