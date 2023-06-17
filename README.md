# SalesManagement
This code implements a simple inventory and sales management system in Python. The objective is to allow product registration in the inventory, record purchases, finalize shopping carts, and perform cash register closure.
The code is organized into two main classes: "Product" and "Stock." The "Product" class represents an individual product with information such as name, quantity, and price. The "Stock" class is responsible for managing the inventory by storing products in a dictionary.

The program starts by loading the inventory from a JSON file named "stocklist.json." If the file does not exist, an error message is displayed. It is possible to register new products in the inventory, list available products, record purchases, finalize shopping carts, and perform cash register closure.

When registering a product, a unique ID, name, quantity in kg, and price per kg are requested. The product is then added to the inventory. If the ID already exists, an error message is displayed.

When listing available products, the IDs and information of products with a quantity greater than zero are shown.

When recording a purchase, the ID of the desired product is requested. If the product exists, its information is displayed, and the desired quantity in kg is requested. If the quantity is available in the inventory, the total purchase value is calculated based on the product price and the desired quantity. The user can choose to add the purchase to the shopping cart or cancel. If the quantity in stock is insufficient, an error message is displayed.

When finalizing the shopping cart, the total purchase value is displayed. If there are no items in the cart, a warning message is shown.

When closing the cash register, the total sales value is displayed by summing all the purchases made. This value is stored in a JSON file named "sellslog.json," along with the date and time of the cash register closure. If the file does not exist, it will be created.

The inventory is saved in a JSON file named "stocklist.json" whenever the cash register is closed.

This code is a basic solution for inventory and sales management, ideal for small businesses. It offers a simple interface and allows the recording of important information for future analysis. It is possible to enhance and customize this code according to the specific needs of a project or business.
