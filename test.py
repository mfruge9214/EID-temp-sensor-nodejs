# based on https://www.microsoft.com/en-us/sql-server/developer-get-started/python/windows/step/2.html

import pyodbc
server = 'localhost'
database = 'SensorData'
username = 'eid'
password = 'eid' # super secure
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#Select Query
print ('Reading data from table')
tsql = "SELECT * FROM Measurements;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        row_str = ''
        for item in row:
            row_str += str(item) + ' '
        print(row_str)
        row = cursor.fetchone()