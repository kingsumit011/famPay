import pymongo
import time
client = pymongo.MongoClient('localhost', 27017)

def store(response ,query="Any"):
    result = []
    db = client['Youtube']
    collection = db['YoutubeData']

    for key in response['items']:
        snippet = key['snippet']
        obj={
            'etag' : key['etag'],
            '_id' : key['id']['videoId'],
            'publishedAt' :snippet['publishedAt'],
            'channelId' : snippet['channelId'],
            'title' : snippet['title'],
            'description' : snippet['description'],
            'thumbnails_default' : snippet['thumbnails']['default']['url'],
            'thumbnails_high' : snippet['thumbnails']['high']['url'],
            'channelTitle' : snippet['channelTitle'],
            'liveBroadcastContent' : snippet['liveBroadcastContent'],
            'publishTime':snippet['publishTime'],
            'query':query,
            'store_time':time.time(),
        }
        if(collection.find_one({'_id':key['id']['videoId']})==None):
            result.append(obj)
        else:
            collection.update_one({'_id':key['id']['videoId']},{'$set' :obj})
    if(result.__len__() > 0):
        collection.insert_many(result)


def fetchDataFromDb(count:int = 10 ,query="Game"):
    if(count < 10):
        count =10
    result = []
    db = client['Youtube']
    collection = db['YoutubeData']
    if(query == ""):
        temp = collection.find().sort('publishTime', -1).limit(count)
    else:
        temp = collection.find({'query':str("/"+query+"/")}).sort('publishTime', -1).limit(count)
    result = []
    for data in temp:
        result.append(data)
    return result
def searchData(count:int = 10 ,title=""):
    if(count < 10):
        count =10
    result = []
    db = client['Youtube']
    collection = db['YoutubeData']
    temp = collection.find( {'$or':[{'description' : str("/"+title+'/') },{ 'title':str("/"+title+'/')}]}).sort('publishTime', -1).limit(count)
    result = []
    for data in temp:
        result.append(data)
    return result