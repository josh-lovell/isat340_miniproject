__author__ = 'Tony Teate'

#imports
import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for

#instantiate
app = Flask(__name__)
# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username=''
        password=''
        conn=sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM logininfo''')
        row = c.fetchall()
        if row:
            i=0
            while i != 2: #must be equal to number of members
                username = row[i]
                print (username)
                i+=1
                if request.form['username'] != username[0] or request.form['password'] != username[1]:
                    error = 'Invalid Credentials. Please try again.'
                else:
                    return redirect(url_for('info'))
                conn.close()
    return render_template('login.htm', error=error)

@app.route('/info', methods=['GET', 'post'])
def info():
        memberID=None
        firstname=''
        lastname=''
        age=None
        email=''
        bio=''
        success=False

        if request.method == 'GET':
            conn=sqlite3.connect('celebrities.db')
            c = conn.cursor()
            c.execute('''SELECT * FROM members''')
            row = c.fetchone()
            if row:
                memberID=row[0]
                firstname=row[1]
                lastname=row[2]
                age = row[3]
                email=row[4]
                bio=row[5]
            conn.close()

        if request.method == 'POST':
            memberID = request.form['memberID']
            firstname= request.form['firstname']
            lastname=request.form['lastname']
            age=request.form['age']
            email=request.form['email']
            bio=request.form['bio']
            success=True
            conn=sqlite3.connect('celebrities.db')
            c = conn.cursor()
            c.execute('''SELECT * FROM members''')
            row = c.fetchone()
            if row:
                c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ?, WHERE memberID=?''',
                    (firstname, lastname, age, email, bio, memberID))
            else:
                c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)''',
                    (memberID, firstname, lastname, age, email, bio))
            conn.commit()
            conn.close()
        return render_template('profile.html', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)
            
@app.route('/view_all_celebs')
def view_all():
    celebID=None
    firstname=''
    lastname=''
    age=''
    email=''
    photo=''
    bio=''

    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')
    rows = c.fetchall()
    conn.close()
    return render_template('view_all_celebs.html',
rows=rows)

@app.route('/view_one_celeb')
def view_one():
    celebID=None
    firstname=''
    lastname=''
    age=''
    email=''
    photo=''
    bio=''
    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')#change ORDER BY to WHERE celebid=# of desired celeb
    row = c.fetchone()
    if row:
        celebID = row[0]
        firstname = row[1]
        lastname = row[2]
        age = row[3]
        email = row[4]
        photo = row[5]
        bio = row[6]
    conn.close()
    return render_template('view_one_celeb.html', celebID=celebID, firstname = firstname, lastname = lastname, age=age,
    email=email, photo=photo, bio=bio)

def get(request):
    pass

def post(request):
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug=False)
