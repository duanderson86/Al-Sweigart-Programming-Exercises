inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory():
    print("Inventory:\n")
    total = 0
    for k, v in inv.items():
        print(v, k)
        total += v
    print("\nTotal number of items: {}".format(total))

def add_inventory(items):
    for item in items:
        inv.setdefault(item, 0)
        inv[item] += 1
        

display_inventory()

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_inventory(dragonLoot)

display_inventory()

