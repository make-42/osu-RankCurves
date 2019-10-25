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
curradd = [int(d.days),int(rank)]
print(curradd)
try:
    a = open("saverank.json","r+")
except:
    a = open("saverank.json","w+")
    a.write("{\"saves\": []}")
    a.close()
    a = open("saverank.json","r+")

jsonloads = json.loads(str(a.read()))["saves"]
jsonloads.append(curradd)
a.close()
os.remove("saverank.json")
a = open("saverank.json","w+")
a.write("{\"saves\" : "+str(jsonloads)+"}")
a.close()
