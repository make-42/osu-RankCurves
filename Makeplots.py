import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
a = open("saverank.json","r+")
ab = json.loads(str(a.read()))["rank"]
b = open("saveday.json","r+")
bc = json.loads(str(b.read()))["day"]
print(ab,bc)
matplotlib.pyplot.style.use("dark_background")
matplotlib.pyplot.plot(bc,ab,label='osu!rank')
matplotlib.pyplot.style.use("dark_background")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
