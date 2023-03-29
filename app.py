from flask import Flask,request,render_template,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
SECRET_KEY = 'secretkey'
db = SQLAlchemy(app)



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
    dateofadding = db.Column("dateofadding",db.Integer)
    timeofadding = db.Column("timeofadding",db.Integer)

    def __init__(self,itemno,accessory,ordered_qty,remain_qty,vendorname,purchaseprice,sellingprice,dateofadding,timeofadding):
        self.itemno=itemno
        self.accessory=accessory
        self.ordered_qty=ordered_qty
        self.remain_qty=remain_qty
        self.vendorname=vendorname
        self.purchaseprice=purchaseprice
        self.sellingprice=sellingprice
        self.dateofadding=dateofadding
        self.timeofadding=timeofadding

    def __repr__(self):
        return f"{self.itemno} -- {self.accessory} -- {self.ordered_qty} --{self.remain_qty} -- {self.vendorname} -- {self.purchaseprice} -- {self.sellingprice} -- {self.dateofadding} -- {self.timeofadding}"


@app.route('/register', methods=['POST'])
def create():
    data = request.json
    new_accessory = Accessory(
        accessory = data['accessory'],
        ordered_qty = data['ordered_qty'],
        remain_qty = data['remain_qty'],
        vendorname = data['vendorname'],
        purchaseprice = data['purchaseprice'],
        sellingprice = data['sellingprice'],
    )
    db.session.add(new_accessory)
    db.session.commit()
    return jsonify(message="Accessory created")

@app.route(/update/<int:id>, methods=['PUT'])



if __name__ == '__main__':
    app.run()