from app import db


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