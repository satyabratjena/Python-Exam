
from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow,fields
from marshmallow import Schema,fields,validate,validates,validates_schema,ValidationError

import os

# initliazing our flask app, SQLAlchemy and Marshmallow
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
app.app_context().push()
ma = Marshmallow(app) #i defined a variable to Marshmallow application. so that when ever i need to call, I can call marshmallow by ma variable
#here we using marshmallow for converting the objects into JSON


# creating database model
class Store(db.Model):
    __tablename__ = "Inventory"
    itemno = db.Column("itemno",db.Integer,primary_key=True)
    accessory = db.Column("accessory",db.String)
    ordered_qty = db.Column("ordered_qty",db.Integer)
    remain_qty = db.Column("remain_qty",db.Integer)
    vendorname = db.Column("vendorname",db.String)
    purchaseprice = db.Column("purchaseprice",db.Integer)
    sellingprice = db.Column("sellingprice",db.Integer)
    dateofadding = db.Column("dateofadding",db.String)
    timeofadding = db.Column("timeofadding",db.String)

    def __init__(self,itemno,accessory,ordered_qty,remain_qty,vendorname,purchaseprice,sellingprice,dateofadding,timeofadding):
        self.itemno = itemno
        self.accessory = accessory
        self.ordered_qty = ordered_qty
        self.remain_qty = remain_qty
        self.vendorname = vendorname
        self.purchaseprice = purchaseprice
        self.sellingprice = sellingprice
        self.dateofadding = dateofadding
        self.timeofadding = timeofadding

    def __repr__(self):
        return f"{self.itemno} -- {self.accessory} -- {self.ordered_qty} --{self.remain_qty} -- {self.vendorname} -- {self.purchaseprice} -- {self.sellingprice} -- {self.dateofadding} -- {self.timeofadding}"

class StoreValidation(ma.Schema):
    accessory = fields.String(required=True) #accessory field is required as String ## required=True mean the field is necessary to fill.
    ordered_qty = fields.Integer(required=True)
    remain_qty = fields.Integer(required=True) #qty is required as Integer field
    vendorname = fields.String(required=True)
    purchaseprice = fields.Float(required=True)
    sellingprice = fields.Float(required=True) # as the pricese will be in decimal so we take the required field as Float
    dateofadding = fields.String(required=True) #date field is required for date data
    timeofadding = fields.String(required=True) #time field is required for time data

#below code ensure that only these fields will be returned in response (POSTMAN)
class StoreSchema(ma.Schema):
    class Meta:
        fields = ("accessory","ordered_qty","remain_qty","vendorname","purchaseprice","sellingprice","dateofadding","timeofadding")

#creates an instance of Storevalidation
store_Schema = StoreValidation() #instance is to validate a single Store object
stores_Schema = StoreValidation(many=True) #many = True, use to validate a collection of Store object

# with app.app_context():
#     db.create_all()
    #this will create a file name inventory.db

@app.route('/show')
def show_all():
    all_accessories = Store.query.all() #this is using SQLAlchemy, to query all the accessories from the database
    return render_template('index.html',all_accessories=all_accessories)
#This line to redirect to the index.html and shows you all the inventory list present in the database

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        errors = store_Schema.validate(request.json)
        if errors:
            return jsonify(errors),400

        accessory = request.json['accessory'] #JSON request
        ordered_qty = request.json ['ordered_qty']
        remain_qty = request.json['remain_qty']
        vendorname = request.json['vendorname']
        purchaseprice = request.json['purchaseprice']
        sellingprice = request.json['sellingprice']
        dateofadding = request.json['dateofadding']
        timeofadding = request.json['timeofadding']

        #adding new inputs to the table name as Store
        new_accessory = Store(None, accessory,ordered_qty,remain_qty,vendorname,purchaseprice,sellingprice,dateofadding,timeofadding)
        db.session.add(new_accessory) #it will add the variable to the database
        db.session.commit() #this commit these changes to the databases
        return store_Schema.jsonify(message="Accessory created")

@app.route('/update/<int:id>/', methods=['PUT'])
def update(id):
    store = Store.query.get(id) #To update any accessory we get the accessory by giving itemno. because ID is primary key

    accessory = request.json['accessory']
    order_qty = request.json['ordered_qty']
    remain_qty = request.json['remain_qty']
    vendorname = request.json['vendorname']
    purchaseprice = request.json['purchaseprice']
    sellingprice = request.json['sellingprice']
    dateofadding = request.json['dateofadding']
    timeofadding = request.json['timeofadding']

#this will show us in the postman body
    store.accessory = accessory
    store.order_qty = order_qty
    store.remain_qty = remain_qty
    store.vendorname = vendorname
    store.purchaseprice = purchaseprice
    store.sellingprice = sellingprice
    store.dateofadding = dateofadding
    store.timeofadding = timeofadding

    db.session.commit() #Here it will update the new values with the old values
    return store_Schema.jsonify(store)

@app.route('/delete/<id>/',methods = ['DELETE'])
def delete(id):
    store = Store.query.get(id) #by calling a variable, we are going the get the id from frontend and push it to the next command
    db.session.delete(store) # .delete command will the id from store variable and delete the id

    db.session.commit() #it will permanently delete all the information related to that ID.
    return store_Schema.jsonify(store)

if __name__ == '__main__':
    app.run(debug=True)