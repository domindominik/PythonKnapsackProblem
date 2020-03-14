from main.item import Item
from main.knapsack import Knapsack
from main.loader import Loader

items_list = []

items_list.append(Item("seba", 255, 17))
items_list.append(Item("seba", 5, 100))
items_list.append(Item("seba", 25, 170))
items_list.append(Item("lara", 35, 10))
items_list.append(Item("lara", 15, 16))
items_list.append(Item("lara croft", 215, 916))
items_list.append(Item("iphone", 21, 191))
items_list.append(Item("iphone 11 pro", 20.01, 400.9))
items_list.append(Item("iphone 11 pro", 10.01, 100.9))

print("Items before sorting")

for x in items_list:
    x.print_info()


knapsack = Knapsack(602)

loader = Loader(knapsack)
loader.loading(items_list)

print("Knapsack includes")
knapsack.print_info()

