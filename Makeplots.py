import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
a = open("saverank.json","r+")
ab = json.loads(str(a.read()))["rank"]
print(ab)
b = open("saveday.json","r+")
bc = json.loads(str(b.read()))["day"]
matplotlib.pyplot.plot(bc,ab)
matplotlib.pyplot.show()
