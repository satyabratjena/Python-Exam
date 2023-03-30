
# Inventory Management of Computer Accessory Store, using Flask RestFul

This program is a Flask(*Flask RESTful API*) application for managing an inventory of computer accessories store. It uses a SQLAlchemy database to store information about the accessories, include accessory names, ordered quantities, remaining quantities, vendor names, purchase prices, selling prices, and the dates and times when they were added to the inventory.

Url : http://http://127.0.0.1:5000


## Description: 

- app.py - Flask python file
- index.html - To see details of accessories in tabular format using jinja.
- inventory.db - It has the table for inventory of computer accessories.
- Output_DEMO.docx - Screensorts of Project Output in POSTMAN and DB Browser.


The program has four routes, one html page in templates folder, one inventory.db:

The '/show' route displays all the accessories in the inventory using a Jinja template.

The '/create' route creates a new accessory in the inventory based on the data provided in a JSON sent in a POST request. The data is validated using a Marshmallow schema before it is added to the database.

The /'update/<id>/' route updates the information of an accessory with a given ID based on the data provided in a JSON payload sent in a PUT request.

The '/delete/<id>/' route deletes an accessory with a given ID from the inventory.

The program also defines a Store class that represents an accessory in the inventory and a Marshmallow schema StoreSchema that serializes and deserializes the Store objects to and from JSON.




## Authors

- [@satyabratjena](https://github.com/satyabratjena)

