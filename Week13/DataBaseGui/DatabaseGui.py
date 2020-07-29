import sqlite3
from sqlite3 import Error
import tkinter as tk

window = tk.Tk()
window.title("Database")
window.geometry("300x300")
fname: str = 'None'
lname: str = 'None'

firstnamebox = tk.Entry(window)
Lastnamebox = tk.Entry(window)
dataButton = tk.Button(window, text="Create Database", command=lambda: CreateDatabaseTable("pythonsqlite.db"))
returnButton = tk.Button(window, text="Return Database",
                         command=lambda: select_all_persons(CreateDatabaseTable("pythonsqlite.db")))

person = ('Matt', 'Gerling')
createButton = tk.Button(window, text="Create Person",
                         command=lambda: create_person(CreateDatabaseTable("pythonsqlite.db"), person))

dataButton.grid(row=0, column=0, columnspan=5)
createButton.grid(row=1, column=0, columnspan=5)
firstnamebox.grid(row=1, column=6, columnspan=5)
Lastnamebox.grid(row=2, column=6, columnspan=5)
returnButton.grid(row=4, column=0, columnspan=5)


def CreateDatabaseTable(db):
    """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid  # returns the row id of the cursor object, the person id]


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows  # return the rows


def ReturnRows():
    conn = CreateDatabaseTable("pythonsqlite.db")
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)


window.mainloop()
