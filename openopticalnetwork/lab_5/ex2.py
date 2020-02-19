from material.utilities import *
from gnpy.core.info import *
import json
import matplotlib.pyplot as plt
from math import *
from gnpy.core.elements import *


#Exercise 2

#loading fiber data from json file
with open("my_fiber.json","r") as rd_file:
	data = json.load(rd_file)

#loading data fiber
fiber = Fiber(**data["Fiber"])

#instantiating noiseless WDM
with open("material/eqp.json","r") as read_file:
	data = json.load(read_file)

#cleaning useless values
data["SI"][0].pop("power_range_db")
data["SI"][0].pop('tx_osnr')
data["SI"][0].pop('sys_margins')

p = 10**((data["SI"][0].pop("power_dbm")-30)/10) #dbm to db

WDM_in = create_input_spectral_information(**data["SI"][0],power=p)

#propagate WDM_in throught Fiber

WDM_out_fiber = fiber.__call__(WDM_in)

#instantiating EDFA
#Loading EDFA parameters (Optical Amplifier)
edfa_params = get_edfa_parameters("my_config.json","material/eqp.json")
edfa = Edfa(**edfa_params)

#propagate WDM throught EDFA
WDM_out_edfa = edfa.__call__(WDM_out_fiber)
