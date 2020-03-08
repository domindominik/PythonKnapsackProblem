from main.item import Item
from main.knapsack import Knapsack

class Loader:
    def __init__(self, Knapsack):
        self.Knapsack = Knapsack

    def loading(self, items_list):

        items_list = sorted(items_list, key=lambda item: item.profitability, reverse=True)

        for x in items_list:
            #if Knapsack.max_weight >= Knapsack.knapsack_weight + Item.weight:
            if Knapsack.max_weight > Knapsack.knapsack_weight + Item.weight:
                Knapsack.add_item(Item)
                #Knapsack.knapsack_weight = Item.weight + Knapsack.knapsack_weight