import sqlite3
conn = sqlite3.connect('northwind.db')
conn.text_factory = bytes

request = 'SELECT Orders.OrderID, Products.ProductName, Products.ProductID FROM Orders, Products INNER JOIN [Order Details] ON [Order Details].OrderID = Orders.OrderID AND Products.ProductID = [Order Details].ProductID WHERE Orders.CustomerID = "ALFKI" ORDER BY Orders.OrderID'

i = 0
for row in conn.execute(request):
    print(row)
    i+=1

print(i)
