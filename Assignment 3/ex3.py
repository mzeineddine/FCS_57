class Item:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price
def addItem(pItems, lItems):
    barcode = input("Enter barcode: ")
    quantity = int(input("Enter quantity: "))
    for item in lItems:
        if(item.barcode == barcode):
            pItems[item] = quantity
            break

def printReceipt(pItems):
    print("Item Name", "\t", "Total Price")
    sum = 0
    for i in pItems.keys():
        print(i.name, "\t", pItems[i]*i.price)
        sum += pItems[i]*i.price
        # print(i.barcode, "\t", i.price*pItems[i])
    print("Total payment =", sum)

item1 = Item("a","Choclate", 10)
item2 = Item("b","Milk", 20)
item3 = Item("c","Egg", 30)

listItems = [item1, item2, item3]
purchasedItems = {}
result = input("New receipt?: ")
if result.lower() == "yes":
    addItem(purchasedItems, listItems)
    result = input("add a new Item?")
    while result.lower() == "yes":
        addItem(purchasedItems, listItems)
        result = input("add a new Item?")
    printReceipt(purchasedItems)
else:
    exit(0)