from multiprocessing import Pool
from flask import Flask
from pymongo import MongoClient
from flask import request
from YoutubeAPI import fetchRequest, intialdum, loop, start

from database import fetchDataFromDb , searchData
app = Flask(__name__)
 
@app.route("/searchQuery", methods=['GET']) #type: ignore
def searchQuery():
    args = request.args
    query = args.get('query')
    count = args.get('count')
    if(query == None):
        return "Invalid Query" , 400

    if(count == None or int(count , 0) <= 0):
        return "Invalid Count" , 400
    count = int(count)

    try:
        result = fetchDataFromDb(count , query)
    except Exception as e:
        return ("Internal Server Error \n ",e) , 500
    
    if(result.__len__() == 0):
        return "No Data Found" , 404
        
    return {'result':result , 'count':result.__len__()} , 200

@app.route("/search", methods=['GET']) #type: ignore
def search():
    args = request.args
    title = args.get('title')
    count = args.get('count')
    if(title == None):
        return "Invalid Query" , 400

    if(count == None or int(count , 0) <= 0):
        return "Invalid Count" , 400
    count = int(count)

    try:
        result = searchData(count , title)
    except Exception as e:
        return ("Internal Server Error \n ",e) , 500
    
    if(result.__len__() == 0):
        return "No Data Found" , 404
        
    return {'result':result , 'count':result.__len__()} , 200

@app.route("/", methods=['GET']) #type: ignore
def get():
    args = request.args
    count = args.get('count')

    if(count == None or int(count , 0) <= 10):
        count =10
    count = int(count)

    try:
        result = fetchDataFromDb(count , "")
    except Exception as e:
        return ("Internal Server Error \n ",e) , 500
    
    if(result.__len__() == 0):
        return "No Data Found" , 404
        
    return {'result':result , 'count':result.__len__()} , 200



@app.route("/setQuery", methods=['POST'])
def startLoop():
    args = request.args
    query = args.get('query')
    if(query == None):
        return "Invalid Query \n Query Required" , 400
    intialdum(query)
    return "Request Accepted" , 202

@app.before_first_request
def before_first_request_func():
    print("App is Running")
    loop()
if __name__ == "__main__":
    loop()
    app.run()