#!/usr/bin/python3
"""List all name that start with N"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access to the database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
    WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    for row in cur.fethcall():
        print(row)

    cur.close()
    conn.close()
