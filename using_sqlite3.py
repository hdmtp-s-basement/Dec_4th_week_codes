from using_sqlite import *

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2021-12-28','LOL','BWAN',108,33.09)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()