import json
import sqlite3

conn = sqlite3.connect('many_to_many.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT
);

CREATE TABLE Member (
    user_id INTRGER,
    Course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, Course_id)
);
''')

fh = 'roster_data.json'
str_data = open(fh).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
    cur.execute('SELECT id FROM User WHERE name= ?', (name, ))
    user_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title, ))
    cur.execute('SELECT id FROM Course WHERE title= ?', (title, ))
    Course_id = cur.fetchone()[0]
    cur.execute("""INSERT OR REPLACE INTO Member (user_id, Course_id, role)
    VALUES(?, ?, ?)""", (user_id, Course_id, role))
    conn.commit()
