from flask import Flask,render_template,request,redirect,url_for,flash
import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',password='sreevedh@13112019',database='taskmanagement')
mycursor = connection.cursor()
user_dict={'admin':'1234','deepa':'4567'}

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('task_index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/emp_home', methods=['POST'])
def emp_home():
    username=request.form['username']
    pwd=request.form['password']
    if username not in user_dict:
        return render_template('login.html', msg='Invalid Username')
    elif user_dict[username]!=pwd:
        return render_template('login.html', msg='Invalid Password')
    else:
         return projects()

@app.route('/staff')
def staff():
    query = "SELECT * FROM staff"
    mycursor.execute(query)
    data = mycursor.fetchall()
    return render_template('staff.html',sqldata=data)

@app.route('/projects')
def projects():
    query = "SELECT * FROM projects"
    mycursor.execute(query)
    data = mycursor.fetchall()
    return render_template('projects.html',sqldata=data)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_projects')
def add_projects():
    return render_template('update.html')


@app.route('/register',methods=['GET','POST'])
def read():
    if request.method=='POST':
        name=request.form.get('name')
        staff_id=request.form.get('staff_id')
        dept=request.form.get('dept')
        mail_id=request.form.get('mail_id')
     

        query="INSERT INTO staff VALUES (%s,%s,%s,%s)"
        data=(name,staff_id,dept,mail_id)

        
        mycursor.execute(query,data)
        connection.commit()
        return staff()

@app.route('/addProject',methods=['GET','POST'])
def addProject():
    if request.method=='POST':
       
        project=request.form.get('project')
        in_charge=request.form.get('in_charge')
        starting_date=request.form.get('starting_date')
        due_date=request.form.get('due_date')
        status=request.form.get('status')
     

        query="INSERT INTO projects VALUES (%s,%s,%s,%s,%s)"
        data=(project,in_charge,starting_date,due_date,status)

        mycursor.execute(query,data)
        connection.commit()
        return projects()
    return render_template('task_update.html')
   
    

 
    

    
    
@app.route('/delete/<string:project>',methods=['GET','POST'])
def delete(project):
    
             

        query="DELETE FROM staff WHERE project= %S"
             

        mycursor.execute(query,project)
        connection.commit()
        return projects()
    
    


   


if __name__=='__main__':
    app.run(debug=True)

