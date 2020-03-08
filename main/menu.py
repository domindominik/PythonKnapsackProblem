from main.item import Item
from main.knapsack import Knapsack
from main.loader import Loader

items_list = []

items_list.append(Item("seba", 255, 17))
items_list.append(Item("seba", 5, 100))
items_list.append(Item("seba", 25, 170))
items_list.append(Item("lara", 35, 10))
items_list.append(Item("lara", 15, 16))

print("Items before sorting")

for x in items_list:
    x.print_info()

knapsack = Knapsack(60)
print(knapsack.max_weight)
elo = Item("elobolo", 34, 987)
#elo.print_info()
#knapsack.add_item(elo)

knapsack.print_info()


loader = Loader(knapsack)





loader.loading(items_list)

knapsack.print_info()

print(knapsack.knapsack_weight)
#print(knapsack.get_items_list())