#!/usr/bin/python3
""" lists all cities on a given state
from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[1],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    list = [] 
    for row in rows:
        list.append(row[0])
    print(', '.join(list))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
