# based on https://www.microsoft.com/en-us/sql-server/developer-get-started/python/windows/step/2.html

import pyodbc
server = 'localhost'
database = 'SensorData'
username = 'eid'
password = 'eid' # super secure
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print('Creating table')
tsql = "IF NOT EXISTS (SELECT [name] FROM sys.tables WHERE [name] = 'Measurements') "\
       'CREATE TABLE Measurements ('\
       'Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY, '\
       'SensorNumber INT, '\
       'Timestamp NVARCHAR(255), '\
       'CurrentTemp FLOAT, '\
       'AlarmCount INT, '\
       'ErrorCount INT'\
       ');'
with cursor.execute(tsql):
    print ('Successfully Created!')


print ('Inserting a new row into table')
#Insert Query
sql_insert_measurement = "INSERT INTO Measurements (SensorNumber, Timestamp, CurrentTemp, AlarmCount, ErrorCount) VALUES (?,?,?,?,?);"
with cursor.execute(sql_insert_measurement, 1, '12:34', 40.1, 1, 2):
    print ('Successfully Inserted!')


with cursor.execute(sql_insert_measurement, 1, '3:12', 23.45, 0, 5):
    print ('Successfully Inserted!')

with cursor.execute(sql_insert_measurement, 2, '2:56', 55.55, 3, 4):
    print ('Successfully Inserted!')
