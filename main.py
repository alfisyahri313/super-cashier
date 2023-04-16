import pandas as pd
import sqlite3

class Transaction:
    def __init__(self):
        """
        Constructor method for the Transaction class. Initializes an empty item_list and establishes a connection to the 
        'transactions.db' SQLite database. Calls the create_table method to create the required tables for the database.
        """
        self.item_list = [] # create an empty list to hold transaction items
        self.conn = sqlite3.connect('transactions.db') # establish connection to the database
        self.create_table() # call the create_table method to create the required tables for the database

    
    def create_table(self):
        """Create the 'transaction_details' table in the connected database if it does not exist.

        This method uses the 'sqlite3' module to create a table named 'transaction_details' with the following columns:
        - id (INTEGER): primary key for each transaction detail
        - item_name (TEXT): name of the item sold
        - quantity (INTEGER): quantity of the item sold
        - price (REAL): price of each item sold
        - discount (REAL): discount applied to the item sold
        - total_price_before_discount (REAL): total price of the item sold before applying any discount
        - total_price (REAL): total price of the item sold after applying any discount

        If the table already exists, this method does nothing.

        Returns:
        None
        """
        # Create a cursor object to execute SQL queries
        c = self.conn.cursor()
        
        # Create the transaction_details table if it does not exist
        c.execute('''CREATE TABLE IF NOT EXISTS transaction_details 
                    (   id INTEGER PRIMARY KEY,
                        item_name TEXT,
                        quantity INTEGER,
                        price REAL,
                        discount REAL,
                        total_price_before_discount REAL,
                        total_price REAL
                    )
                    ''')
        
        # Commit the changes to the database
        self.conn.commit()


    def add_item(self, item_name, quantity, price):
        """
        Adds a new item to the item list or updates the quantity if the item already exists.
        Validates the inputs and prints an error message if any input is invalid.

        Parameters:
            item_name (str): The name of the item to add or update.
            quantity (int): The quantity of the item to add or update.
            price (float): The price of the item to add or update.

        Returns:
            None
        """
        # validate inputs
        if not isinstance(item_name, str) or item_name == "" or not isinstance(quantity, int) or quantity <= 0 or not isinstance(price, (int, float)) or price <= 0:
            print("Invalid input!")
            return
        
        # check if item already exists
        for item in self.item_list:
            if item['item_name'] == item_name:
                item['quantity'] += quantity
                item['price'] = price
                item['total_price_before_discount'] = quantity*price
                print("Item quantity updated.")
                self.check_order()
                return
        
        # add new item to list
        self.item_list.append({
            'item_name': item_name,
            'quantity': quantity,
            'price': price,
            'total_price_before_discount': quantity*price
        })
        print("Item added.")
        self.check_order()


    def update_item_name(self, item_name, new_item_name):
        """
        Update an existing item_name to the item list with new_item_name.
        Validates the inputs and prints an error message if any input is invalid.

        Parameters:
            item_name (str): The name of the item to update.
            new_item_name (str): The new name of the item to update.


        Returns:
            None
        """
        # validate inputs
        if not isinstance(item_name, str) or item_name == "" or not isinstance(new_item_name, str) or new_item_name == "":
            print("Invalid input!")
            return
        
        for item in self.item_list:
            if item['item_name'] == item_name:
                item['item_name'] = new_item_name
                print("Item name updated.")
                self.check_order()
                return
        
        print("Item not found.")

    def update_item_quantity(self, item_name, new_quantity):
        """
        Update quantity of an existing item_name to the item list.
        Validates the inputs and prints an error message if any input is invalid.

        Parameters:
            item_name (str): The name of the item to update.
            new_quantity (int): The new quantity of the item to update.


        Returns:
            None
        """
        # validate inputs
        if not isinstance(item_name, str) or item_name == "" or not isinstance(new_quantity, int) or new_quantity <= 0:
            print("Invalid input!")
            return
        
        for item in self.item_list:
            if item['item_name'] == item_name:
                item['quantity'] = new_quantity
                item['total_price_before_discount'] = new_quantity*item['price']
                print("Item quantity updated.")
                self.check_order()
                return
        
        print("Item not found.")

    def update_item_price(self, item_name, new_price):
        """
        Update price of an existing item_name to the item list.
        Validates the inputs and prints an error message if any input is invalid.

        Parameters:
            item_name (str): The name of the item to update.
            new_price (float): The new price of the item to update.


        Returns:
            None
        """
        # validate inputs
        if not isinstance(item_name, str) or item_name == "" or not isinstance(new_price, (int, float)) or new_price <= 0:
            print("Invalid input!")
            return
        
        for item in self.item_list:
            if item['item_name'] == item_name:
                item['price'] = new_price
                item['total_price_before_discount'] = item['quantity']*new_price
                print("Item price updated.")
                self.check_order()
                return
        
        print("Item not found.")

    def delete_item(self, item_name):
        """
        Delete an existng item_name from the item list.
        Validates the inputs and prints an error message if any input is invalid.

        Parameters:
            item_name (str): The name of the item to delete.

        Returns:
            None
        """
        # validate inputs
        if not isinstance(item_name, str) or item_name == "":
            print("Invalid input!")
            return
        
        for i, item in enumerate(self.item_list):
            if item['item_name'] == item_name:
                self.item_list.pop(i)
                print("Item deleted.")
                self.check_order()
                return
        
        print("Item not found.")

    def reset_transaction(self):
        """
        Delete all items from the item list.

        Returns:
            None
        """
        self.item_list = []
        print("Transaction reset.")
        self.check_order()

    def check_order(self):
        """
        Print the current item_list.

        Returns:
            None
        """
        if len(self.item_list) == 0:
            print("Transaction is empty.")
            return

        df = pd.DataFrame(self.item_list)
        print(df)

    def check_out(self):
        """
        Check out the current item_list. 
        Calculate discount and total price of the item list. 
        Insert the current transaction to database.
        Delete the current item_list.

        Returns:
            None
        """
        self.conn = sqlite3.connect('transactions.db')
        c = self.conn.cursor()
        total_price_before_discount = 0
        total_discount = 0
        total_price = 0
        item_list_check_out = []
        for item in self.item_list:
            item_price = item["total_price_before_discount"]
            total_price_before_discount += item_price
            if item_price > 500000:
                discount = 0.07 * item_price
            elif item_price > 300000:
                discount = 0.06 * item_price
            elif item_price > 200000:
                discount = 0.05 * item_price
            else:
                discount = 0
            discounted_price = item_price - discount
            total_price += discounted_price
            total_discount += discount
            item_list_check_out.append({
                "item_name" : item["item_name"],
                "quantity" : item["quantity"],
                "price" : item["price"],
                "discount" : discount,
                "total_price_before_discount" : item["total_price_before_discount"],
                "total_price" : discounted_price
            })
            
            # print(f"{item['item_name']}: {item['quantity']} x {item['price']} = {discounted_price}")
            
            # Insert the transaction item into the transaction_item table
            c.execute("""
                INSERT INTO transaction_details (item_name, quantity, price, discount, total_price_before_discount, total_price)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ( item["item_name"], item["quantity"], item["price"], discount, item["total_price_before_discount"], discounted_price))
        
        # Commit the changes to the database
        self.conn.commit()
        if len(item_list_check_out) == 0:
            self.reset_transaction()
        else:
            df = pd.DataFrame(item_list_check_out)
            print(df)
            print(f"Total Price Before Discount: {total_price_before_discount}")
            print(f"Total Discount: {total_discount}")
            print(f"Total Price: {total_price}")

            # Reset the item list
            self.reset_transaction()
