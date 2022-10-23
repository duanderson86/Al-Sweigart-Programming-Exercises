inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory():
    print("Inventory:\n")
    total = 0
    for k, v in inv.items():
        print(v, k)
        total += v
    print("\nTotal number of items: {}".format(total))

display_inventory()

