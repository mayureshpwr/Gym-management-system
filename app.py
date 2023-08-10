from flask import *
from controls.users import users


app = Flask(__name__)

user = users()

@app.route('/')
def index():    
    data = user.get_trainner()
    return render_template("index.html",data=data)

    		
@app.route('/pricingplan')
def pricingplan():
    return render_template("pricingplan.html")

@app.route('/pricing')
def pricing(): 
    return render_template("pricing.html")

@app.route('/trainers.')
def trainers():    
    return render_template("trainers.html")


    # if request.method == 'POST':
    #     # do stuff when the form is submitted

    #     # redirect to end the POST handling
    #     # the redirect can be to the same route or somewhere else
    #     return redirect(url_for('index'))

    # show the form, it wasn't submitted
    # return render_template('cool_form.html')

@app.route('/Register',methods=['GET','POST'])
def Register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user_pass = request.form['password']
        result = user.Register(username,email,user_pass)
        print(result)
        if result == True:
            return redirect(url_for('Login'))            
        else:                       
            return redirect(url_for('Register'))
    
    return render_template("Register.html")


@app.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        user_pass = request.form['password']
        result = user.Login(email,user_pass)
        print(result)
        if result == True:
            return redirect(url_for('userHome'))            
        else:                       
            return redirect(url_for('Login'))
    
    return render_template("Login.html")

@app.route('/userHome')
def userHome():
	if session.get('loggedIn') == True:
		curr_user = user.SingleUser()					
		data = curr_user	
		return render_template('user/userhome.html',data=data)
	else:
    		return redirect(url_for('Login'))

@app.route('/user_logout')
def user_logout():
   # remove the username from the session if it is there
   session.pop('username',None)
   session.pop('user_id',None)
   session.pop('loggedIn', None)   
   return redirect(url_for('Login'))



app.secret_key = 'mp_fits'
if __name__ == "__main__":
    app.run(debug=True)