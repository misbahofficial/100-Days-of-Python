class CoffeeMaker:
    def __init__(self):
        self.available_water = 1000  # in ml
        self.available_milk = 500     # in ml
        self.available_coffee_beans = 200  # in grams
        self.available_cups = 10

    def check_resources(self, water_needed, milk_needed, coffee_beans_needed):
        return (
            self.available_water >= water_needed and
            self.available_milk >= milk_needed and
            self.available_coffee_beans >= coffee_beans_needed
        )

    def make_coffee(self, water_needed, milk_needed, coffee_beans_needed):
        if self.check_resources(water_needed, milk_needed, coffee_beans_needed):
            print("Making coffee...")
            self.available_water -= water_needed
            self.available_milk -= milk_needed
            self.available_coffee_beans -= coffee_beans_needed
            self.available_cups -= 1
            print("Your coffee is ready! Enjoy.")
        else:
            print("Sorry, not enough resources to make coffee.")

def display_menu():
    print("Menu:")
    print("1. Regular Coffee")
    print("2. Latte")
    print("3. Cappuccino")
    print("0. Exit")

def main():
    coffee_maker = CoffeeMaker()

    while True:
        display_menu()
        choice = input("Select coffee (1, 2, 3) or 0 to exit: ")

        if choice == '0':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select a valid option.")
            continue

        if choice == '1':  # Regular Coffee: Water - 150 ml, Coffee Beans - 20g
            coffee_maker.make_coffee(150, 0, 20)
        elif choice == '2':  # Latte: Water - 200 ml, Milk - 100 ml, Coffee Beans - 25g
            coffee_maker.make_coffee(200, 100, 25)
        elif choice == '3':  # Cappuccino: Water - 250 ml, Milk - 150 ml, Coffee Beans - 30g
            coffee_maker.make_coffee(250, 150, 30)

if __name__ == "__main__":
    main()
