import sqlite3
conn = sqlite3.connect('northwind.db')
conn.text_factory = bytes

request_1 = 'SELECT Orders.OrderID FROM Orders, Products INNER JOIN [Order Details] ON [Order Details].OrderID = Orders.OrderID AND Products.ProductID = [Order Details].ProductID WHERE Orders.CustomerID = "ALFKI" GROUP BY Orders.OrderID HAVING COUNT(Products.CategoryID) >= 2'
request_2 = 'SELECT req.OrderID, Products.ProductName, Categories.CategoryName FROM ('+ request_1 + ') as req, Products, Categories LEFT JOIN [Order Details] ON req.OrderID = [Order Details].OrderID WHERE Products.ProductID = [Order Details].ProductID AND Categories.CategoryID = Products.CategoryID ORDER BY req.OrderID'

i = 0
for row in conn.execute(request_2):
    print(row)
    i+=1

print(i)
