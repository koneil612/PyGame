from flask import Flask,render_template, request, redirect
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

    return render_template("phonebook.html", phonebook_list=list, title="Christmas Card List", q=q)


@app.route('/new_entry')
def new_entry():
    return render_template("new_entry.html")

@app.route('/submit_new_entry', methods=['POST'])
def submit_new_entry():
    name=request.form.get('name')
    address=request.form.get('address')
    city=request.form.get('city')
    state=request.form.get('state')
    zip=request.form.get('zip')
    query= "INSERT INTO phonebook (name, address, city, state,zip) values ('%s','%s','%s','%s','%s')" % (name, address, city, state, zip)
    cur.execute(query)
    conn.commit()
    return render_template("submit_new_entry.html", name=name, address=address, city=city, state=state, zip=zip)

@app.route('/update_entry', methods=['GET'])
def update_entry():
    id=request.args.get('id')
    query = "SELECT id, name, address, city, state, zip FROM phonebook WHERE id=%s" %id
    cur.execute(query)
    list = cur.fetchone()
    id=list[0]
    name=list[1]
    address=list[2]
    city=list[3]
    state=list[4]
    zip=list[5]
    return render_template("update_entry.html", name=name, address=address, city=city, state=state, zip=zip,id=id)

@app.route('/submit_update_entry', methods=['POST', 'GET'])
def submit_update_entry():
    id=request.form.get('id')
    name=request.form.get('name')
    address=request.form.get('address')
    city=request.form.get('city')
    state=request.form.get('state')
    zip=request.form.get('zip')
    query= "UPDATE phonebook SET name = '%s', address='%s', city='%s', state='%s', zip='%s' WHERE id = %s" % (name, address, city, state, zip, id)
    cur.execute(query)
    conn.commit()
    return render_template("submit_update_entry.html", name=name)

@app.route("/delete_contact",methods=["GET"])
def delete_contact():
    id=request.args.get('id')
    query = ("DELETE from phonebook where id=%s" % id)
    cur.execute(query)
    conn.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)

cur.close()
conn.close()
