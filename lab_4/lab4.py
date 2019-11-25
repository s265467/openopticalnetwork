from gnpy.core.info import *
import json
import matplotlib.pyplot as plt
from math import *

#reading json file
with open("dati_esercizio.json","r") as read_file:
	data = json.load(read_file)

#obtaining data to compute spectral information
si = data["SI"][0]
#creating spectral information
obj = create_input_spectral_information(si["f_min"],si["f_max"],si["roll_off"],si["baud_rate"],10**((si["power_dbm"]-30)/10),si["spacing"])

#replacing value as requested
obj1 = obj._replace(carriers=tuple(c._replace(power = c.power._replace(signal= c.power.signal + 10**0.3, nli = 5*10**(-8), ase= 10**(-7)))
                              for c in obj.carriers))

#dati plot
p_,f_ = [],[]
ase_,nli_ = [],[]

#making list to plot
for ogg in obj1[1]:
	f_.append(ogg.frequency)
	p_.append(ogg.power.signal)
	ase_.append(ogg.power.ase)
	nli_.append(ogg.power.nli)


