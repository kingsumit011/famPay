# famPay
BackendTask
####
## Step To Run
Create a config.pyFile and add APi key and token in format 
    api_key = ["API key"]
    access_token = ["access token"]
Install the Mongo database or add your remote mongo database in the database.pyFile
Make Virtual Envirnment and install the requiment.txt file
run the command flask run 


####  
# Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# API Made
# EndPoints
1) /searchQuery[GET] : to Do Partial Search Based on Query Parameters : Params query and count

2)/search[GET] : to Do Partial Search Based on title and Description Parameters : Params title/desscription and count

3)/[GET] : Give the list of stored video data in a paginated response sorted in descending order of published datetime. Params count

4) /setQuery[POST] : to add Query for youtube API

# Also You can see the live API on this domain with the above endPoints

# Explanation
All Data of youtube vedios are stored in Mongo Db with the following format: 
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
Youtube API will be calling every 30 minutes in the background Thread

The Project Mainly consists of 3 File 
app.py : application
database.py : consistes of database related functions
YoutubeAPI.py : call All the API related to youtube


