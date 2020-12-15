1 SOL_INFO = VALUES OF SOL
AT = Atmospheric Temperature
PRE = Atmospheric Pressure
HWS = Horizontal Wind Speed
WD = Wind Direction
SEASON = [“winter”, “spring”, “summer”, “fall”]
FIRST / LAST UTC = format of YYYY-MM-DDTHH:MM:SSZ



2(i) VALUES OF SOL_INFO(AT, HWS, PRE) - AT , CT , MN , MX
For AV :-
	av is Fahrenheit in the case of AT
	av is m/s in the case of HWS
	av is Pa in the case of PRE
For CT :-
	For all(AT , HWS & PRE) - total number of recorded samples over the Sol
For MN :-
	For all(AT , HWS & PRE) - minimum data sample recorded over the Sol
For MX :-
	For all(AT , HWS & PRE) - maximum data sample recorded over the Sol

2(ii) VALUES OF SOL_INFO(WD) - compass_pt_no , most_common
For compass_pt_no :-
	Falls in the range ['1','2','3','4',...,'16']
For most_common and compass_pt_no :-
	compass_degrees - Number; the compass direction of the center of the compass point; degrees
	compass_point - String; the name of the compass point e.g. “N” for North, or “ESE” for East-SouthEast
	compass_right - Number; the positive-right (positive-east), horizontal component of a unit vector indicating the direction of the compass point
	compass_up - Number; the positive--up (positive-north), vertical component of a unit vector indicating the direction of the compass point
	ct - Number; the number of samples for the Sol in the <compass_degrees> around this compass point



BUT NOT DONE :-
	DEFAULT UNITS :-

	1) Air Temperature - Fahrenheit (Add Celsius)
	2) HWS - m/s (Add m/hr)
	3) Air Pressure - Pa (Add atm)