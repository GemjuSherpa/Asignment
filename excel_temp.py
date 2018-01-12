import openpyxl
import sqlite3

wb = openpyxl.Workbook()

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


year = []
temp = []
city = []
for lists in cities:
	for i in lists:
		year.append(i[1]) #extract the year lists
		temp.append(i[2]) #extract the temp lists
		city.append(i[0])

data = list(zip(year, temp)) #create a dictionries k, v -> year, temp

d = {}
for k, v in data:
	d.setdefault(k, []).append(v) # combine dictionaries values together forming a lists as k, v ->year, lists of temp

values = []
keys = []
for k, v in d.items():
	values.append(v)
	keys.append(k)



valuesfloat = []
mean = []
for j in values:
	valuesfloat.append([float(i) for i in j if i != "None"])
for value in valuesfloat:
	mean.append(sum(value)/len(valuesfloat))


year_mean = dict(zip(keys, mean))
city_year = dict(zip(keys, city))

d2 = {}
for key in set(year_mean.keys()):
	try:
		d2.setdefault(key, []).append(year_mean[key])
	except KeyError:
		pass
	try:
		d2.setdefault(key, []).append(city_year[key])
	except KeyError:
		pass

print(d2)

#list_of_tuples = list(d2.items())
#print(list_of_tuples)

sheet = wb.create_sheet('Temperature By City', 0)

#header = ['Year', 'Mean_Temperature', 'City']
sheet.cell(column=1, row=1, value='Year')
sheet.cell(column=2, row=1, value='Mean_Temperature')
sheet.cell(column=3, row=1, value='City')

next_row=2
val = []
for key, value in d2.items():
	sheet.cell(column=1, row=next_row, value=key)
	val.append(value)
	print(val)
	for v in val:
		sheet.cell(column=2, row=next_row, value=v[0])
		sheet.cell(column=3, row=next_row, value=v[1])
	next_row += 1

#row = 0
#for key in d2.keys():
	#sheet.cell(row, 0, key)
	#sheet.cell(row, 1, d2[key])
	#row += 1
wb.save('World Temperature.xlsx')
wb.close()
#print(year_mean)
#print(city_year)
