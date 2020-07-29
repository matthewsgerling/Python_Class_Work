import sqlite3
from sqlite3 import Error


def create_connection(db):
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
    return cur.lastrowid # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    with conn:
        person1 = ('Rob', 'Thomas')
        person_id1 = create_person(conn, person1)
        person2 = ('Matt', 'Gerling')
        person_id2 = create_person(conn, person2)
        person3 = ('Logan', 'Jones')
        person_id3 = create_person(conn, person3)
        person4 = ('Caleb', 'Thomas')
        person_id4 = create_person(conn, person4)

        student = (person_id1, 'Songwriting', '2000-01-01')
        student_id1 = create_student(conn, student)
        student = (person_id2, 'Songwriting', '2000-01-01')
        student_id2 = create_student(conn, student)
        student = (person_id3, 'Songwriting', '2000-01-01')
        student_id3 = create_student(conn, student)
        student = (person_id4, 'Songwriting', '2000-01-01')
        student_id4 = create_student(conn, student)
