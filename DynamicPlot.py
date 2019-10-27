import json
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time
#a = open("saverank.json","r+")
#ab = json.loads(str(a.read()))["rank"]
#b = open("saveday.json","r+")
#bc = json.loads(str(b.read()))["day"]
#print(ab,bc)
#plt.style.use("dark_background")
#hl = plt.plot(bc,ab,label='osu!rank')
plt.style.use("dark_background")
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
def update(i):
    a = open("saverank.json","r+")
    ab = json.loads(str(a.read()))["rank"]
    b = open("saveday.json","r+")
    bc = json.loads(str(b.read()))["day"]
    print(ab,bc)
    ax.clear()
    ax.plot(bc,ab)
a = anim.FuncAnimation(fig, update, interval=10000, frames=999999999999999999999, repeat=False)
plt.show()
    
    
    
