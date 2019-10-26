import requests
import datetime
import json
import os
user = "<user>"
key = "<key>"
epoch = datetime.datetime.utcfromtimestamp(0)
today = datetime.datetime.today()
d = today - epoch
rank = requests.get("https://osu.ppy.sh/api/get_user?k="+key+"&u="+user).json()[0]["pp_rank"]
day = int(d.days)+float(today.hour/24)+float(today.minute/1440)
try:
    a = open("saverank.json","r+")
except:
    a = open("saverank.json","w+")
    a.write("{\"rank\": ["+str(int(rank))+"]}")
    a.close()
    a = open("saverank.json","r+")
try:
    b = open("saveday.json","r+")
except:
    b = open("saveday.json","w+")
    b.write("{\"day\": ["+str(day)+"]}")
    b.close()
    b = open("saveday.json","r+")
jsonloads = json.loads(str(a.read()))["rank"]
try:
    test = 1/(int(rank)-jsonloads[len(jsonloads)-1])
    jsonloads.append(int(rank))
    jsonloadsd = json.loads(str(b.read()))["day"]
    jsonloadsd.append(day)
    print(jsonloadsd, jsonloads)
except:
    pass
a.close()
b.close()
try:
    test = 1/(int(rank)-jsonloads[len(jsonloads)-1])
    os.remove("saverank.json")
    os.remove("saveday.json")
    a = open("saverank.json","w+")
    a.write("{\"rank\" : "+str(jsonloads)+"}")
    a.close()
    b = open("saveday.json","w+")
    b.write("{\"day\" : "+str(jsonloadsd)+"}")
    b.close()
except:
    pass
