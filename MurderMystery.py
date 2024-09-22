
import pandas as pd
import sqlite3 as sql



#setting up a connection to the database
con = sql.connect("C:/Shikha/SQLMurderMystery/Database/sql-murder-mystery.db")

#We know that murder happened in SQL City and on 20180115, look for entry in crime scene report for that
query_1 = '''
select * from crime_scene_report where city = "SQL City" and date = "20180115" and type = "murder"
'''

pd.read_sql_query(query_1, con)

# Per crime scene report Security footage shows that there were 2 witnesses. The first witness lives at the 
# last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave"
#Let's, look for them.

#checking personal details of both the witnesses
query_2 = '''
SELECT *
FROM person
WHERE address_street_name = "Northwestern Dr"
ORDER BY address_number desc limit 1;
'''
pd.read_sql_query(query_2, con)[:1]

query_3 = '''
SELECT *
FROM person
WHERE name like '%Annabel%' AND address_street_name = "Franklin Ave";
'''
pd.read_sql_query(query_3, con)

#What did the witnesses say in the interview
query_4 = '''
SELECT *
FROM interview
WHERE person_id = 14887 OR person_id = 16371;
'''
pd.read_sql_query(query_4, con)


# One step closer-

# Per the witnesses Killer is a man and a member of the gym with a status of gold and having a membership no. starting with 48Z and left in a car with a no. plate of H42W
# He was working out in the gym on 9th of Jan

#Checking the gym database with above details
query_5 = '''
SELECT *
FROM get_fit_now_check_in 
WHERE membership_id like "%48Z%" AND check_in_date = 20180109 
order by check_in_date;
'''
pd.read_sql_query(query_5, con)

# Two member's found and their membership id
#now, let's check the car details by the above details
query_6 = '''
SELECT *
FROM drivers_license
WHERE plate_number like "%H42W%";
'''
pd.read_sql_query(query_6, con)

#Two male with a plate no. containg H42W

#checking personal details of both the males from the above query
query_7 = '''
SELECT *
FROM person
WHERE license_id = "423327" OR license_id = "664760";
'''
pd.read_sql_query(query_7, con)

#lets check which of this two are a member of the gym?
query_8 = '''
SELECT *
FROM get_fit_now_member
WHERE person_id = "51739" OR person_id = "67318";
'''
pd.read_sql_query(query_8, con)

#Finally, found the murderer - Jeremy Bowers. Both the membership id and status also matches as per the 
# information we found earlier.

#Now to confirm you can visit the website and run this query

#INSERT INTO solution VALUES (1, 'Jeremy Bowers'); SELECT value FROM solution;

#Result shown is:

#Congrats, you found the murderer! But wait, there's more... If you think you're up for a challenge, 
# try querying the interview transcript of the murderer to find the real villain behind this crime. 
# If you feel especially confident in your SQL skills, try to complete this final step with no more than 
# 2 queries. Use this same INSERT statement with your new suspect to check your answer.

#There's more to this, reading the transcript of the murderer
query_9 = '''
SELECT *
FROM interview
WHERE person_id = 67318;
'''
pd.read_sql_query(query_9, con)

#So, the real villain is a woman with a Tesla car and red hair. Using the above clues let find 
# out who's the mastermind behind this murder.

query_10 = '''
SELECT *
FROM drivers_license
WHERE car_make = "Tesla" AND car_model = "Model S" AND 
gender = "female" AND hair_color = "red";
'''
pd.read_sql_query(query_10, con)

#Three woman with Tesla Model S and red hair color

#personal details of the above three woman are:
query_11 = '''
SELECT *
FROM person
WHERE license_id = "202298" OR license_id = "291182" OR license_id = "918773";
'''
pd.read_sql_query(query_11, con)


#checking the event SQL symphony concert
query_12 = '''
SELECT person_id, count(*), event_name
FROM facebook_event_checkin 
GROUP BY person_id
having count(*) = 3 AND event_name = "SQL Symphony Concert" AND date like "%201712%";
'''
pd.read_sql_query(query_12, con)

#Finally, found the mastermind/real villian of this whole mystry - Miranda Priestly

#Now, confirming it on the website shows us-

#INSERT INTO solution VALUES (1, 'Miranda Priestly'); SELECT value FROM solution;

#Result is: Congrats, you found the brains behind the murder! Everyone in SQL City 
# hails you as the greatest SQL detective of all time. Time to break out the champagne!
