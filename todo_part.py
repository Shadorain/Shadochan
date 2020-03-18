from tabulate import tabulate
import sqlite3 as db
from datetime import date
from uuid import uuid4

today = str(date.today().strftime('%m-%d-%Y'))


def new(f_name, type, ctype):
    conn = db.connect("/root/Documents/Shadochan/todo/{}.{}.db".format(f_name, ctype))
    cur = conn.cursor()
    # Homework: class | date | due date | assignment | notes
    # Goals: category | date | due date | description | notes
    # Tech:  category | date | due date | description | notes
    cur.execute("create table if not exists type=? (category string, date string, due_date string, description string, notes string, uuid string)", type)
    conn.commit()


def add(type, f_name, category, due_date, description, notes):
    rand_id = str(uuid4())

    conn = db.connect("/root/Documents/Shadochan/todo/hello.t.db")  # .format(f_name, ctype))
    cur = conn.cursor()
    cur.execute("insert into type=? values('category=?', 'today=?', 'due_date=?', 'description=?', 'notes=?', 'rand_id=?')",
                (category, today, due_date, description, notes, rand_id))
    conn.commit()
    print("  |----------------------------------|  ")
    print("-<|     Item added Successfully!     |>-")
    print("  |----------------------------------|  ")


def delete(type, f_name, ln):
    conn = db.connect("/root/Documents/Shadochan/todo/hello.t.db")  # .format(f_name, ctype))
    cur = conn.cursor()

    conn.commit()
    print("  |------------------------------------|  ")
    print("-<|     Item deleted Successfully!     |>-")
    print("  |------------------------------------|  ")


def list(f_name, type, ctype, category):
    conn = db.connect("/root/Documents/Shadochan/todo/{}.{}.db".format(f_name, ctype))
    cur = conn.cursor()
    if category:
        cur.execute("select * from type=? where category='category=?'", (type, category))
    else:
        cur.execute("select * from type=?", (type,))

    results = cur.fetchall()

    return results
