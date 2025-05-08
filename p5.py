Aim : Develop an chatbot for any suitable customer interaction application 
def welcome():
    print("****** Welcome to Food Shop ******")
    print()

def info():
    global name  # To access 'name' in order() function
    print("Can I know your good name?")
    name = input("Can I know your good name: ")
    print("Hey " + name + "! Good to see you here!!!")
    print("You are in the right place, I will help you to book your dish and drinks.")
    print()

def menu():
    print('''Here is your menu with their prices:
1. Pizza - RS.200
2. Mango Juice - RS.70
3. Apple Juice - RS.80
''')

def choice():
    print("Please select an item by entering the corresponding number:")
    user_choice = input("Enter your choice (1/2/3): ")

    if user_choice == "1":
        order(200, "Pizza")
    elif user_choice == "2":
        order(70, "Mango Juice")
    elif user_choice == "3":
        order(80, "Apple Juice")
    else:
        print("Invalid choice! Please try again.")
        choice()  # Recursively call choice() for a valid input

def order(price, product):
    global name
    print("\nThank you for choosing " + product)
    print("\nPlease give us some more information about you!")
    mob = input("Enter your mobile number: ")
    add = input("Enter your address for delivery: ")

    print('''Choose payment mode:
1. Online
2. Cash on delivery''')
    pay = input("Enter your choice (1/2): ")

    paymode = "Online" if pay == "1" else "Cash on delivery"

    print("\n******* Here is the detail of your selected order ******\n")
    print("Customer Name: " + name)
    print("Product Name: " + product)
    print("Price of Product: RS." + str(price))
    print("Mode of Payment: " + paymode)
    print("Delivery Address: " + add)
    
    b = input("\nPlease confirm by pressing 1, else press 0 to cancel: ")

    if b == "1":
        print("\n******* Your order has been booked successfully! *******")
        print("Customer Name: " + name)
        print("Product Name: " + product)
        print("Price of Product: RS." + str(price))
        print("Mode of Payment: " + paymode)
        print("Delivery Address: " + add)
        print("\nThank you for your interest! Have a nice day!!!")
    else:
        print("\n***** Thank you for visiting! Have a nice day!!! *****")

def main():
    welcome()
    info()
    menu()
    choice()  # Now correctly defined

# Main function call
if __name__ == "__main__":
    main()
