from pymongo import MongoClient
client = MongoClient()

# print(client.database_names())            #print the name of available databases
db = client.Northwind
customers = db.customers
products = db.products
orders = db.orders
order_details = db['order-details']


for order in orders.find({"CustomerID":"ALFKI"}):
    for order_detail in order_details.find({"OrderID":order["OrderID"]}):
        for product in products.find({"ProductID":order_detail["ProductID"]}):
            print(order["OrderID"], product["ProductName"], product["ProductID"])
