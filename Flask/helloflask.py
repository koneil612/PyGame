from flask import Flask,render_template, request
import mysql.connector

app = Flask("MyApp")

conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='demo')

cur = conn.cursor()

@app.route('/')
def home():
    query = ("SELECT id,name FROM student")
    cur.execute(query)
    list = cur.fetchall()
    q=request.args.get('q')
    # print list
    return render_template("students.html", student_list=list, title="Student List", q=q)

@app.route('/new_student')
def new_student():
    return render_template("new_student.html")

@app.route('/submit_new_student', methods=['POST'])
def submit_new_student():
    name=request.form.get('name')
    website=request.form.get('website')
    github_username=request.form.get('github_username')
    query= ("insert into student (name) values (\"%s\")"%name)
    cur.execute(query)
    conn.commit()
    return render_template("submit_new_student.html", name=name, website=website, github_username=github_username)

if __name__ == '__main__':
    app.run(debug=True)

cur.close()
conn.close()
