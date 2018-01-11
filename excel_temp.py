import openpyxl
import sqlite3

connection = sqlite3.connect("globaltemperature.db")
cursor = connection.cursor()
cities = []

sql = """
	SELECT City, STRFTIME('%Y', Date), Average_Temp
	FROM Bycity
	WHERE Country = 'China'
	ORDER BY STRFTIME('%Y', Date);
"""

cursor.execute(sql)
cities.append(cursor.fetchall())

print(cities)