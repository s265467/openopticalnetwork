from gnpy.core.info import *
import json
import matplotlib.pyplot as plt
from math import *

with open("spectral_info.json","r") as read_file:
	data = json.load(read_file)
n=[]
for el in data["spectral_info"][0]:
	n.append( float(data["spectral_info"][0][el]) )

test = create_input_spectral_information(n[0],n[1],n[2],n[3],n[4],n[5])

x_,y_ = [],[]
for el in test[1]:
	x_.append(el[1]/(10**12))
	y_.append(10*log10(el[4][0])+30)
plt.ylabel("[dBm] (power of signals)")
plt.xlabel("[THz] channels frequency")
plt.plot(x_,y_,'o')
plt.show()
