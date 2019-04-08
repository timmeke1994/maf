from flask import Flask, render_template, request, make_response, redirect
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
import authomatic
import logging
import requests
from config import CONFIG
# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, '', report_errors=False)
userid = ""

app = Flask(__name__, template_folder='.')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    global userid
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name) 
    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
            userid = result.user.id
            exist = int(requests.get("http://192.168.37.129:5000/api/user/exist/"+userid).content)
            if exist != 0:
                ##Gebruiker bestaat al
                info = requests.get("http://192.168.37.129:5000/api/user/number/"+userid).json()
                cn = info['_id']
                adc = info['address']['city']
                ads = info['address']['street']
                adz = info['address']['zipcode']
                mail = info['email']
                fn = info['name']['first_name']
                ln = info['name']['last_name']
                return render_template('login.html', result=result, customernumber=cn, city=adc, street=ads, zipcode=adz, email=mail, firstname=fn, lastname=ln)
            else:
                #Gebruiker bestaat nog niet
                return redirect('/register')
        # The rest happens inside the template.
        
    # Don't forget to return the response.
    return response

@app.route('/register', methods=['POST', 'GET'])
def register():
    global userid
    if request.method == 'POST':
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        email = request.form.get('emailaddress')
        street = request.form.get('street')
        zipcode = request.form.get('zipcode')
        city = request.form.get('city')
        data = {'customernr': str(userid),'first_name': str(first_name),'last_name': str(last_name),'email': str(email),'street': str(street),'city': str(city),'zipcode': str(zipcode)}
        while first_name and last_name and email and street and zipcode and city !="":
            # Alle velden zijn ingevuld
            requests.post('http://192.168.37.129:5000/api/user/new', data=data)
            return render_template("return.html", registered=False, customernumber=userid, firstname=first_name, lastname=last_name, mail=email, street=street, zipcode=zipcode,city=city)
        else:
            # Een of meerdere velden zijn nog niet ingevuld
            return render_template("register.html")
    else:
        return render_template('register.html')

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global userid
    if request.method == 'POST':
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        email = request.form.get('emailaddress')
        street = request.form.get('street')
        zipcode = request.form.get('zipcode')
        city = request.form.get('city')
        data = {'first_name': str(first_name),'last_name': str(last_name),'email': str(email),'street': str(street),'city': str(city),'zipcode': str(zipcode)}
        while first_name and last_name and email and street and zipcode and city !="":
            requests.put('http://192.168.37.129:5000/api/user/number/'+userid, data=data)
            return render_template("return.html", registered=True, customernumber=userid, firstname=first_name, lastname=last_name, mail=email, street=street, zipcode=zipcode,city=city)
        else:
            return render_template("edit.html")
    else:
        return render_template("edit.html")

# Run the app on port 5000 on all interfaces, accepting only HTTPS connections
if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', host='0.0.0.0', port=5000)