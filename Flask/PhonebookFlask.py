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
    query = ("SELECT id, name, address, city, state, zip FROM phonebook")
    cur.execute(query)
    list = cur.fetchall()
    q=request.args.get('q')
    # print list
    return render_template("phonebook.html", phonebook_list=list, title="Phonebook List", q=q)

@app.route('/new_entry')
def new_entry():
    return render_template("new_entry.html")

@app.route('/submit_new_entry', methods=['POST'])
def submit_new_entry():
    name=request.form.get('name')
    address=request.form.get('address')
    city=request.form.get('city')
    state=request.form.get('state')
    zip=request.form.get('state')
    query= ("insert into phonebook (name, address, city), (state),(zip) values (\"%s\") (\"%s\") (\"%s\") (\"%s\")(\"%s\")" % (name, address, city, state, zip)
    cur.execute(query)
    conn.commit()
    return render_template("submit_new_entry.html", name=name, address=address, city=city, state=state, zip=zip)

if __name__ == '__main__':
    app.run(debug=True)

cur.close()
conn.close()
