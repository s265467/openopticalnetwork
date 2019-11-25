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

