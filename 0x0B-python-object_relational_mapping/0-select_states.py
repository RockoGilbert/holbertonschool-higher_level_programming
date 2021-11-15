#!/usr/bin/python3
"""This is a script that imports all states from database"""


import MySQLdb

if __name__ == '__main__':
    


    db = MySQLdb.connect(host="local host", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

roc = db.cursor()
roc.execute("SELECT * FROM states ORDER by id ASC")
roc = cur.fetchall()