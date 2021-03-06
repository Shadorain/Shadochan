#!/usr/bin/env python3

"""
###########################################################################

                                Shadochan 1.0
      This is an intensive Script to handle any basic Shado-kun needs!

                  Shado-chan will support in any way I can!
          Shado-kun shouldn't have to worry about pointless stuff,
                              I'll help you :)!

############################################################################

Usage:
    shadochan todo list [ --cat <type> ] FILE
    shadochan todo add <category> <due_date> <description> [ -n <notes> ] FILE
    shadochan todo ( new | delete ) FILE
    shadochan calc [ -v | -q ] ( sqr | cub ) <x>
    shadochan calc [ -v | -q ] ( add | sub | mul | div | exp ) <x> <y>
    shadochan spent [ -v ] ( init | view )
    shadochan spent log <amount> <category> <message>
    shadochan (-h | --help)
    shadochan --version

----------------------------------------------------------------------------

Global Options:
    --version   Displays current version of Shadochan
    -v          Outputs more than normal
    -q          Only prints main output

----------------------------------------------------------------------------

Todo Options:
    -c, --cat <type>     Only will display rows of specified category
    -n, --notes <notes>  Optional notes [default: ""]
    list                 Displays specified list
    new                  Will add a new file with the name being FILE
    add                  Will be prompted to provide details, creates new item to be added to later specified list
    delete               Will display list with line numbers, will be prompted to delete chosen line

Calc Options:
    <x>         Placeholder for first value
    <y>         Placeholder for second value

Spent Options:
    init        Creates table if not already made
    view        Displays table list
    log         Logs the date, amount, category, and message

----------------------------------------------------------------------------
"""

import random
import sys
import os
import time
import subprocess
from docopt import docopt
from bin.spend_tracker import *
from bin.todo_part import *
from uuid import uuid4
from bin.calculate import *

def_fold = "/root/Documents/Shadochan/"
today = date.today().strftime('%m-%d-%Y')


# -<| Spending Tracker |>-
def spend_track(args):
    if args['init']:
        init()
        print("  |----------------------------|  ")
        print("-<| Table created successfully |>-")
        print("  |----------------------------|  ")
    elif args['view']:
        cat = args['<category>']
        amount, results = view(cat)
        print(tabulate(results), headers, tablefmt="fancy_grid", showindex="always")
        print("Your total expenses: ", amount)

        try:
            iamount = float(str(amount))
            if iamount >= 0 and iamount < 50:
                print("  |-------------------------------------|  ")
                print("-<| Way to be fruitful with your money! |>-")
                print("  |-------------------------------------|  ")
            elif iamount >= 50:
                print("  |--------------------------------------------------|  ")
                print("-<| Make sure to handle your money better Shado-kun! |>-")
                print("  |--------------------------------------------------|  ")
        except:
            print("  |-----------------------------------------|  ")
            print("-<| Shado-kun, its ok to buy some stuff :)! |>-")
            print("  |-----------------------------------------|  ")

    elif args['log']:
        try:
            amount = float(args['<amount>'])
            log(amount, args['<category>'], args['<message>'])
        except:
            print(args)

        print("  |-----------------------------------------|  ")
        print("-<| Successfully logged the new information |>-")
        print("  |-----------------------------------------|  ")


# -<| Todo Lists |>-
def todo(args):
    file = str(def_fold + "todo/" + args['FILE'])
    headers = ["Category", "Date", "Due-Date", "Description", "Notes"]

    if args['new']:
        x = int(input("What type of todo list is this: \n1): Homework\n2): Goals\n3): Tech\n $(1-3)> "))
        if x == 1:
            type = "homework"
        elif x == 2:
            type = "goals"
        elif x == 3:
            type = "tech"
        else:
            print("Shado! Invalid option")
            todo(args)
        ctype = type[:1]
        print("  |------------------------------------|  ")
        print("-<| Successfully created new todo list |>-")
        print("  |------------------------------------|  ")
        new(args['FILE'], type, ctype)

    elif args['list']:
        # Determine if file exists
        ctype = None
        for key in ["h", "g", "t"]:
            try:
                f = open("/root/Documents/Shadochan/todo/{}.{}.db".format(args['FILE'], key), "r")
            except FileNotFoundError:
                continue
            if f:
                ctype = key
                if ctype == "h":
                    type = "homework"
                elif ctype == "g":
                    type = "goals"
                elif ctype == "t":
                    type = "tech"
                break
            f.close()

        if ctype in ["h", "g", "t"]:
            # Authing if real db
            line = subprocess.check_output(
                ["file", "/root/Documents/Shadochan/todo/{}.{}.db".format(args['FILE'], ctype)])
            if "SQLite" in str(line):
                print("File Validity: True")
                if args['--cat']:
                    category = str(args['--cat'])
                else:
                    category = None
                results = list(args['FILE'], type, ctype, category)
                print(tabulate(results, headers, tablefmt="fancy_grid", showindex="always"))
            else:
                print("  |-------------------------|  ")
                print("-<|      Invalid File       |>-")
                print("-<| shadochan todo new FILE |>-")
                print("  |-------------------------|  ")
        else:
            print("  |-------------------------|  ")
            print("-<|     File not found      |>-")
            print("-<| shadochan todo new FILE |>-")
            print("  |-------------------------|  ")

    elif args['add']:
        # Determine if file exists
        ctype = None
        for key in ["h", "g", "t"]:
            try:
                f = open("/root/Documents/Shadochan/todo/{}.{}.db".format(args['FILE'], key), "r")
            except FileNotFoundError:
                continue
            if f:
                ctype = key
                if ctype == "h":
                    type = "homework"
                elif ctype == "g":
                    type = "goals"
                elif ctype == "t":
                    type = "tech"
                break
            f.close()

        if ctype in ["h", "g", "t"]:
            # Authing if real db
            line = subprocess.check_output(
                ["file", "/root/Documents/Shadochan/todo/{}.{}.db".format(args['FILE'], ctype)])
            if "SQLite" in str(line):
                print("File Validity: True")
                category = str(args['<category>'])
                due_date = str(args['<due_date>'])
                description = str(args['<description>'])
                if args['--notes']:
                    notes = str(args['--notes'])
                else:
                    notes = None
                add(type, args['FILE'], category, due_date, description, notes)
            else:
                print("  |-------------------------|  ")
                print("-<|      Invalid File       |>-")
                print("-<| shadochan todo new FILE |>-")
                print("  |-------------------------|  ")
        else:
            print("  |-------------------------|  ")
            print("-<|     File not found      |>-")
            print("-<| shadochan todo new FILE |>-")
            print("  |-------------------------|  ")

    elif args['delete']:
        # Determine if file exists
        ctype = None
        for key in ["h", "g", "t"]:
            try:
                f = open("/root/Documents/Shadochan/todo/{}.{}.db".format(args['FILE'], key), "r")
            except FileNotFoundError:
                continue
            if f:
                ctype = key
                if ctype == "h":
                    type = "homework"
                elif ctype == "g":
                    type = "goals"
                elif ctype == "t":
                    type = "tech"
                break
            f.close()

    if ctype in ["h", "g", "t"]:
        # Authing if real db
        line = subprocess.check_output(
            ["file", "/root/Documents/Shadochan/todo/{}.{}.db".format(args['FILE'], ctype)])
        if "SQLite" in str(line):
            print("File Validity: True")
            results = tabulate(list(args['FILE'], type, ctype,
                                    category=None), headers, tablefmt="fancy_grid", showindex="always")
            print(results)
            ln = int(input("Which line would you like to delete Shado-kun: \n$(-)>  "))
            delete(type, args['FILE'], ln)
        else:
            print("  |-------------------------|  ")
            print("-<|      Invalid File       |>-")
            print("-<| shadochan todo new FILE |>-")
            print("  |-------------------------|  ")
    else:
        print("  |-------------------------|  ")
        print("-<|     File not found      |>-")
        print("-<| shadochan todo new FILE |>-")
        print("  |-------------------------|  ")


def calc(args):
    vq = 0
    if args['-v']:
        vq = 1
    elif args['-q']:
        vq = -1

    if args['add']:
        print(calc_add(args['<x>'], args['<y>'], vq))
    elif args['sub']:
        print(calc_sub(args['<x>'], args['<y>'], vq))
    elif args['mul']:
        print(calc_mul(args['<x>'], args['<y>'], vq))
    elif args['div']:
        print(calc_div(args['<x>'], args['<y>'], vq))
    elif args['sqr']:
        print(calc_sqr(args['<x>'], vq))
    elif args['cub']:
        print(calc_cub(args['<x>'], vq))
    elif args['exp']:
        print(calc_exp(args['<x>'], args['<y>'], vq))


if __name__ == '__main__':
    args = docopt(__doc__, version='  |---------------|  \n-<| Shadochan 1.0 |>-\n  |---------------|  ')
    if args['spent']:
        spend_track(args)
    if args['todo']:
        todo(args)
    if args['calc']:
        calc(args)
