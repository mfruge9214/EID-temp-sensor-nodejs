#########################
# File: Graph.py
# Author: Mike Fruge & Bryan Cisneros
# Description:
# 		This class creates a graph of the sensor data in the database. It reads
#		all the measurements from the database, then plots them using matplotlib
#		
#########################


from time import sleep
import os
import json
from datetime import datetime
import pyodbc
import numpy as np
import matplotlib.pyplot as plt


database = 'SensorData_1'
table = 'Sensor_Data_Test'


class Graph:

	def __init__(self):
		# dictionary that will contain all the data from all the sensors
		self.all_sensor_data = {}

		self.server = 'localhost'
		self.database = database
		self.username = 'eid'
		self.password = 'eid' # super secure
		self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
		self.cursor = self.cnxn.cursor()

		# dictionary that will contain calculations on the sensor data
		self.all_sensor_calculations = {}
		self.ErrorCount = 0
	

	def read_sensor_data(self):
		# clear the current stored data. We will re-read all of it to get a fresh copy
		self.all_sensor_data.clear()

		tsql = "SELECT * FROM " + table + ";"
		with self.cursor.execute(tsql):
			# help getting the data into a json object from:
			# https://stackoverflow.com/questions/16519385/output-pyodbc-cursor-results-as-python-dictionary/16523148#16523148
			columns = [column[0] for column in self.cursor.description]
			for row in self.cursor.fetchall():
				entry = dict(zip(columns, row))
				# if the sensor number isn't in the dictionary yet, add an
				# empty list to the dictionary for that sensor
				if entry['SensorNumber'] not in self.all_sensor_data:
					self.all_sensor_data[entry['SensorNumber']] = []
				self.all_sensor_data[entry['SensorNumber']].append(entry)


	def plotSensorData(self):
		plt.figure()
		plt.xlabel('Time (s)')
		plt.ylabel('Temperature (F)')
		plt.title('Accumulated Temperature Sensor Data')

		temps = {}
		for sensor_id, sensor_data in self.all_sensor_data.items():
			if sensor_id not in temps:
				temps[sensor_id] = []
			for entry in sensor_data:
				temp = entry['CurrentTemp']
				if temp == 999.0:
					temp = np.nan
				temps[sensor_id].append(temp)

		numEntries = len(temps[1])

		timevals = np.arange(0, 10*numEntries, 10)

		for sensor_id in self.all_sensor_data.keys():
			tempList = temps[sensor_id]
			label = 'Sensor ' + str(sensor_id)
			plt.plot(timevals, tempList, label=label)

		plt.legend()
		plt.show()

	def generate_graph(self):
		self.read_sensor_data()
		self.plotSensorData()
