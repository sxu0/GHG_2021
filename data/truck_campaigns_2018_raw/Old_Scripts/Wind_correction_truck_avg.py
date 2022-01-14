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

def convert_to_time_meteo(x):
    return datetime.strptime(x,"%Y/%m/%d %H:%M:%S")

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

HEURE = [datetime(2018,9,27, i, 00, 00, 00) for i in range(2,12)]
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
'''




######################################
## Garmin GPS data
############################################
				
path_datasync = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/'

#df_gps = pd.read_csv(path_datasync + fichier_sebastien_interp)
df_gps = pd.read_csv(path_datasync + fichier_felix_interp)
df_gps["gps_time"] = df_gps["gps_time"].apply(convert_to_time)
gps_time = df_gps["gps_time"]

df_gps.set_index('gps_time',inplace=True)
#gps_time, alt, ch4, ch4d, co2, co2d, h2o, lat, lon = df_gps["gps_time"], df_gps["alt"], df_gps["ch4"], df_gps["ch4d"], df_gps["co2"], df_gps["co2d"], df_gps["h2o"], df_gps["lat"], df_gps["lon"]
alt, ch4, ch4d, co2, co2d, h2o, lat, lon = df_gps["alt"], df_gps["ch4"], df_gps["ch4d"], df_gps["co2"], df_gps["co2d"], df_gps["h2o"], df_gps["lat"], df_gps["lon"]

gps_time_epoch = []

for ll in range(0,len(gps_time)):
    gps_time_epoch.append( (gps_time[ll] - datetime(1970,1,1)).total_seconds() )

print('gps', len(gps_time))


######################################
## MeteoData
############################################

path_meteo = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Weather_Station/' 					# chemin du dossier contenant le fichier a decouper
filename_meteo = path_meteo + fichier_meteo 	# chemin du fichier a traiter

df_meteo = pd.read_csv(filename_meteo)
df_meteo["Time"] = df_meteo["Time"].apply(convert_to_time_meteo)
#meteo_time = df_meteo["Time"] + meteo_shift_sebastien
meteo_time = df_meteo["Time"] + meteo_shift_felix

df_meteo.set_index('Time',inplace=True)

#meteo_time, wind_speed, wind_direction, temperature, Relative_Humidity, pressure = df["Time"], df["WS(m/s)"], df["WD(Deg)"], df["AT(C)"], df["RH(%)"], df["BP(mbar)"]
wind_speed, wind_direction, temperature, Relative_Humidity, pressure = df_meteo["WS(m/s)"], df_meteo["WD(Deg)"], df_meteo["AT(C)"], df_meteo["RH(%)"], df_meteo["BP(mbar)"]

meteo_time_epoch = []

for ll in range(0,len(meteo_time)):
    meteo_time_epoch.append( (meteo_time[ll] - datetime(1970,1,1)).total_seconds() )

print('meteo', len(meteo_time))

path_results = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Wind_correction/'

try:
	os.makedirs(path_results)
except OSError:
	pass



###########################################
# wind correction
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

	car_d.append( (math.degrees(math.atan2( X , Y )) ) %360) 	# direction to

print('car', len(car_d))

df_car = pd.DataFrame({'car_s': car_s,'car_d': car_d},index = car_time)


wind_speed_corr, wind_direction_corr, time_corr = [], [], []
wind_speed_corr_spdfilter, wind_direction_corr_spdfilter, time_corr_spdfilter = [], [], []
wind_speed_corr_stop, wind_direction_corr_stop, time_corr_stop = [], [], []
wind_speed_corr_braking, wind_direction_corr_braking, time_corr_braking = [], [], []
wind_speed_corr_both, wind_direction_corr_both, time_corr_both = [], [], []
vxs, vys = [], []

'''
for ii in range(0,len(meteo_time)):
	for ll in range(0,len(car_time)):
		if meteo_time[ii].day == car_time[ll].day and meteo_time[ii].hour == car_time[ll].hour and meteo_time[ii].minute == car_time[ll].minute and meteo_time[ii].second == car_time[ll].second:
		    			
			U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
			V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

			U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
			V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

			time_corr.append(car_time[ll])
			wind_speed_corr.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
			wind_direction_corr.append(( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360)


			if wind_speed[ii] > car_s[ll] :			# filter data when car speed higher than wind speed
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_spdfilter.append(car_time[ll])
				wind_speed_corr_spdfilter.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				wind_direction_corr_spdfilter.append(( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360)
	

			if car_s[ll] == 0:				# filter data when car stop
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_stop.append(car_time[ll])
				wind_speed_corr_stop.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				wind_direction_corr_stop.append(( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360)
	
	for ll in range(0,len(car_time)-1):
		if meteo_time[ii].day == car_time[ll].day and meteo_time[ii].hour == car_time[ll].hour and meteo_time[ii].minute == car_time[ll].minute and meteo_time[ii].second == car_time[ll].second:
			if abs(car_s[ll]-car_s[ll+1]) < 0.5: 			# filter when big acceleration and braking
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_braking.append(car_time[ll])
				wind_speed_corr_braking.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				wind_direction_corr_braking.append(( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360)				
'''

wind_speed_uncorr, wind_direction_uncorr, pressure_file, temperature_file = [], [], [], []

start = 0
	
for ll in range(0,len(car_time)-1):
	print car_time[ll]
	for ii in range(start,len(meteo_time)):
		if meteo_time[ii].day == car_time[ll].day and meteo_time[ii].hour == car_time[ll].hour and meteo_time[ii].minute == car_time[ll].minute and meteo_time[ii].second == car_time[ll].second:
			if (abs(car_s[ll]-car_s[ll+1]) < 0.5):# and (wind_speed[ii] > car_s[ll]) : 			# filter when big acceleration and braking and car speed higher than wind speed
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_both.append(car_time[ll])
				wind_speed_corr_both.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				#wind_direction_corr_both.append(( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360)

				vxs.append( math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ) * np.sin(np.radians( ( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360 )))	
				vys.append( math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ) * np.cos(np.radians( ( math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ) ) %360 )))

				pressure_file.append(pressure[ii])
				temperature_file.append(temperature[ii])
				wind_speed_uncorr.append(wind_speed[ii])
				wind_direction_uncorr.append(wind_direction[ii])

			start = ii
			break

#df_car_corr = pd.DataFrame({'ws_corr': wind_speed_corr_both,'wd_corr': wind_direction_corr_both},index = time_corr_both)
df_car_corr = pd.DataFrame({'ws_corr': wind_speed_corr_both,'vxs': vxs,'vys': vys},index = time_corr_both)
wind_speed_corr_both = df_car_corr['ws_corr']
#wind_direction_corr_both = df_car_corr['wd_corr']
vxs = df_car_corr['vxs']
vys = df_car_corr['vys']

wind_speed_avg = wind_speed_corr_both.rolling(window='300s').mean()
#wind_direction_avg = wind_direction_corr_both.rolling(window='300s').mean()
vxs_avg = vxs.rolling(window='300s').mean()
vys_avg = vys.rolling(window='300s').mean()

wind_direction_avg = []

for ii in range(0, len(vxs_avg)):
	thetas_avg = np.degrees(np.arctan2(np.average(vys_avg[ii]), np.average(vxs_avg[ii])))
	wind_direction_avg.append((450 - thetas_avg) % 360)


path_results = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Wind_correction/'

try:
	os.makedirs(path_results)
except OSError:
	pass
os.chdir(path_results)





'''
plt.plot(meteo_time, wind_speed, 'cx', label='Measured speed')
plt.plot(car_time, car_s, 'g+', label='Car speed')
#plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.legend(loc=2)
plt.savefig("Speed_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured Direction')
plt.plot(car_time, car_d, 'g+', label='Car Direction')
#plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.legend(loc=2)
plt.savefig("Direction_" + jour_mesure + ".png")
plt.close('all')


#plot time series
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr, wind_speed_corr, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr, wind_direction_corr, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Direction_corr_" + jour_mesure + ".png")
plt.close('all')
'''

##################
## wind roses 
##################
       
def new_axes():
    fig = plt.figure(figsize=(8, 8), dpi=80, facecolor='w', edgecolor='w')
    rect = [0.1, 0.1, 0.8, 0.8]
    ax = WindroseAxes(fig, rect, axisbg='w')
    fig.add_axes(ax)
    return ax

def set_legend(ax):
    l = ax.legend(borderaxespad=-0.10)
    plt.setp(l.get_texts(), fontsize=8)
'''
##windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wind_direction_corr, wind_speed_corr, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_" + jour_mesure + ".png")
plt.close("all") 





#plot speed filter
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr_spdfilter, wind_speed_corr_spdfilter, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_spdfilter_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr_spdfilter, wind_direction_corr_spdfilter, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Direction_corr_spdfilter_" + jour_mesure + ".png")
plt.close('all')

##windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wind_direction_corr_spdfilter, wind_speed_corr_spdfilter, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_spdfilter_" + jour_mesure + ".png")
plt.close("all") 


#plot stop filter
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr_stop, wind_speed_corr_stop, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_stop_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr_stop, wind_direction_corr_stop, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Direction_corr_stop_" + jour_mesure + ".png")
plt.close('all')

##windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wind_direction_corr_stop, wind_speed_corr_stop, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_stop_" + jour_mesure + ".png")
plt.close("all") 



#plot braking filter
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr_braking, wind_speed_corr_braking, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_braking_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr_braking, wind_direction_corr_braking, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Direction_corr_braking_" + jour_mesure + ".png")
plt.close('all')

##windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wind_direction_corr_braking, wind_speed_corr_braking, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_braking_" + jour_mesure + ".png")
plt.close("all") 



#plot braking and car speed filter
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr_both, wind_speed_corr_both, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_both_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr_both, wind_direction_corr_both, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Direction_corr_both_" + jour_mesure + ".png")
plt.close('all')

##windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wind_direction_corr_both, wind_speed_corr_both, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_both_" + jour_mesure + ".png")
plt.close("all") 
'''


#plot braking and car speed filter minute avg
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr_both, wind_speed_avg, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_both-avg_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr_both, wind_direction_avg, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Direction_corr_both-avg_" + jour_mesure + ".png")
plt.close('all')


##windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wind_direction_avg, wind_speed_avg, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_both-avg_" + jour_mesure + ".png")
plt.close("all") 









### plot hourly averaging

vxs_meas, vys_meas = [], []

for ii in range(0,len(wind_speed)):
	vxs_meas.append( wind_speed[ii] * np.sin(np.radians( wind_direction[ii] )))	
	vys_meas.append( wind_speed[ii] * np.cos(np.radians( wind_direction[ii] )))

df_wind_meas = pd.DataFrame({'vxs_meas': vxs_meas,'vys_meas': vys_meas},index = meteo_time)
df_p = df_wind_meas.resample('H').mean()
time_wind_avg, vxs_meas_avg, vys_meas_avg = df_p.index, df_p['vxs_meas'], df_p['vys_meas']

wd_meas_avg = []

for ii in range(0, len(vxs_meas_avg)):
	thetas_avg = np.degrees(np.arctan2(np.average(vys_meas_avg[ii]), np.average(vxs_meas_avg[ii])))
	wd_meas_avg.append((450 - thetas_avg) % 360)


df_p = df_meteo.resample('H').mean()
time_meas_avg, ws_meas_avg = df_p.index, df_p['WS(m/s)']

df_p = df_car_corr.resample('H').mean()
time_corr_avg, ws_corr_avg, vxs_avg, vys_avg = df_p.index, df_p['ws_corr'], df_p['vxs'], df_p['vys']

wd_avg = []

for ii in range(0, len(vxs_avg)):
	thetas_avg = np.degrees(np.arctan2(np.average(vys_avg[ii]), np.average(vxs_avg[ii])))
	wd_avg.append((450 - thetas_avg) % 360)


plt.plot(time_meas_avg, ws_meas_avg, 'co', label='Measured wind')
plt.plot(time_corr_avg, ws_corr_avg, 'bo', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.title('%s' % jour_mesure, loc='center')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("AVG_Speed_corr_" + jour_mesure + ".png")
plt.close('all')

plt.plot(time_wind_avg, wd_meas_avg, 'co', label='Measured wind')
plt.plot(time_corr_avg, wd_avg, 'bo', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.title('%s' % jour_mesure, loc='center')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("AVG_Direction_corr_" + jour_mesure + ".png")
plt.close('all')





"""
##### Creates file with wind data

path_results = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Wind_correction/'

try:
	os.makedirs(path_results)
except OSError:
	pass
os.chdir(path_results)

if os.path.exists(fichier_sebastien_interp):		# if file exists delete 
  os.remove(fichier_sebastien_interp)


nom_sebastien_interp = open(fichier_sebastien_interp, "w")

nom_sebastien_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')
n=0

for ii in range(0,len(gps_time)):
	for jj in range(n,len(time_corr_both)):
		if time_corr_both[jj].day == gps_time[ii].day and time_corr_both[jj].hour == gps_time[ii].hour and time_corr_both[jj].minute == gps_time[ii].minute and time_corr_both[jj].second == gps_time[ii].second:
			print gps_time[ii].strftime("%Y-%m-%d %H:%M:%S.%f")
			nom_sebastien_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (gps_time[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt[ii],'Nan',ch4[ii],ch4d[ii],'Nan',co2[ii],co2d[ii],'Nan','Nan','Nan',h2o[ii],'Nan','Nan',lat[ii],lon[ii],pressure_file[jj],'Nan','Nan','Nan','Nan',temperature_file[jj],wind_direction_avg[jj],wind_direction_uncorr[jj],wind_speed_avg[jj],wind_speed_uncorr[jj]))
			n = jj
			break

nom_sebastien_interp.close()
"""

########################## 
# Felix GPS data
###########################




