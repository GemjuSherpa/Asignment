import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

wb = openpyxl.load_workbook('World Temperature.xlsx')
sheet = wb.create_sheet('Comparision')

connection = sqlite3.connect("globaltemperature.db")
cursor = connection.cursor()

sql_state = """
	select State, strftime('%Y', Date), Average_Temp
	from Bystate where Country = 'Australia' 
	order by strftime('%Y', Date);

"""

sql_national = """
	select strftime('%Y', Date), Average_Temp
	from Bycountry where Country = 'Australia' 
	order by strftime('%Y', Date);

"""

def stateData(sql_state):
	cursor.execute(sql_state)
	array1 = np.array(cursor.fetchall())

	year_temp = array1[:, 1::]

	year = []
	temp = []

	for i in year_temp:
		year.append(i[0])
		temp.append(i[1])

	data = list(zip(year, temp)) # create a dictionaries k, v -> year, temp

	d = {}
	for k, v in data:
		d.setdefault(k, []).append(v) # combine dictionaries values together forming a lists as k, v ->year, lists of temp

	values = [] #lists of Values which is temperature
	keys = [] # lists if keys which is year
	for k, v in d.items():
		values.append(v)
		keys.append(k)



	valuesfloat = [] # lists of values converted to floats
	mean = []
	for j in values:
		valuesfloat.append([float(i) for i in j if i != "None"]) # eliminate the None values
	for value in valuesfloat:
		mean.append(sum(value)/len(valuesfloat)) # calculate the mean temp for each year
	mean2 = list(zip(keys, mean))
	return mean2
####################################
def nationalData(sql_national):
	cursor.execute(sql_national)
	array2 = np.array(cursor.fetchall())
	year1 = []
	temp1 = []

	for i in array2:
		year1.append(i[0])
		temp1.append(i[1])

	data1 = list(zip(year1, temp1)) # create a dictionaries k, v -> year, temp

	d1 = {}
	for k, v in data1:
		d1.setdefault(k, []).append(v) # combine dictionaries values together forming a lists as k, v ->year, lists of temp

	values1 = [] #lists of Values which is temperature
	keys1 = [] # lists if keys which is year
	for k, v in d1.items():
		values1.append(v)
		keys1.append(k)

	valuesfloat1 = [] # lists of values converted to floats
	mean1 = []
	for j in values1:
		valuesfloat1.append([float(i) for i in j if i != "None"]) # eliminate the None values
	for value in valuesfloat1:
		mean1.append(sum(value)/len(valuesfloat1)) # calculate the mean temp for each year
	mean3 = list(zip(keys1, mean1))
	return mean3
#######


m1 = stateData(sql_state)
npm1 = np.array(m1)
x1 = npm1[:, 0]
y1 = npm1[:, 1]

m2 = nationalData(sql_national)
npm2 = np.array(m2)

x2 = npm2[:, 0]
y2 = npm2[:, 1]

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()



