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
create_table()

def load_workbook(filename, sheet):
	wb = openpyxl.load_workbook("filename")
	sheet = wb.get_sheet_by_name('sheet')

	return sheet

load_workbook('GlobalLandTemperaturesByCountry.xlsx', 'GlobalLandTemperaturesByCountry')

def insert_data():
	return True
