import ar_master
import os
from flask import Flask, render_template, request, session, Response, current_app, send_from_directory, url_for
app = Flask(__name__, static_folder='static',template_folder='templates',static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'change-this-development-key')
mm = ar_master.master_flask_code()
@app.route("/")
def homepage():
    return render_template('index.html',result='---')

@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html',result='---')


@app.route("/doctor_home")
def doctor_home():
    return render_template('doctor_home.html',result='---')


@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    if request.method == 'POST':
        un = request.form['username']
        pa = request.form['password']
        usern = mm.select_direct_query("select * from admin_details where username='" + str(un) + "' and password='" + str(pa) + "'")
        if usern:
            session['username'] = usern
            return render_template('admin_home.html', flash_message=True,data="Login Success")
        else:
            return render_template('admin.html', flash_message=True,data="Login Failed")
    return render_template('admin.html')



@app.route("/doctor", methods = ['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        un = request.form['username']
        pa = request.form['password']
        usern = mm.select_direct_query("select * from doctor_details where name='" + str(un) + "' and password='" + str(pa) + "'")
        if usern:
            session['username'] = usern
            return render_template('doctor_home.html', flash_message=True,data="Login Success")
        else:
            return render_template('doctor.html', flash_message=True,data="Login Failed")
    return render_template('doctor.html')



@app.route("/donar", methods = ['GET', 'POST'])
def donar():
    if request.method == 'POST':
        un = request.form['username']
        pa = request.form['password']
        usern = mm.select_direct_query("select * from donar_details where name='" + str(un) + "' and password='" + str(pa) + "'")
        if usern:
            session['username'] = usern
            return render_template('donar_home.html', flash_message=True,data="Login Success")
        else:
            return render_template('donar.html', flash_message=True,data="Login Failed")
    return render_template('donar.html')



@app.route("/admin_add_doctor",methods = ['GET', 'POST'])
def admin_add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        qualification = request.form['qualification']
        age = request.form['age']
        specialization = request.form['specialization']
        experiance = request.form['experiance']

        address = request.form['address']
        mail = request.form['mail']
        password = request.form['password']

        maxid = mm.find_max_id("doctor_details")
        qry=("insert into doctor_details values('" + str(maxid) + "','" + str(name) + "','" + str(qualification) + "','" + str(age) + "','" + str(specialization) + "','" + str(experiance) + "','" + str(address) + "','" + str(mail) + "','" + str(password) + "','0','0')")
        result=mm.insert_query(qry)
        if (result == 1):
            return render_template('admin_add_doctor.html',msg="Registered Successfully")
    return render_template('admin_add_doctor.html')



@app.route("/doctor_add_patient", methods = ['GET', 'POST'])
def doctor_add_patient():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        dob = request.form['dob']
        age = request.form['age']
        password = request.form['password']

        maxin = mm.find_max_id("patient_details")
        qq = "insert into patient_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(email) + "','" + str(address) + "','" + str(gender) + "','"+str(dob)+"','"+str(age)+"','"+str(password)+"')"
        mm.insert_query(qq)
        return render_template('doctor_add_patient.html', flash_message=True, data="Registration Successfully")
    return render_template('doctor_add_patient.html')


@app.route("/donar_register", methods = ['GET', 'POST'])
def donar_register():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        dob = request.form['dob']
        age = request.form['age']
        password = request.form['password']

        maxin = mm.find_max_id("donar_details")
        qq = "insert into donar_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(email) + "','" + str(address) + "','" + str(gender) + "','"+str(dob)+"','"+str(age)+"','"+str(password)+"')"
        mm.insert_query(qq)
        return render_template('donar_register.html', flash_message=True, data="Registration Successfully")
    return render_template('donar_register.html')



if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true', use_reloader=False)