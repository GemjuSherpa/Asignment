# Filename: sql_temp.py
# Author: Gemju Sherpa

# #!/bin/Python
import sqlite3

## Connecting to the Database
connection = sqlite3.connect("globaltemperature.db")
cursor = connection.cursor()

##Finding distinct Cities
cities = """
	SELECT  DISTINCT City, Country, Latitude
	FROM Bycity
	WHERE Latitude LIKE '%S'
	ORDER BY Country
"""
cursor.execute(cities)
result = cursor.fetchall()

print(result) ## Printing result to the console..

## Finding Min, Max and Average Temperature of Qld in year 2010.
temp = """
	SELECT  MIN(Average_Temp) AS Minimum_Temp, MAX(Average_Temp) AS Maximum_Temp, 
	AVG(Average_Temp) AS Maximum_Temp
	FROM Bystate
	WHERE State = 'Queensland' AND STRFTIME('%Y', Date) = '2010';
"""
cursor.execute(temp)
result_temp = cursor.fetchall()
print(result_temp) #Printing result to console

##Creating table Southerncities..
create_table = """
	CREATE TABLE SouthernCities(Id INTEGER PRIMARY KEY AUTOINCREMENT, 
		CityName VARCHAR(50), 
		Country VARCHAR(50), 
		GeoLocation VARCHAR(20));
"""
cursor.execute(create_table) ## execute cursor()

#looping through the result to update table SouthernCities
for i in result:
	format_str = """INSERT INTO SouthernCities(Id, CityName, Country, GeoLocation)
	VALUES (NULL, "{CityName}", "{Country}", "{GeoLocation}");"""
	sql_command = format_str.format(CityName=i[0], Country=i[1], GeoLocation=i[2])
	cursor.execute(sql_command)
	connection.commit()

	##End of Tasks

#######################################################################################