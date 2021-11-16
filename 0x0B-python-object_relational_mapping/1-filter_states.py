#!/usr/bin/python3
"""List all names that start with N"""

import MySQLdb
import sys

def main():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cur.execute(query)
    row = cur.fethcall()

    cur.close()
    conn.close()

    if __name__ == '__main__':
        main()