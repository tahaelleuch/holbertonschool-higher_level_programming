#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[1],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
