
import pandas as pd
import sqlite3 as sql

#setting up a connection to the database
con = sql.connect("C:/Shikha/SQLMurderMystery/Database/sql-murder-mystery.db")

#running our first query, looking for data from crime scene report
query_1 = '''
select * from crime_scene_report where city = "SQL City" and date = "20180115" and type = "murder"
'''

#seting the dataframe width to max
pd.set_option('display.max_colwidth', None)
#running our query
df = pd.read_sql_query(query_1, con)
print (df)



#checking personal details of both the witnesses
query_2 = '''
SELECT *
FROM person
WHERE address_street_name = "Northwestern Dr"
ORDER BY address_number desc;
'''
pd.read_sql_query(query_2, con)[:1]