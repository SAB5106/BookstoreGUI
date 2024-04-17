import sqlite3

def connect():
    db = sqlite3.connect("books.db")
    crsr = db.cursor()
    crsr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    db.commit()
    db.close()

def view():
    db = sqlite3.connect("books.db")
    crsr = db.cursor()
    crsr.execute("SELECT * FROM book")
    rows = crsr.fetchall()
    db.close()
    return rows

def search(title="",author="",year="",isbn=""):
    db = sqlite3.connect("books.db")
    crsr = db.cursor()
    crsr.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows = crsr.fetchall()
    db.close()
    return rows

def add(title,author,year,isbn):
    db = sqlite3.connect("books.db")
    crsr = db.cursor()
    crsr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    db.commit()
    db.close()

def update(id,title,author,year,isbn):
    db = sqlite3.connect("books.db")
    crsr = db.cursor()
    crsr.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    db.commit()
    db.close()

def delete(id):
    db = sqlite3.connect("books.db")
    crsr = db.cursor()
    crsr.execute("DELETE FROM book WHERE id=?",(id,))
    db.commit()
    db.close()