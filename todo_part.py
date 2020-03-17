from tabulate import tabulate
import sqlite3 as db
from datetime import date

today = str(date.today().strftime('%m-%d-%Y'))


def new(f_name, type, ctype):
    conn = db.connect("/root/Documents/Shadochan/todo/{}.{}.db".format(f_name, ctype))
    cur = conn.cursor()
    # Homework: class | date | due date | assignment | notes
    # Goals: category | date | due date | description | notes
    # Tech:  category | date | due date | description | notes
    sql.execute("create table if not exists type=? (category string, date string, due_date string, description string, notes string)", type)
    cur.execute(sql)
    conn.commit()


def add(type, f_name, category, due_date, description, notes):
    conn = db.connect("/root/Documents/Shadochan/todo/hello.t.db")  # .format(f_name, ctype))
    cur = conn.cursor()
    sql.execute("insert into type=? values('category=?', 'today=?', 'due_date=?', 'description=?', 'notes=?')",
                (category, today, due_date, description, notes))
    cur.execute(sql)
    conn.commit()
    print("  |----------------------------------|  ")
    print("-<|     Item added Successfully!     |>-")
    print("  |----------------------------------|  ")


def list(f_name, type, ctype, category):
    conn = db.connect("/root/Documents/Shadochan/todo/{}.{}.db".format(f_name, ctype))
    cur = conn.cursor()
    if category:
        sql.execute("select * from type=? where category='category=?'", (type, category))
    else:
        sql.execute("select * from type=?", type)
    cur.execute(sql)
    results = cur.fetchall()

    return results
