import sqlite3
import openpyxl
import datetime

connection = sqlite3.connect("globaltemperature.db")
cursor = connection.cursor()

def create_table():
	connection.execute(
		'CREATE TABLE Bycountry(Date DATE PRIMARY KEY, '
		'Average_Temp VARCHAR(20), '
		'Avg_Temp_Uncertainty VARCHAR(30), '
		'Country CHAR(20));'
	)

	connection.execute(
		'CREATE TABLE Bystate(Date DATE PRIMARY KEY, '
		'Average_Temp VARCHAR(20), '
		'Avg_Temp_Uncertainty VARCHAR(30),'
		'State VARCHAR(30),'
		'Country CHAR(20));'
	)

	connection.execute(
		'CREATE TABLE Bycity( '
		'Date    DATE PRIMARY KEY, '
		'Average_Temp    VARCHAR(20), '
		'Avg_Temp_Uncertainty    VARCHAR(30),'
		'City   VARCHAR(30),'   
		'Country VARCHAR(30),'
		'Latitude    VARCHAR(20),'
		'Longitude   VARCHAR(20));'
	)
#create_table()

def load_workbook(filename, sheet):
	wb = openpyxl.load_workbook(filename)
	sheet = wb.get_sheet_by_name(sheet)

	rows_iter = sheet.iter_rows(min_col=0, min_row=1)
	vals = [[cell.value for cell in row] for row in rows_iter]
	datalists = []
	datalists.append(vals)

	return datalists

#load_workbook('GlobalLandTemperaturesByCountry.xlsx', 'GlobalLandTemperaturesByCountry')
#load_workbook('GlobalLandTemperaturesByState.xlsx', 'GlobalLandTemperaturesByState')


data = load_workbook('GlobalLandTemperaturesByCountry.xlsx', 'GlobalLandTemperaturesByCountry')
for p in data:
	format_str = """INSERT INTO Bycountry
	VALUES ("{Date}", "{Average_Temp}", "{Avg_Temp_Uncertainty}", "{Country}");"""
	sql_command = format_str.format(Date=p[0], Average_Temp=p[1], Avg_Temp_Uncertainty=p[2], Country=p[3])
	cursor.execute(sql_command)


