import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.maf
collection = db.customers

class Databasemongo():
        def insert(self,cn,fn,ln,ma,ads,adc,adz):
                """This function can insert data in MongoDB
                usage = insert(<customernumber>,<first_name>,<last_name>,<email>,<street>,<city>,<zipcode>,<province>)"""
                inscustomer={"_id" : str(cn),
                                "name" : {"first_name": str(fn), "last_name": str(ln)},
                                "email" : str(ma),
                                "address" : {
                                        "street" : str(ads),
                                        "city" : str(adc),
                                        "zipcode" : str(adz)
                                },
                                "trainingresults" : []
                        }
                try:
                        collection.insert(inscustomer)
                        print ("Registreren geslaagd")
                except:
                        print("Registreren mislukt")

        def select(self,cn):
                """This function can select data from MongoDB
                usage = select(<first_name>,<last_name)"""
                output = collection.find({"_id":str(cn)})
                for i in output:
                        return i

        def updatecus(self,cn,fn,ln,ma,ads,adc,adz):
                """This function can update data in MongoDB
                usage = update(<customernumber>,<firsname>,<lastname>,<email>,<street>,<city>,<zipcode>)"""
                try:
                        collection.update({"_id":str(cn)},{'$set': {"name": {"first_name": str(fn),"last_name": str(ln)}}})
                        collection.update({"_id":str(cn)},{'$set': {"email": str(ma)}})
                        collection.update({"_id":str(cn)},{'$set': {"address" : {"street" : str(ads),"city" : str(adc),"zipcode" : str(adz)}}})
                        print("Customer updatet")
                except:
                        print("Can't update customer")

        def updatetraining(self,cn,tr):
                """This function can update data in MongoDB
                usage = update(<customernumber>,<trainingresults>)"""
                try:
                        collection.update({"_id":str(cn)},{'$push': {"trainingresults": int(tr)}})
                        print("Update geslaagd")
                except:
                        print("Update mislukt")

        def delete(self,cn):
                """This function can delete data from MongoDB
                usage = delete(<customernumber>)"""
                try:
                        collection.delete_one({"_id": str(cn)})
                except:
                        print("Kan de data niet verwijderen")

        def countdoc(self,cn):
                """This function can check if customer exists in MongoDB
                usage = cexists(<customernumber>)"""
                test = collection.count_documents({ "$and": [{"_id": str(cn)},{ "_id": {"$not":{"$size": 0}} },{ "_id": {"$exists": "true" }}]})
                return test
