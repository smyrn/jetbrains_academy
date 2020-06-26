class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.cash = 550
        self.machine_state = "action"  # Possible states: action, coffee_choice, fill_ingredient
        self.fill_ingredient_count = 0

    def take_input(self, user_input):
        if self.machine_state == "action":
            if user_input == "buy":
                self.machine_state = "coffee_choice"
            elif user_input == "fill":
                self.machine_state = "fill_ingredient"
                self.fill_ingredients(user_input)
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.show_ingredient_levels()
            elif user_input == "exit":
                exit()
            else:
                print(f"That is not a valid choice.")

        elif self.machine_state == "coffee_choice":
            if user_input in "123":
                self.make_coffee(user_input)
            elif user_input == "back":
                self.machine_state = "action"
            else:
                print(f"That is not a valid choice.")

        elif self.machine_state == "fill_ingredient":
            self.fill_ingredients(user_input)

    def fill_ingredients(self, user_input):
        if self.fill_ingredient_count == 0 and user_input == "fill":
            print(f"Write how many ml of water do you want to add:")
        elif self.fill_ingredient_count == 0 and user_input != "fill":
            self.water += int(user_input)
            self.fill_ingredient_count += 1
            print(f"Write how many ml of milk do you want to add:")
        elif self.fill_ingredient_count == 1:
            self.milk += int(user_input)
            self.fill_ingredient_count += 1
            print(f"Write how many grams of coffee beans do you want to add:")
        elif self.fill_ingredient_count == 2:
            self.coffee_beans += int(user_input)
            self.fill_ingredient_count += 1
            print(f"Write how many disposable cups of coffee do you want to add:")
        elif self.fill_ingredient_count == 3:
            self.cups += int(user_input)
            self.fill_ingredient_count = 0
            self.machine_state = "action"

    def show_ingredient_levels(self):
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.cash} of money")

    def make_coffee(self, coffee_type):
        if coffee_type == "1":
            if self.water - 250 < 0:
                print(f"Sorry, not enough water")
            elif self.coffee_beans - 16 < 0:
                print(f"Sorry, not enough coffee beans")
            elif self.cups - 1 < 0:
                print(f"Sorry, not enough disposable cups")
            else:
                print(f"I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.cash += 4

        elif coffee_type == "2":
            if self.water - 350 < 0:
                print(f"Sorry, not enough water")
            elif self.milk - 75 < 0:
                print(f"Sorry, not enough milk")
            elif self.coffee_beans - 20 < 0:
                print(f"Sorry, not enough coffee beans")
            elif self.cups - 1 < 0:
                print(f"Sorry, not enough disposable cups")
            else:
                print(f"I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.cash += 7

        elif coffee_type == "3":
            if self.water - 200 < 0:
                print(f"Sorry, not enough water")
            elif self.milk - 100 < 0:
                print(f"Sorry, not enough milk")
            elif self.coffee_beans - 12 < 0:
                print(f"Sorry, not enough coffee beans")
            elif self.cups - 1 < 0:
                print(f"Sorry, not enough disposable cups")
            else:
                print(f"I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.cash += 6

        self.machine_state = "action"

    def take_money(self):
        print(f"I gave you ${self.cash}")
        self.cash = 0


coffeeMachine = CoffeeMachine()

while True:
    if coffeeMachine.machine_state == "action":
        print(f"Write action (buy, fill, take, remaining, exit):")
        coffeeMachine.take_input(input())
    elif coffeeMachine.machine_state == "coffee_choice":
        print(f"What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffeeMachine.take_input(input())
    elif coffeeMachine.machine_state == "fill_ingredient":
        coffeeMachine.take_input(input())
