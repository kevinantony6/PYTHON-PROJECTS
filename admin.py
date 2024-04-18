# Coffee Machine Project
from store import menu, inventory_dict
from art import logo
print(logo)
use_inventory_list = []
bank = 0
order = 0
quantity = 0
add_sugar = 0
nt_enough_name = str
low_stock_name = str
low_stock_no = 0
bakery_order = str

def check_inventory():
    coffee_bean_stock = inventory_dict["items"]["coffee_bean"]
    milk_stock = inventory_dict["items"]["milk"]
    water_stock = inventory_dict["items"]["water"]
    sugar_stock = inventory_dict["items"]["sugar"]
    cookies_stock = inventory_dict["items"]["cookies"]
    muffins_stock = inventory_dict["items"]["muffins"]
    hash_brown_stock = inventory_dict["items"]["hash_brown"]
    burger_stock = inventory_dict["items"]["burger"]
    sandwich_stock = inventory_dict["items"]["sandwich"]
    cake_stock = inventory_dict["items"]["cake"]
    croissants_stock = inventory_dict["items"]["croissants"]

    inventory_left = f"Stock Balance\nCoffee Bean : {coffee_bean_stock} grams left\n" \
                         f"Milk : {milk_stock} litres left\nWater : {water_stock} " \
                         f"litres left\nSugar : {sugar_stock} grams left\nCookies : {cookies_stock}\n" \
                         f"Muffins : {muffins_stock}\nHash Brown : {hash_brown_stock}\nBurger : {burger_stock}\n" \
                         f"Burger : {burger_stock}\nSandwich : {sandwich_stock}\nCake : {cake_stock}\nCroissants : {croissants_stock}"
    print(inventory_left)


def use_inventory():
    global quantity
    global add_sugar
    global low_stock_name
    global low_stock_no
    inventory_dict["items"]["coffee_bean"] = (inventory_dict["items"]["coffee_bean"]) - (menu["cappuccino"]["ingredients"]["coffee_bean"]) * quantity
    inventory_dict["items"]["milk"] = inventory_dict["items"]["milk"] - (menu["cappuccino"]["ingredients"]["milk"]) * quantity
    inventory_dict["items"]["water"] = inventory_dict["items"]["water"] - (menu["cappuccino"]["ingredients"]["water"]) * quantity
    inventory_dict["items"]["sugar"] = inventory_dict["items"]["sugar"] - (menu["cappuccino"]["ingredients"]["sugar"]) * quantity
    inventory_dict["items"]["cookies"] = (inventory_dict["items"]["cookies"]) - (menu["bakery"]["cookies"]) * quantity
    inventory_dict["items"]["muffins"] = inventory_dict["items"]["muffins"] - (menu["bakery"]["muffins"]) * quantity
    inventory_dict["items"]["hash_brown"] = inventory_dict["items"]["hash_brown"] - (menu["bakery"]["hash_brown"]) * quantity
    inventory_dict["items"]["burger"] = inventory_dict["items"]["burger"] - (menu["bakery"]["burger"]) * quantity
    inventory_dict["items"]["sandwich"] = inventory_dict["items"]["sandwich"] - (menu["bakery"]["sandwich"]) * quantity
    inventory_dict["items"]["cake"] = inventory_dict["items"]["cake"] - (menu["bakery"]["cake"]) * quantity
    inventory_dict["items"]["croissants"] = inventory_dict["items"]["croissants"] - (menu["bakery"]["croissants"]) * quantity
    coffee_bean_stock = inventory_dict["items"]["coffee_bean"]
    milk_stock = inventory_dict["items"]["milk"]
    water_stock = inventory_dict["items"]["water"]
    sugar_stock = inventory_dict["items"]["sugar"]
    cookies_stock = inventory_dict["items"]["cookies"]
    muffins_stock = inventory_dict["items"]["muffins"]
    hash_brown_stock = inventory_dict["items"]["hash_brown"]
    burger_stock = inventory_dict["items"]["burger"]
    sandwich_stock = inventory_dict["items"]["sandwich"]
    cake_stock = inventory_dict["items"]["cake"]
    croissants_stock = inventory_dict["items"]["croissants"]

    if coffee_bean_stock <= 0:
        low_stock_name = "Coffee Beans."
        low_stock_no = coffee_bean_stock
        if milk_stock <= 0:
            low_stock_name = "Milk."
            low_stock_no = milk_stock
            if water_stock <= 0:
                low_stock_name = "Water."
                low_stock_no = water_stock
                if sugar_stock <= 0:
                    low_stock_name = "Sugar."
                    low_stock_no = sugar_stock
                    if cookies_stock <= 0:
                        low_stock_name = "Cookies."
                        low_stock_no = cookies_stock
                        if muffins_stock <= 0:
                            low_stock_name = "Muffins."
                            low_stock_no = muffins_stock
                            if hash_brown_stock <= 0:
                                low_stock_name = "Hash Brown."
                                low_stock_no = hash_brown_stock
                                if burger_stock <= 0:
                                    low_stock_name = "Burger."
                                    low_stock_no = burger_stock
                                    if sandwich_stock <= 0:
                                        low_stock_name = "Sandwich."
                                        low_stock_no = sandwich_stock
                                        if cake_stock <= 0:
                                            low_stock_name = "Cake."
                                            low_stock_no = cake_stock
                                            if croissants_stock <= 0:
                                                low_stock_name = "Croissants."
                                                low_stock_no = croissants_stock
                                                if low_stock_no < 0:
                                                    repl_low_stock = input("Enter 4 To Replenish Inventory : ")
                                                    if repl_low_stock == "4":
                                                        replenish_inventory()
    else:
        inventory_left = f"Stock Balance\nCoffee Bean : {coffee_bean_stock} grams left\n" \
                         f"Milk : {milk_stock} litres left\nWater : {water_stock} " \
                         f"litres left\nSugar : {sugar_stock} grams left\nCookies : {cookies_stock}\n" \
                         f"Muffins : {muffins_stock}\nHash Brown : {hash_brown_stock}\nBurger : {burger_stock}\n" \
                         f"Burger : {burger_stock}\nSandwich : {sandwich_stock}\nCake : {cake_stock}\nCroissants : {croissants_stock}"
        print(inventory_left)


def replenish_inventory():

    print("\nInventory Replenished\n")
    inventory_dict["items"]["coffee_bean"] = 100000
    inventory_dict["items"]["milk"] = 100000
    inventory_dict["items"]["water"] = 100000
    inventory_dict["items"]["sugar"] = 100000
    coffee_bean_inventory = inventory_dict["items"]["coffee_bean"]
    milk_inventory = inventory_dict["items"]["milk"]
    water_inventory = inventory_dict["items"]["water"]
    sugar_inventory = inventory_dict["items"]["sugar"]
    print(f"Coffee Bean : {coffee_bean_inventory}\nMilk : {milk_inventory}\nWater : {water_inventory}\nSugar : {sugar_inventory}")


def brew_cappuccino():
    global order 
    global bank
    global quantity
    global add_sugar
    global nt_enough_name

    quantity = int(input("How many : "))
    add_sugar = int(input("How Many Sugar : "))
    if int(inventory_dict["items"]["coffee_bean"]) < int((menu["cappuccino"]["ingredients"]["coffee_bean"]) * quantity):
        nt_enough_name = "Coffee Bean"
        if int(inventory_dict["items"]["milk"]) < (int(menu["cappuccino"]["ingredients"]["milk"]) * quantity):
            nt_enough_name = "Milk"
            if int(inventory_dict["items"]["water"]) < int((menu["cappuccino"]["ingredients"]["water"]) * quantity):
                nt_enough_name = "Water"
                if int(inventory_dict["items"]["sugar"]) < int((menu["cappuccino"]["ingredients"]["sugar"]) * quantity):
                    nt_enough_name = "Sugar"
                print(f"Not Enough {nt_enough_name}")
                query_to_rpl_inventory = input("\nEnter 4 To Replenish Inventory : ")
                if query_to_rpl_inventory == "4":
                    replenish_inventory()

    elif add_sugar > 0:
        order = int(((menu["cappuccino"]["cappuccino_cost"]) + 2) * quantity)
        print(f"Here is your Cappuccino\nTotal Price : {order} $")
        use_inventory()
    elif add_sugar == 0:
        order = int(menu["cappuccino"]["cappuccino_cost"]) * quantity
        print(f"Here is your Cappuccino\nTotal Price : {order} $")
        use_inventory()
    bank = bank +order 
    order = bank
    print(f"\nMoney Made By Robot Coffee Machine {bank} $ ")
    print("************************************************")



def brew_latte():
    global order 
    global bank
    global quantity
    global add_sugar
    global nt_enough_name

    quantity = int(input("How many : "))
    add_sugar = int(input("How Many Sugar : "))
    if int(inventory_dict["items"]["coffee_bean"]) < int((menu["latte"]["ingredients"]["coffee_bean"]) * quantity):
        nt_enough_name = "Coffee Bean"
        if int(inventory_dict["items"]["milk"]) < (int(menu["latte"]["ingredients"]["milk"]) * quantity):
            nt_enough_name = "Milk"
            if int(inventory_dict["items"]["water"]) < int((menu["latte"]["ingredients"]["water"]) * quantity):
                nt_enough_name = "Water"
                if int(inventory_dict["items"]["sugar"]) < int((menu["latte"]["ingredients"]["sugar"]) * quantity):
                    nt_enough_name = "Sugar"
                print(f"Not Enough {nt_enough_name}")
                query_to_rpl_inventory = input("\nEnter 4 To Replenish Inventory : ")
                if query_to_rpl_inventory == "4":
                    replenish_inventory()

    elif add_sugar > 0:
        order = int(((menu["latte"]["latte_cost"]) + 2) * quantity)
        print(f"Here is your latte\nTotal Price : {order} $")
        use_inventory()
    elif add_sugar == 0:
        order = int(menu["latte"]["latte_cost"]) * quantity
        print(f"Here is your latte\nTotal Price : {order} $")
        use_inventory()
    bank = bank +order 
    order = bank
    print(f"\nMoney Made By Robot Coffee Machine {bank} $ ")
    print("************************************************")


def add_bakery_items():
    global order
    global bank
    global nt_enough_name

    print("Bakery Items\nEnter Item Names To Order")
    take_bakery_order = input("cookies, muffins, hash brown, burger, sandwich, cake, croissants")
    bkry_it_qty = int(input("How many : "))

    if bakery_order == "cookies":
        bkry_take_order = bakery_order
        if bakery_order == "muffins":
            bkry_take_order = bakery_order
            if bakery_order == "hash brown":
                bkry_take_order = bakery_order
                if bakery_order == "burger":
                    bkry_take_order = bakery_order
                    if bakery_order == "sandwich":
                        bkry_take_order = bakery_order
                        if bakery_order == "cake":
                            bkry_take_order = bakery_order
                            if bakery_order == "croissants":
                                bkry_take_order = bakery_order
##ADD DEDUCT INVENTORY
##DISPENSE ORDER
##COLLECT MONEY


for r_c_machine in range(1000):
    take_order = input("What would you like\n\nEnter 1 for Cappuccino 2 for Latte 3 for Bakery Items 4 To Check Inventory 5 For Replenish Inventory: ")
    if take_order == "1":
        brew_cappuccino()
    if take_order == "2":
        brew_latte()
    if take_order == "3":
        add_bakery_items()
    if take_order == "4":
        check_inventory()
    if take_order == "5":
        replenish_inventory()

