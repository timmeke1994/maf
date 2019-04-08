#!/usr/bin/python

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

# hieronder importeer je al je functies
from database import *

app = Flask(__name__)
api = Api(app)
dbcustomers = Databasemongo()
parser = reqparse.RequestParser()
# Argumenten die je via curl en de methoden PUT en POST via "-d" kan meegeven, bv:
# curl http://192.168.37.129:5000/url/url -d "name=jan" -d "street=kerkstraat" -X POST
parser.add_argument('customernr')
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('email')
parser.add_argument('street')
parser.add_argument('city')
parser.add_argument('zipcode')
parser.add_argument('trainingresult')
# hier de overige argumenten ook zo benoemen


class MAFUserNew(Resource):
    # Maak een nieuwe user aan
    # curl http://192.168.37.129:5000/api/user/new -d "name=jan" -d "street=kerkstraat" -X POST
    def post(self):
        args = parser.parse_args()
        cn = args['customernr']
        fn = args['first_name']
        ln = args['last_name']
        ma = args['email']
        ads = args['street']
        adc = args['city']
        adz = args['zipcode']
        # hier roep je de functie aan voor het aanmaken van een nieuwe user
        dbcustomers.insert(cn,fn,ln,ma,ads,adc,adz)
        return {'status': 'ok'}


class MAFUserNumber(Resource):
    # Verwijder de user
    # curl http://192.168.37.129:5000/api/user/number/3 -X DELETE
    def delete(self, customernumber):
        # hier roep je de functie aan voor het verwijderen van een user
        dbcustomers.delete(str(customernumber))
        return {'status': 'ok'}

    # Voeg een trainingresultaat toe
    # curl http://192.168.37.129:5000/api/user/number/3 -d "trainingresults=3101" -X PUT
    def put(self, customernumber):
        args = parser.parse_args()
        fn = args['first_name']
        ln = args['last_name']
        ma = args['email']
        ads = args['street']
        adc = args['city']
        adz = args['zipcode']
        # hier een variabele toekennen aan elk argument, bv c = args['code'] etc.
        dbcustomers.updatecus(customernumber,fn,ln,ma,ads,adc,adz)
        return {'status': 'ok'}

    # Vraag informatie op over de user
    # curl http://192.168.37.129:5000/api/user/number/3
    def get(self, customernumber):
        x = dbcustomers.select(customernumber)
        # return x: een stukje json met daarin informatie over de user, dus niet onderstaande regel
        return x

class MAFUserExist(Resource):
    # Kijkt of de gebruiker bestaat
    # curl http://192.168.37.129:5000/api/user/exist/1
    def get(self,customernumber):
        x = dbcustomers.countdoc(customernumber)
        return x
##
## Elke url moet je hieronder apart definieren, dus /api/user/new  of /api/user/name
## Als een deel van de url een variabele is dan tussen vishaken, bv <user_name>
##
api.add_resource(MAFUserNew, '/api/user/new')
api.add_resource(MAFUserNumber, '/api/user/number/<customernumber>')
api.add_resource(MAFUserExist, '/api/user/exist/<customernumber>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

