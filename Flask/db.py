import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='demo')
# opens the connecton
cur = conn.cursor()


# command that passes into the database
query = ("SELECT id,name FROM student")

# does the command: puts the database into the cursor (its a list at this point)
cur.execute(query)

# passing each of the lists into the forms. doens't need to be (for id it can be for studentId) the print is what is pulling the information
for (id, name) in cur:
  print "%s. %s" % (id, name)

cur.close()
conn.close()
