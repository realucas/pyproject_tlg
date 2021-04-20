# standard library
import sqlite3 as sql

# python3 -m pip install flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

# return home.html (landing page)
@app.route('/')
def home():
    return render_template('home.html')

# return student.html (a way to add a student to our sqliteDB)
@app.route('/enternew')
def new_student():
    return render_template('asset.html')

@app.route('/enterticket')
def new_tik():
    return render_template('tickets.html')

# if someone uses student.html it will generate a POST
# this post will be sent to /addrec
# where the information will be added to the sqliteDB
@app.route('/addrec',methods = ['POST'])
def addrec():
    try:
        hostname = request.form['hostname']         # Hostname
        ipaddr = request.form['ipaddr']     # IP address
        location = request.form['location']     # Location
        notes = request.form['notes']       # notes

        # connect to sqliteDB
        with sql.connect("database.db") as con:
            cur = con.cursor()

            # place the info from our form into the sqliteDB
            cur.execute("INSERT INTO assets (hostname,ipaddr,location,notes) VALUES (?,?,?,?)",(hostname,ipaddr,location,notes) )
            # commit the transaction to our sqliteDB
            con.commit()
        # if we have made it this far, the record was successfully added to the DB
        #msg = "Record successfully added"
        
    except:
        con.rollback()  # this is the opposite of a commit()
        #msg = "error in insert operation"    # we were NOT successful

    finally:
        con.close()     # successful or not, close the connection to sqliteDB
        return redirect('/list')    #

@app.route('/addticket',methods = ['POST'])
def addticket():
    try:
        name = request.form['name']         # name of requestor
        email = request.form['email']     # email address
        department = request.form['department']     # department
        description = request.form['description']       # description of the issue

        # connect to sqliteDB
        with sql.connect("database.db") as con:
            cur = con.cursor()

            # place the info from our form into the sqliteDB
            cur.execute("INSERT INTO tickets (name,email,department,description) VALUES (?,?,?,?)",(name,email,department,description) )
            # commit the transaction to our sqliteDB
            con.commit()
        # if we have made it this far, the record was successfully added to the DB
        #msg = "Record successfully added"
        
    except:
        con.rollback()  # this is the opposite of a commit()
        #msg = "error in insert operation"    # we were NOT successful

    finally:
        con.close()     # successful or not, close the connection to sqliteDB
        return redirect('/listtickets')    #

# return all entries from our sqliteDB as HTML
@app.route('/list')
def list_assets():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from assets")           # pull all information from the table "assets"
    
    rows = cur.fetchall()
    return render_template("list.html",rows = rows) # return all of the sqliteDB info as HTML

@app.route('/listtickets')
def list_tickets():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from tickets")           # pull all information from the table "tickets"
    
    rows = cur.fetchall()
    return render_template("listtickets.html",rows = rows) # return all of the sqliteDB info as HTML

if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        con = sql.connect('database.db')
        print("Opened database successfully")
        # ensure that the table assets is ready to be written to
        con.execute('CREATE TABLE IF NOT EXISTS assets (hostname TEXT, ipaddr TEXT, location TEXT, notes TEXT)')
        con.execute('CREATE TABLE IF NOT EXISTS tickets (name TEXT, email TEXT, department TEXT, description TEXT)')
        print("Table created successfully")
        con.close()
        # begin Flask Application 
        app.run(debug = True)
    except:
        print("App failed on boot")
