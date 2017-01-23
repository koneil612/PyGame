from flask import Flask,render_template, request, redirect, session

import mysql.connector

app = Flask("MyApp")
app.secret_key = 'alkj'

conn = mysql.connector.connect(
         user='jrrydbspeyhsdm',
         password='dbcc418026d62a27ce58eced992becf2a36a4a36ea572b0a32b939f978f33a91',
         host='ec2-54-163-234-4.compute-1.amazonaws.com',
         database='d22p7l07ohqiie')

cur = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect('/home')
    else:
        return render_template("submit_login.html")

@app.route('/submit_login', methods=['GET','POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    query = ("SELECT username, password FROM myuser WHERE username = '%s'" % username)
    cur.execute(query)
    # result_list = namedresult()
    result_list = cur.fetchone()
    # q=request.args.get('q')
    if result_list and len(result_list) > 0:
        username = result_list[0]
        if result_list[1]== password:
            #successfully logged in
            session['username'] = username
            return redirect('/home')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    del session['username']
    return redirect('/')

@app.route('/home', methods= ['GET', 'POST'])
def home():
    # if not logged in
    #redir to login
    if 'username' not in session:
        return redirect('/submit_login')

    query = ("SELECT id, firstname, lastname, address, address2, city, state, zip FROM phonebook")
    cur.execute(query)
    list = cur.fetchall()
    q=request.args.get('q')
    # print list

    return render_template("phonebooklisting.html", phonebook_list=list, title="Christmas Card List", q=q)

@app.route('/phonebook', methods= ['GET'])
#pulls all the listings in the phonebook
def phonebook():
    query = ("SELECT id, firstname, lastname, address, address2, city, state, zip FROM phonebook")
    cur.execute(query)
    list = cur.fetchall()
    q=request.args.get('q')
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
    query= "INSERT INTO phonebook (firstname, lastname, address, address2, city, state,zip) values ('%s','%s','%s','%s','%s','%s','%s')" % ((Database.escape(firstname)), (Database.escape(lastname)), (Database.escape(address)), (Database.escape(address2)), (Database.escape(city)), (Database.escape(state)), zip)
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
    query= "UPDATE phonebook SET firstname = '%s', lastname='%s', address='%s', address2='%s', city='%s', state='%s', zip='%s' WHERE id = %s" % ((Database.escape(firstname)), (Database.escape(lastname)), (Database.escape(address)), (Database.escape(address2)), (Database.escape(city)), (Database.escape(state)), zip, id)
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


class Database(object):
    @staticmethod
    def escape(value):
        return value.replace("'","''")

if __name__ == '__main__':
    app.run(debug=True)




cur.close()
conn.close()
