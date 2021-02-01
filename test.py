# based on https://www.microsoft.com/en-us/sql-server/developer-get-started/python/windows/step/2.html

import json
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
    # help getting the data into a json object from:
    # https://stackoverflow.com/questions/16519385/output-pyodbc-cursor-results-as-python-dictionary/16523148#16523148
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    print(results)
