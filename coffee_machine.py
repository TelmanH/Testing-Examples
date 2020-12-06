currently_water = 400
currently_milk = 540
currently_coffee_beans = 120
currently_disposable_cups = 9
currently_money = 550

print("Write action (buy, fill, take, remaining, exit):")
action = str(input())

while action != "exit":

    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        want_to_buy = str(input())

        if want_to_buy == "1":
            needed_water = 250
            needed_disposable_cups = 1
            needed_coffe_beans = 16
            not_enough = []

            if currently_coffee_beans / needed_coffe_beans < 1:
                not_enough.append("coffe_beans")
            if currently_disposable_cups / currently_disposable_cups < 1:
                not_enough.append("disposable cups")
            if currently_water / needed_water < 1:
                print("no water")
                not_enough.append("water")
            if len(not_enough) == 0:
                print("I have enough resources, making you a coffee!")

                currently_money = currently_money + 4
                currently_water = currently_water - needed_water
                currently_disposable_cups = currently_disposable_cups - needed_disposable_cups
                currently_coffee_beans = currently_coffee_beans - needed_coffe_beans
            else:
                required = "Sorry, not enough"
                for i in not_enough:
                    required = required + " " + i
                required = required + "!"
                print(required)




        elif want_to_buy == "2":
            needed_water = 350
            needed_milk = 75
            needed_disposable_cups = 1
            needed_coffe_beans = 20
            not_enough = []
            if currently_coffee_beans / needed_coffe_beans < 1:
                not_enough.append("coffe_beans")
            if currently_disposable_cups / currently_disposable_cups < 1:
                not_enough.append("disposable cups")
            if currently_water / needed_water < 1:
                not_enough.append("water")
            if len(not_enough) == 0:
                print("I have enough resources, making you a coffee!")

                currently_money = currently_money + 7
                currently_water = currently_water - needed_water
                currently_milk = currently_milk - needed_milk
                currently_disposable_cups = currently_disposable_cups - needed_disposable_cups
                currently_coffee_beans = currently_coffee_beans - needed_coffe_beans

            else:
                required = "Sorry, not enough"
                for i in not_enough:
                    required = required + " " + i
                required = required + "!"
                print(required)




        elif want_to_buy == "3":
            needed_water = 200
            needed_milk = 100
            needed_disposable_cups = 1
            needed_coffe_beans = 12
            not_enough = []

            if currently_coffee_beans / needed_coffe_beans < 1:
                not_enough.append("coffe_beans")
            if currently_disposable_cups / currently_disposable_cups < 1:
                not_enough.append("disposable cups")
            if currently_water / needed_water < 1:
                print("no water")
                not_enough.append("water")
            if len(not_enough) == 0:
                print("I have enough resources, making you a coffee!")
                currently_money = currently_money + 6
                currently_water = currently_water - needed_water
                currently_milk = currently_milk - needed_milk
                currently_disposable_cups = currently_disposable_cups - needed_disposable_cups
                currently_coffee_beans = currently_coffee_beans - needed_coffe_beans


            else:
                required = "Sorry, not enough"
                for i in not_enough:
                    required = required + " " + i
                required = required + "!"
                print(required)

        elif want_to_buy != "back":
            print("Invalid action")

        print("Write action (buy, fill, take, remaining, exit):")
        action = str(input())



    elif action == "fill":
        print("Write how many ml of water do you want to add:")
        added_water = int(input())
        currently_water = currently_water + added_water
        print("Write how many ml of milk do you want to add:")
        added_milk = int(input())
        currently_milk = currently_milk + added_milk
        print("Write how many grams of coffee beans do you want to add:")
        added_coffee_beans = int(input())
        currently_coffee_beans = currently_coffee_beans + added_coffee_beans
        print("Write how many disposable cups of coffee do you want to add:")
        added_diposable_cups = int(input())
        currently_disposable_cups = added_diposable_cups + currently_disposable_cups

        print("Write action (buy, fill, take, remaining, exit):")
        action = str(input())

    elif action == "take":
        print("I gave you $", currently_money)
        currently_money = 0

        print("Write action (buy, fill, take, remaining, exit):")
        action = str(input())

    elif action == "remaining":
        print(currently_water, "of water")
        print(currently_milk, "of milk")
        print(currently_coffee_beans, "of coffe beans")
        print(currently_disposable_cups, "disposable cups")
        print(currently_money, "of money")

        print("Write action (buy, fill, take, remaining, exit):")
        action = str(input())


    elif action == "exit":
        break

    else:
        print("Invalid action")

        print("Write action (buy, fill, take, remaining, exit):")
        action = input()











