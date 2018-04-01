import pandas 
sales = pandas.ExcelFile("sales.xlsx").parse("Sheet1")
price = sales["Price"][0:38]
print(price.mean())