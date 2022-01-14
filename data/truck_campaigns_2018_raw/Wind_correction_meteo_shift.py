# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:38:05 2018

@author: Sébastien
"""


import sys	# for windrose
reload(sys)  
sys.setdefaultencoding('Cp1252')

import os
import datetime as dt
from datetime import datetime
from datetime import timedelta
import pylab as pl
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates as md
from matplotlib.ticker import MaxNLocator
from scipy import stats
import math
from math import *
import pandas as pd
from windrose import WindroseAxes


# Convert the gps_time strings into real date&times
def convert_to_time(x):
    return datetime.strptime(x,"%Y-%m-%d %H:%M:%S.%f")


######################################
## Files
############################################

'''
# 2018-08-15
jour_mesure = '2018-08-15'
fichier_meteo='Meteodata_Campaign20180815'
fichier_felix_interp = 'sync_data_2018-08-15_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-15_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=15)
meteo_shift_felix = timedelta(seconds=11)

HEURE = [datetime(2018,8,16,i,00,00,00) for i in range(2,9)]
WIND_DIRECTION = [270, 280, 240, 260, 280, 270, 310]
WIND_SPEED = [9, 11, 11, 9, 9, 9, 6]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-08-16
jour_mesure = '2018-08-16'
fichier_meteo='Meteodata_Campaign20180817'
fichier_felix_interp = 'sync_data_2018-08-16_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-16_sebastien_interp.csv'
#meteo_shift_sebastien = timedelta(seconds=)
meteo_shift_felix = timedelta(seconds=13)

HEURE = [datetime(2018,8,17, i, 00, 00, 00) for i in range(7,11)]
WIND_DIRECTION = [180, 140, 160, 170]
WIND_SPEED = [9, 9, 9, 7]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-08-27
jour_mesure = '2018-08-27'
fichier_meteo='Meteodata_Campaign20180827'
fichier_felix_interp = 'sync_data_2018-08-27_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-27_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=14)
meteo_shift_felix = timedelta(seconds=11)

HEURE = [datetime(2018,8,28,i,00,00,00) for i in range(3,11)]
WIND_DIRECTION = [240, 230, 190, 220, 220, 220, 220, 230]
WIND_SPEED = [13, 13, 7, 13, 17, 20, 19, 19]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-08-30
jour_mesure = '2018-08-30'
fichier_meteo='Meteodata_Campaign20180830'
fichier_felix_interp = 'sync_data_2018-08-30_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-30_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=9)
meteo_shift_felix = timedelta(seconds=6)

HEURE = [datetime(2018,8,30, i, 00, 00, 00) for i in range(15,24)]
WIND_DIRECTION = [350, 10, 10, 20, 350, 340, 150, 160, 130]
WIND_SPEED = [19, 17, 13, 11, 11, 6, 9, 9, 7]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-09-26
jour_mesure = '2018-09-26'
fichier_meteo='Meteodata_Campaign20180927'
fichier_felix_interp = 'sync_data_2018-09-26_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-09-26_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=-8)
meteo_shift_felix = timedelta(seconds=-10)

HEURE = [datetime(2018,9,27, i, 00, 00, 00) for i in range(2,11)]
WIND_DIRECTION = [350, 0, 250, 240, 240, 240, 240, 290, 0, 40]  # /!\ 0 means no wind
WIND_SPEED = [13, 0, 6, 7, 9, 9, 7, 6, 0, 6]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-10-03
jour_mesure = '2018-10-03'
fichier_meteo='Meteodata_Campaign20181003'
fichier_felix_interp = 'sync_data_2018-10-03_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-10-03_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=-15)
meteo_shift_felix = timedelta(seconds=-17)

HEURE = [datetime(2018,10,03, i, 00, 00, 00) for i in range(19,24)]
HEURE = HEURE + [datetime(2018,10,04, i, 00, 00, 00) for i in range(0,4)]
WIND_DIRECTION = [180, 160, 170, 150, 130, 130, 120, 120, 130]
WIND_SPEED = [7, 17, 11, 13, 13, 11, 9, 9, 9]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-10-05
jour_mesure = '2018-10-05'
fichier_meteo='Meteodata_Campaign20181005'
fichier_felix_interp = 'sync_data_2018-10-05_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-10-05_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=-17)
meteo_shift_felix = timedelta(seconds=-19)

HEURE = [datetime(2018,10,06, i, 00, 00, 00) for i in range(2,14)]
WIND_DIRECTION = [110, 110, 100, 100, 100, 10, 50, 30, 40, 20, 40, 100]
WIND_SPEED = [19, 17, 11, 9, 7, 15, 11, 9, 11, 9, 9, 9]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''

# 2018-10-12
jour_mesure = '2018-10-12'
fichier_meteo='Meteodata_Campaign20181012'
fichier_felix_interp = 'sync_data_2018-10-12_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-10-12_sebastien_interp.csv'
meteo_shift_sebastien = timedelta(seconds=-22)
meteo_shift_felix = timedelta(seconds=-24)

HEURE = [datetime(2018,10,13, i, 00, 00, 00) for i in range(3,13)]
WIND_DIRECTION = [250, 250, 260, 300, 280, 280, 230, 250, 260, 250]
WIND_SPEED = [17, 19, 19, 19, 11, 11, 11, 17, 15, 13]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]





######################################
## Garmin GPS data
############################################
				
path_datasync = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/'

df = pd.read_csv(path_datasync + fichier_sebastien_interp)
#df = pd.read_csv(path_datasync + fichier_felix_interp)
df["gps_time"] = df["gps_time"].apply(convert_to_time)
gps_time, alt, ch4, ch4d, co2, co2d, h2o, lat, lon = df["gps_time"], df["alt"], df["ch4"], df["ch4d"], df["co2"], df["co2d"], df["h2o"], df["lat"], df["lon"]

print('gps', len(gps_time))

###########################################
# car 
###########################################

R = 6371000	# meters

car_s, car_d, car_time = [], [], []
wind_speed_interp_plot = []

for ii in range(1,len(lat)):
	car_time.append(gps_time[ii])

	distance = R * math.radians( math.sqrt(math.pow(math.cos(math.radians(lat[ii-1])) * (lon[ii-1] - lon[ii]) , 2) + math.pow(lat[ii-1] - lat[ii], 2)) )
	temps = gps_time[ii]-gps_time[ii-1]
	car_s.append( distance / temps.total_seconds() )

	X = math.cos(math.radians(lat[ii])) * math.sin(math.radians(lon[ii]-lon[ii-1]))
	Y = math.cos(math.radians(lat[ii-1])) * math.sin(math.radians(lat[ii])) - math.sin(math.radians(lat[ii-1])) * math.cos(math.radians(lat[ii])) * math.cos(math.radians(lon[ii] - lon[ii-1]))
	car_d.append( (math.degrees(math.atan2( X , Y )) )%360) 	# /!\ car direction to 


	#wind_speed_interp_plot.append(wind_speed_interp[ii])

print('car', len(car_d))

######################################
## MeteoData
############################################

path_meteo = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Weather_Station/' 					# chemin du dossier contenant le fichier a decouper
filename_meteo = path_meteo + fichier_meteo 	# chemin du fichier a traiter

fil=open(filename_meteo, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier


shift, r_val = [], []

#for jj in range(-30,30):
for jj in range(-25,30):
	print jj
	meteo_shift = timedelta(seconds=jj)		# selected looking at the correlation between car_s and wind_speed

	meteo_time, wind_speed, wind_direction = [], [], []

	for ll in range(1, nbl):

		d = (','.join(donnees[ll].split())).split(',')[0]
		year = int(('/'.join(donnees[ll].split())).split('/')[0])
		month = int(('/'.join(donnees[ll].split())).split('/')[1])
		day = int(('/'.join(donnees[ll].split())).split('/')[2])
			   
		d = (','.join(donnees[ll].split())).split(',')[1]
		hour = int((':'.join(d.split())).split(':')[0])
		minute = int((':'.join(d.split())).split(':')[1])
		sec = float((':'.join(d.split())).split(':')[2])
		second = int(sec)
	
		meteo_time.append(datetime(year,month,day,hour,minute,second)+meteo_shift)
		wind_speed.append(float((','.join(donnees[ll].split())).split(',')[2]))				
		wind_direction.append(float((','.join(donnees[ll].split())).split(',')[3]))			

	car_speed, wind_sp = [], []
	start = 0
	for ii in range(0,len(car_time)):
		for ll in range(0,len(meteo_time)):
			if meteo_time[ll].day == car_time[ii].day and meteo_time[ll].hour == car_time[ii].hour and meteo_time[ll].minute == car_time[ii].minute and meteo_time[ll].second == car_time[ii].second:
				wind_sp.append(wind_speed[ll])
				car_speed.append(car_s[ii])
				start = ll
				break

	# determiner meteoshift a l'aide du coef de corr entre car_s et wind_speed
	slope, intercept, r_value, p_value, std_errb = stats.linregress(car_speed,wind_sp)
	r_val.append(r_value)
	shift.append(jj)
	print('r:', r_value)		

maxposition = r_val.index(max(r_val)) 
print(shift[maxposition])

plt.plot(shift,r_val, 'b+')
plt.show()








########################## 
# Felix GPS data
###########################




