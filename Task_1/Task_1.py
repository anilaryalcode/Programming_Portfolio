
def get_integer_input(x): #number of pizzas
    while True:
        try:
            value = int(input(x))
            if value < 0:
                print("Please enter a positive integer!")
            else:
                return value
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(x): #all yes/no question function
    while True:
        response = input(x).lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app): #total price
    pizza_price = 12
    delivery_cost = 2.5
    discount_percentage = 25

    if is_tuesday:
        pizza_price *= 0.5  # 50% discount on Tuesdays

    total_price = num_pizzas * pizza_price

    if is_delivery and num_pizzas < 5:
        total_price += delivery_cost  #adding deliver cost

    if used_app:
        total_price *= (1 - discount_percentage / 100)  #price if using app

    return round(total_price, 2) #rounding value to 2 decimal

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = get_integer_input("How many pizzas ordered? ")
    is_delivery = get_yes_no_input("Is delivery required? (Y/N) ")
    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")
    used_app = get_yes_no_input("Did the customer use the app? (Y/N) ")

    total_price = calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()