import recipe_and_ingredients

balance_money = 0

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}


def coin_insert():
    print("Please insert coins.")
    quarters_no = int(input("How many quarters?: "))
    dimes_no = int(input("How many dimes?: "))
    nickles_no = int(input("How many nickles?: "))
    pennies_no = int(input("How many pennies?: "))

    dimes_amt = dimes_no * coins["dime"]
    quarters_amt = quarters_no * coins["quarter"]
    nickles_amt = nickles_no * coins["nickel"]
    pennies_amt = pennies_no * coins["penny"]

    money = dimes_amt + quarters_amt + nickles_amt + pennies_amt
    return money


ingredients_left = recipe_and_ingredients.resources

while True:
    invalidity = False
    user_drink = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if user_drink == "espresso":
        user_choice_ing = recipe_and_ingredients.MENU[user_drink]
    elif user_drink == "latte":
        user_choice_ing = recipe_and_ingredients.MENU[user_drink]
    elif user_drink == "cappuccino":
        user_choice_ing = recipe_and_ingredients.MENU[user_drink]
    elif user_drink == "report":
        print(f"Water : {recipe_and_ingredients.resources['water']}")
        print(f"Milk : {recipe_and_ingredients.resources['milk']}")
        print(f"Coffee : {recipe_and_ingredients.resources['coffee']}")
        print(f"Money : ${balance_money}")
        invalidity = True
    else:
        invalidity = True
        print("You entered an Invalid drink.")

    items_less = []
    condition_for_water = ingredients_left["water"] >= user_choice_ing["ingredients"]["water"]
    condition_for_milk = ingredients_left["milk"] >= user_choice_ing["ingredients"]["milk"]
    condition_for_coffee = ingredients_left["coffee"] >= user_choice_ing["ingredients"]["coffee"]

    if not invalidity:
        if condition_for_water and condition_for_milk and condition_for_coffee:
            money_inserted = coin_insert()
            if money_inserted < recipe_and_ingredients.MENU[user_drink]["cost"]:
                invalidity = True
                print("Sorry, that's not enough money. Money refunded.")
            else:
                balance_money += recipe_and_ingredients.MENU[user_drink]["cost"]
                ingredients_left["water"] -= user_choice_ing["ingredients"]["water"]
                ingredients_left["milk"] -= user_choice_ing["ingredients"]["milk"]
                ingredients_left["coffee"] -= user_choice_ing["ingredients"]["coffee"]
                change = round(money_inserted - recipe_and_ingredients.MENU[user_drink]["cost"], 2)
                print(f"Here is your change of ${change}.")
                print(f"Here is your {user_drink} ☕. Enjoy!")
        else:
            invalidity = True
            missing_item = ''
            if not condition_for_water:
                missing_item = "water"
                items_less.append(missing_item)

            if not condition_for_milk:
                missing_item = "milk"
                items_less.append(missing_item)

            if not condition_for_coffee:
                missing_item = "coffee"
                items_less.append(missing_item)

            times_run = 1
            print_item_less = ' Sorry, there is not enough'
            for item in items_less:
                items_less_len = len(items_less)
                if times_run < items_less_len != 1:
                    print_item_less += f' {item},'
                    times_run += 1
                else:
                    print_item_less += f' {item}.'
                    times_run += 1

            print(print_item_less)
