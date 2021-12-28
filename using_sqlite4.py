from using_sqlite import *

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

#https://docs.python.org/3/library/sqlite3.html