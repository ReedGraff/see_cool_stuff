import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path) # will create file if it does not exist
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("Test.db")
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")



##########################

'''
sql_command = """CREATE TABLE emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""
  
# execute the statement
crsr.execute(sql_command)
'''

'''
# SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (23, "Rishabh",\
"Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command)
  
# another SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates",\
"M", "1980-10-28");"""
crsr.execute(sql_command)


# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()
'''

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM emp")
  
# store all the fetched data in the ans variable
ans = crsr.fetchall()
  
# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
for i in ans:
    print(i)

##########################



# close the connection
connection.close()