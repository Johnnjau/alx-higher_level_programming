#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb
import sys

# Establish the database connection
db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

# Create a cursor object
c = db.cursor()

# Execute the SQL query
c.execute("SELECT * FROM `states`")

# Fetch the results
results = c.fetchall()

# Process the results (example: print the data)
for row in results:
    print(row)

# Close the cursor and database connection
c.close()
db.close()
