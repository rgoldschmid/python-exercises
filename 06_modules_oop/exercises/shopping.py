"""
Time to go shopping!

For this program, you should implement an online-shopping shopping cart! Do it using classes!

--------------------------------------------------------------------------------------------------

Create a file "product.py"
Create a Class 'product' with the following...
    attributes: id (int), name (str), price(float)
    methods: __str__(self) for printing out the attributes

--------------------------------------------------------------------------------------------------

Create a file "shopping_cart.py"
Create a Class 'shopping_cart' with the following...
    attributes: items (dictionary, key = Product, value = amount)
    methods:
        add_item(self, product, quantity) to add an item to the cart
        remove_item(self, product_id) to remove an item from the cart
        get_total(self) to get the total sum of all items' prices in the cart
        __str__(self) for printing a summary of items in the cart (amount, price, etc.)

--------------------------------------------------------------------------------------------------

In this file:
1) Import the product.py and shopping_cart.py module
2) Do some examples usages, creating products and adding them to the cart.

--------------------------------------------------------------------------------------------------

Bonus Task: Create a console program using user input to add products to the cart.
Bonus Bonus Task: Create an additional class "online_shop", using product and shopping_cart classes to work!

--------------------------------------------------------------------------------------------------

Tip: As this is an exercise with learning purpose, feel free to adjust attributes or use different data structures,
if you want to extend/alternate the behaviour of the program.
Just don't do any less than asked for in the task description! :-)

Good Luck and Have Fun!
"""