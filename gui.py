from main import Transaction

def print_menu():
    print("1. Add item")
    print("2. Update item name")
    print("3. Update item quantity")
    print("4. Update item price")
    print("5. Delete item")
    print("6. Reset transaction")
    print("7. Check order")
    print("8. Check out")
    print("0. Exit")

def main():
    transaction = Transaction()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = int(input("Enter item price: "))
            transaction.add_item(name, quantity, price)
        elif choice == "2":
            old_name = input("Enter old item name: ")
            new_name = input("Enter new item name: ")
            transaction.update_item_name(old_name, new_name)
        elif choice == "3":
            name = input("Enter item name: ")
            quantity = int(input("Enter new item quantity: "))
            transaction.update_item_quantity(name, quantity)
        elif choice == "4":
            name = input("Enter item name: ")
            price = int(input("Enter new item price: "))
            transaction.update_item_price(name, price)
        elif choice == "5":
            name = input("Enter item name: ")
            transaction.delete_item(name)
        elif choice == "6":
            transaction.reset_transaction()
        elif choice == "7":
            transaction.check_order()
        elif choice == "8":
            transaction.check_out()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()