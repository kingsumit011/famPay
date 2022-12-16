import asyncio
import requests
import database
import schedule
import time 
from threading import Thread

key = 'AIzaSyCiTiATyASdb37KBe5TrTzISg8bD329Hf4'
header =  {'Authorization': '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'}
i =0
defQuery = "Game"
countDump =0
dns = 'https://youtube.googleapis.com/youtube/v3/search?type=video&part=snippet&eventType=completed&'
# loop = asyncio.get_event_loop()

def fetch(query:str=defQuery , count:int = 50):
   
    if(count > 50 or query == None or query.__len__() == 0 or key == None or key.__len__() == 0 or header==None):
        raise  Exception("Invalid Arguments")

    url=dns +'maxResults='+str(count)+'&q='+query+'&key=' +key
    fetchRequest(url)


def intialdum(type:str , token:str =""):
    global countDump
    if(countDump >= 3) :
        countDump = 0
        loop()
        return
    count = 49
    url =dns+"key="+key+"&pageToken="+token+"&maxResults="+str(count)+"&q="+type
    token = fetchRequest(url)
    countDump = countDump + 1
    intialdum(type , token)

def fetchRequest(url:str , query:str=defQuery):
    global defQuery
    response = requests.get(url , headers=header)
    defQuery = query +"|" +defQuery

    if response.status_code != 200:
        print('Failed to get data:', response.status_code)
        raise Exception('Failed to get data:', response.status_code)
    else:
        print(response.json()['items'].__len__())
        database.store(response.json() , defQuery)
    return response.json()['nextPageToken']

def start():
    global i
    while True:
        time.sleep(30*60)
        print("Count : " , i)
        i = i+1
def loop():
    print("Loop Started")
    t = Thread(target=start)
    t.start()
