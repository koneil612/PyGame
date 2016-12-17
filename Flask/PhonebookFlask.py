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
    query = ("SELECT id, firstname, lastname, address, address2, city, state, zip FROM phonebook")
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
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    address=request.form.get('address')
    address2=request.form.get('address2')
    city=request.form.get('city')
    state=request.form.get('state')
    zip=request.form.get('zip')
    query= "INSERT INTO phonebook (firstname, lastname, address, address2, city, state,zip) values ('%s','%s','%s','%s','%s','%s','%s')" % (firstname, lastname, address, address2, city, state, zip)
    cur.execute(query)
    conn.commit()
    return render_template("submit_new_entry.html", firstname=firstname, lastname=lastname, address=address, address2=address2, city=city, state=state, zip=zip)

@app.route('/update_entry', methods=['GET'])
def update_entry():
    id=request.args.get('id')
    query = "SELECT id, firstname, lastname, address, address2, city, state, zip FROM phonebook WHERE id=%s" %id
    cur.execute(query)
    list = cur.fetchone()
    id=list[0]
    firstname=list[1]
    lastname=list[2]
    address=list[3]
    address2=list[4]
    city=list[5]
    state=list[6]
    zip=list[7]
    return render_template("update_entry.html", firstname=firstname, lastname=lastname, address=address, address2=address2, city=city, state=state, zip=zip,id=id)

@app.route('/submit_update_entry', methods=['POST', 'GET'])
def submit_update_entry():
    id=request.form.get('id')
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    address=request.form.get('address')
    address2=request.form.get('address2')
    city=request.form.get('city')
    state=request.form.get('state')
    zip=request.form.get('zip')
    query= "UPDATE phonebook SET firstname = '%s', lastname='%s', address='%s', address2='%s', city='%s', state='%s', zip='%s' WHERE id = %s" % (firstname, lastname, address, address2, city, state, zip, id)
    cur.execute(query)
    conn.commit()
    return render_template("submit_update_entry.html", firstname=firstname)

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
