import sqlite3
conn = sqlite3.connect('northwind.db')
conn.text_factory = bytes

request = 'SELECT Orders.CustomerID, Employees.LastName, [Order Details].Quantity FROM Orders, [Order Details], Employees INNER JOIN Products ON [Order Details].ProductID = Products.ProductID WHERE [Order Details].OrderID = Orders.OrderID AND Employees.EmployeeID = Orders.EmployeeID AND Products.ProductName = "Chartreuse verte" AND [Order Details].Quantity >=30'

i = 0
for row in conn.execute(request):
    print(row)
    i+=1

print(i)
