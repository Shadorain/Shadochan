from tabulate import tabulate
import sqlite3 as db
from datetime import date

today = date.today().strftime('%m-%d-%Y')


def init():
    conn = db.connect("/root/Documents/Shadochan/expenses/spent.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
    )
    '''
    cur.execute(sql)
    conn.commit()


def log(amount, category, message=""):
    conn = db.connect("/root/Documents/Shadochan/expenses/spent.db")
    cur = conn.cursor()
    sql = '''
    insert into expenses values (
        {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount, category, message, today)
    cur.execute(sql)
    conn.commit()


def view(category=None):
    conn = db.connect("/root/Documents/Shadochan/expenses/spent.db")
    cur = conn.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''
        sql2 = '''
        select sum(amount) from expenses
        '''
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]

    return total_amount, results
