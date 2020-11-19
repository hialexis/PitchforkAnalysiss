import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(dbfile):
    c = None
    try:
        c = sqlite3.connect(dbfile)
    except error as e:
        print(e)
    return c


def select_query(c, sqlfile):
    cur = c.cursor()
    fd = open(sqlfile, 'r')
    sqlFile = fd.read()
    fd.close()

    cur.execute(sqlFile)

    rows = cur.fetchall()

    data =[]
    for row in rows:
        data.append((row))
    return data

def run_query(sqlfile):
    database = r"C:/Users/18184/Documents/database.sqlite/database.sqlite"

    c = create_connection(database)
    with c:
        dataset = select_query(c, sqlfile) 
    return dataset