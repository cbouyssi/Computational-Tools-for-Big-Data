from pymongo import MongoClient
client = MongoClient()

# print(client.database_names())            #print the name of available databases
db = client.Northwind
customers = db.customers
products = db.products
orders = db.orders
employees = db.employees
order_details = db['order-details']




for chartreuse_id in products.find({'ProductName': 'Chartreuse verte'}):
    for order_detail in order_details.find({'ProductID': chartreuse_id['ProductID'], 'Quantity': {'$gt': 29} }):
        for order in orders.find({'OrderID':order_detail['OrderID']}):
            for employee in employees.find({'EmployeeID': order['EmployeeID']}):
                print(order['CustomerID'], employee['LastName'], order_detail['Quantity'])
