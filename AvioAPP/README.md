Here are displayed all possibile options
To execute a complete mission cicle from a file use:
	 ./motor --cicle
	 ./motor --cicle --loop [value] , value means number of loop, if not specified it's set to 1
		 ./motor --cicle --loop 2
If you want to run motor in manual mode use:
	 ./motor --ManualPosition [-option(s)] [value]
In the following section are displayed all possible option avaiable:
		  --homing : using this option motor starts a reset of position going to zero position
		  -p [value] : this set motor position, value must be expressed in percentage
		  -t [value] : this keep motor position for n seconds, value must be expressed in seconds
		  --end: this close the connection to epos4
	 some example:
		./motor --ManualPosition --homing 	 this sets only the homing position.
		./motor --ManualPosition --homing -p -80 -t 2 	 this sets homing position and goes to position for 2 seconds
		./motor --ManualPosition -p -80 -t 2 	 this goes to position for 2 seconds
		./motor --ManualPosition -p -80 -t 2 --end	 this goes to position for 2 seconds and close the EPOS4 connection
It's mandatory to run Manual Positioning Mode starts from homing position. 
It is possibile to set directly from command line execution parameters:

!!!It's mandatory to pass all parameters every time you call this method!!!
With option --HM_PAR you can modify HOMING POSITION PARAMETERS:
 you have to pass new parameter exactly in this order:

		--HM_PAR CURRENT_THRESHOLD ACCELERATION HOMING_POSITION HOMING_POSITION_OFFSET SPEED_TO_SWITCH SPEEDINDEX


for the meaning of this parameters refers to HOMING POSITION from this manual:
 www.maxongroup.it/medias/sys_master/root/8834319745054/EPOS-Command-Library-En.pdf
With option --PS_PAR you can modify PROFILE POSITION PARAMETERS:
 you have to pass new parameter exactly in this order:

		--PS_PAR PROFILE_VELOCITY PROFILE_ACCELERATION PROFILE_DECELERATION


for the meaning of this parameters refers to PROFILE POSITION from this manual:
 www.maxongroup.it/medias/sys_master/root/8834319745054/EPOS-Command-Library-En.pdf
To do this change for each HOMING POSITION and POSITION PROFILE use:

		 --HP_PAR CURRENT_THRESHOLD\ 
			 ACCELERATION\ 
			 HOMING_POSITION\ 
			 HOMING_POSITION_OFFSET\ 
			 SPEED_TO_SWITCH\ 
			 SPEEDINDEX\ 
			 PROFILE_VELOCITY\ 
			PROFILE_ACCELERATION\ 
			 PROFILE_DECELERATION

