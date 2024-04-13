from flask import Flask,render_template,flash,session,request,redirect


import sqlite3

app=Flask(__name__)
app.secret_key="123"


sqlconnection =sqlite3.connect("sancart.db")
sqlconnection.execute('''CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            address TEXT NOT NULL,
            address1 TEXT NOT NULL,
            city TEXT NOT NULL,
            region TEXT NOT NULL,
            postal TEXT NOT NULL
        )
    ''')
sqlconnection.close()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about us.html")

@app.route('/cartpage')
def cartpage():
    return render_template("cart page.html")

@app.route('/cleaning')
def cleaning():
    return render_template("cleaning.html")

@app.route('/cookies')
def cookies():
    return render_template("cookies.html")

@app.route('/empty payment')
def emptypayment():
    return render_template("empty payment.html")

@app.route('/fruits and vegetables')
def fruitsandvegetables():
    return render_template("fruits and vegetables.html")

@app.route('/ice creams')
def icecream():
    return render_template("ice creams.html")

# Login Module
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        conn =sqlite3.connect("sancart.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE email = ? AND phone = ?", (email,phone))
        user = cur.fetchone()
        conn.close()

        if user:
            #session['username'] = user['fullname']
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password', 'danger')
            return redirect('/login')

    return render_template('login.html')
@app.route('/makeup')
def makeup():
    return render_template("makeup.html")

@app.route('/masala')
def masala():
    return render_template("masala.html")

@app.route('/milks')
def milks():
    return render_template("milks.html")

@app.route('/munchies')
def munchies():
    return render_template("munchies.html")

@app.route('/oats')
def oats():
    return render_template("oats.html")

@app.route('/odering confirm')
def oderingconfirm():
    return render_template("odering confirm.html")

@app.route('/packaged')
def packaged():
    return render_template("packaged.html")

@app.route('/payment')
def payment():
    return render_template("paymentown.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        birth = request.form['birth']
        gender = request.form['gender']
        address = request.form['address']
        address1 = request.form['address1']
        city = request.form['city']
        region = request.form['region']
        postal = request.form['postal']

        conn =sqlite3.connect("sancart.db")
        conn.execute('''
            INSERT INTO user (fullname, email, phone, birth, gender, address, address1, city, region, postal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (fullname, email, phone, birth, gender, address, address1, city, region, postal))
        conn.commit()
        conn.close()

        flash('Signup successful!', 'success')
        return redirect('/submit')
    
    return render_template('register.html')


       



   
       

@app.route('/rice and atta')
def riceandatta():
    return render_template("rice and atta.html")

@app.route('/sauses')
def sauses():
    return render_template("sauses.html")

@app.route('/submit')
def sabmit():
    return render_template("submit.html")

@app.route('/sweets')
def sweets():
    return render_template("sweets.html")

@app.route('/tea and cofee')
def teaandcofee():
    return render_template("tea and cofee.html")
    

if __name__ == '__main__':
    app.run(debug=True)