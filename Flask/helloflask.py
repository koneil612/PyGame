from flask import Flask,render_template
import mysql.connector

app = Flask("MyApp")

conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='demo')

cur = conn.cursor()

@app.route('/')
def hello():
    query = ("SELECT id,name FROM student")

    cur.execute(query)

    list = cur.fetchall()

    # print list
    return render_template('students.html', student_list=list, title="Student List")


if __name__ == '__main__':
    app.run(debug=True)

cur.close()
conn.close()
