from OOP import Shopping_List
def food_cart():
    total_items_ordered = eval(input("How many items will you order today ? "))
    while total_items_ordered < 1:
        print("Number of items must be at least 1 ")
        total_items_ordered = eval(input("How many items will you order today ? "))
    list_of_all_orders = []
    for i in range(total_items_ordered):
        print(f"Item #{i+1}-")
        name_of_the_food = input("Enter food : ")
        amount_of_pounds_ordered = eval(input("Enter amount of pounds : "))
        while amount_of_pounds_ordered <= 0:
            print("Amount of pounds must be greater than 0 ")
            amount_of_pounds_ordered = eval(input("Enter amount of pounds : "))
        item = Shopping_List(name_of_the_food, amount_of_pounds_ordered)
        print("")
        list_of_all_orders.append(item)
    return list_of_all_orders


def food_display(list_of_all_orders):
    print("Here's a summary of the items purchased : ")
    print("-" * 50)
    for i in range(len(list_of_all_orders)):
        list_of_all_orders[i].food_cost()
        print(f"Item : {list_of_all_orders[i].foodname}")
        print(f"Amount ordered : {list_of_all_orders[i].amount} pounds")
        print(f"Price per pound: $ {list_of_all_orders[i].get_price():.2f}")
        print(f"Price of order: $ {list_of_all_orders[i].food_cost():.2f}")
        print("")
    print("-" * 50)

def total_cost_calc(list_of_all_orders):
    total_cost = 0
    for i in range(len(list_of_all_orders)):
        total_cost += list_of_all_orders[i].food_cost()
    return total_cost

def mainFood():
    full_list = food_cart()
    food_display (full_list)
    print(f"Total cost: $ {total_cost_calc(full_list):.2f}")

mainFood()