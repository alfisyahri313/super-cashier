## Problem Background

* Andi faced issues at the cashier, such as long queues and slow transaction times
* He wants to implement a self-service cashier system in his supermarket to solve these problems
* The system allows customers to scan and input their purchases, aiming to speed up transactions, reduce queues, and provide a better shopping experience
* Andi wants to make his supermarket accessible to customers who are not in the city by offering easy and flexible payment and delivery options
* He aims to create a process for generating customer IDs, adding items, editing names, quantities, and prices, deleting items, resetting transactions, checking orders, applying discounts, and checking out.

## Requirements/Objectives

* Create a process for generating a customer ID for each transaction
* Create a process for adding items to the transaction
* Create a process for editing item names
* Create a process for editing item quantity
* Create a process for editing item price
* Create a process for deleting items
* Create a process for resetting the transaction
* Create a process for checking the order
* Create a process for applying discounts
* Create a process for checkout

## Program Flow Chart
![Alt text](/flowchart.png "Flow Chart")

## Function Explanation
All Function below is in the Transaction class in the main.py file:

### Method
* __init__ : Constructor method for the Transaction class. Initializes an empty item_list and establishes a connection to the 'transactions.db' SQLite database. Calls the create_table method to create the required tables for the database.
* create_table : Create the 'transaction_details' table in the connected database if it does not exist.
* add_item : Adds a new item to the item list or updates the quantity if the item already exists.
* update_item_name : Update an existing item_name to the item list with new_item_name.
* update_item_quantity : Update quantity of an existing item_name to the item list.
* update_item_price : Update price of an existing item_name to the item list.
* delete_item : Delete an existng item_name from the item list.
* reset_transaction : Delete all items from the item list.
* check_order : Print the current item_list.
* check_out : Check out the current item_list. Calculate discount and total price of the item list. Discount is defined as follows:
    * if total price of a set of item of same item_name is above 200.000 then the discount is 5%.
    * if total price of a set of item of same item_name is above 300.000 then the discount is 6%.
    * if total price of a set of item of same item_name is above 500.000 then the discount is 7%.
Insert the current transaction to database. Delete the current item_list.

### Test and Output
* Test can be seen in testing.ipynb
* Final Output
![Alt text](/database-table2.png "Database SQLite")

### Conclusion
* Super cashier is a program to enable customer input their purchases and check out the items by them self.
* With this program a lot of process can be done by customer them self. It will speed up transaction and reduce queue

### Future Work
* Add GUI for customer and Deploy the program as web app
