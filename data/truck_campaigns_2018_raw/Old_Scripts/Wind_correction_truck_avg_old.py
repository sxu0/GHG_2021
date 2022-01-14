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
meteo_shift_felix = timedelta(seconds=7)

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
meteo_shift_sebastien = timedelta(seconds=-14)
meteo_shift_felix = timedelta(seconds=-16)

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
meteo_shift_sebastien = timedelta(seconds=-16)
meteo_shift_felix = timedelta(seconds=-18)

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

gps_time_epoch = []

for ll in range(0,len(gps_time)):
    gps_time_epoch.append( (gps_time[ll] - datetime(1970,1,1)).total_seconds() )

print('gps', len(gps_time))

######################################
## MeteoData
############################################

path_meteo = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Weather_Station/' 					# chemin du dossier contenant le fichier a decouper
filename_meteo = path_meteo + fichier_meteo 	# chemin du fichier a traiter

fil=open(filename_meteo, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

meteo_time, meteo_time_epoch, wind_speed, wind_direction, temperature, Relative_Humidity, Pressure = [], [], [], [], [], [], []

#meteo_shift = timedelta(seconds=11)		# selected looking at the correlation between car_s and wind_speed
#meteo_shift = timedelta(seconds=29)


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

    #meteo_time.append(datetime(year,month,day,hour,minute,second)+meteo_shift)
    #meteo_time_epoch.append( (datetime(year,month,day,hour,minute,second) + meteo_shift - datetime(1970,1,1)).total_seconds() )
    meteo_time.append(datetime(year,month,day,hour,minute,second)+meteo_shift_sebastien)
    meteo_time_epoch.append( (datetime(year,month,day,hour,minute,second) + meteo_shift_sebastien - datetime(1970,1,1)).total_seconds() )
    wind_speed.append(float((','.join(donnees[ll].split())).split(',')[2]))				
    wind_direction.append(float((','.join(donnees[ll].split())).split(',')[3]))			
    temperature.append(float((','.join(donnees[ll].split())).split(',')[4]))
    Relative_Humidity.append(float((','.join(donnees[ll].split())).split(',')[5]))
    Pressure.append(float((','.join(donnees[ll].split())).split(',')[6]))

'''
######## minute average

meteo_time_m, wind_speed_m, wind_direction_m = [], [], []
ws, wd, vxs, vys = [], [], [], []


# initialisation m0
h0 = meteo_time[0].hour
m0 = meteo_time[0].minute

for ll in range(0,len(meteo_time)):
	if meteo_time[ll].hour == h0 and meteo_time[ll].minute == m0:
		ws.append(wind_speed[ll])
		vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
		vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))

	if meteo_time[ll].minute != m0:
		meteo_time_m.append(meteo_time[ll])
		wind_speed_m.append(np.mean(ws))
		# Wind conditions average
		# recombine into a theta, second line takes care of negative angles and angels greater than 360 and rotates into angel from North	
		thetas_avg = np.degrees(np.arctan2(np.average(vys), np.average(vxs)))
		wind_direction_m.append((450 - thetas_avg) % 360)
     	
		h0 = meteo_time[ll].hour
		m0 = meteo_time[ll].minute
		ws, vxs, vys = [], [], []		



plt.plot(meteo_time, wind_direction, 'bx', label='Raw data')
plt.plot(meteo_time_m, wind_direction_m, 'c+', label='Minute avg')
plt.ylabel('Direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.legend(loc=2)
plt.show()
'''




'''
gps_time_interp, wind_speed_interp, wind_direction_interp, temperature_interp, Relative_Humidity_interp, Pressure_interp = [], [], [], [], [], []

for ii in range(0,len(gps_time)):
	if gps_time[ii] >= meteo_time[0] and gps_time[ii] <= meteo_time[-1]:
		gps_time_interp.append(gps_time[ii])
		wind_speed_interp.append(np.interp(gps_time_epoch[ii],meteo_time_epoch,wind_speed))
		wind_direction_interp.append(np.interp(gps_time_epoch[ii],meteo_time_epoch,wind_direction))
		temperature_interp.append(np.interp(gps_time_epoch[ii],meteo_time_epoch,temperature))
		Relative_Humidity_interp.append(np.interp(gps_time_epoch[ii],meteo_time_epoch,Relative_Humidity))
		Pressure_interp.append(np.interp(gps_time_epoch[ii],meteo_time_epoch,Pressure))


print('interp', len(wind_speed_interp))
'''



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
	if math.degrees(math.atan2( X , Y )) >= 0:
		car_d.append(math.degrees(math.atan2( X , Y )) ) 	# /!\ car direction to 
	if math.degrees(math.atan2( X , Y )) < 0:
		car_d.append(math.degrees(math.atan2( X , Y )) + 360)

	#wind_speed_interp_plot.append(wind_speed_interp[ii])

print('car', len(car_d))



'''
# determiner meteoshift a l'aide du coef de corr entre car_s et wind_speed
slope, intercept, r_value, p_value, std_errb = stats.linregress(car_s,  wind_speed_interp_plot)
print('r:', r_value)		

plt.plot(car_s, wind_speed_interp_plot, 'b+')
plt.show()
'''


wind_speed_corr, wind_direction_corr, time_corr = [], [], []
wind_speed_corr_spdfilter, wind_direction_corr_spdfilter, time_corr_spdfilter = [], [], []
wind_speed_corr_stop, wind_direction_corr_stop, time_corr_stop = [], [], []
wind_speed_corr_braking, wind_direction_corr_braking, time_corr_braking = [], [], []
wind_speed_corr_both, wind_direction_corr_both, time_corr_both = [], [], []

for ii in range(0,len(meteo_time)):
	for ll in range(0,len(car_time)):
		if meteo_time[ii].day == car_time[ll].day and meteo_time[ii].hour == car_time[ll].hour and meteo_time[ii].minute == car_time[ll].minute and meteo_time[ii].second == car_time[ll].second:
		    			
			U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
			V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

			U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
			V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

			time_corr.append(car_time[ll])
			wind_speed_corr.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
			direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
			if direction >= 0:
				wind_direction_corr.append( direction )
			if direction < 0:
				wind_direction_corr.append( direction + 360 )



			if wind_speed[ii] > car_s[ll] :			# filter data when car speed higher than wind speed
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_spdfilter.append(car_time[ll])
				wind_speed_corr_spdfilter.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
				if direction >= 0:
					wind_direction_corr_spdfilter.append( direction )
				if direction < 0:
					wind_direction_corr_spdfilter.append( direction + 360 )
	

			if car_s[ll] == 0:				# filter data when car stop
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_stop.append(car_time[ll])
				wind_speed_corr_stop.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
				if direction >= 0:
					wind_direction_corr_stop.append( direction )
				if direction < 0:
					wind_direction_corr_stop.append( direction + 360 )



	for ll in range(0,len(car_time)-1):
		if meteo_time[ii].day == car_time[ll].day and meteo_time[ii].hour == car_time[ll].hour and meteo_time[ii].minute == car_time[ll].minute and meteo_time[ii].second == car_time[ll].second:
			if abs(car_s[ll]-car_s[ll+1]) < 0.5: 			# filter when big acceleration and braking
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_braking.append(car_time[ll])
				wind_speed_corr_braking.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
				if direction >= 0:
					wind_direction_corr_braking.append( direction )
				if direction < 0:
					wind_direction_corr_braking.append( direction + 360 )					


	for ll in range(0,len(car_time)-1):
		if meteo_time[ii].day == car_time[ll].day and meteo_time[ii].hour == car_time[ll].hour and meteo_time[ii].minute == car_time[ll].minute and meteo_time[ii].second == car_time[ll].second:
			if (abs(car_s[ll]-car_s[ll+1]) < 0.5) and (wind_speed[ii] > car_s[ll]) : 			# filter when big acceleration and braking and car speed higher than wind speed
				U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
				V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

				U_c = ( - car_s[ll] * math.sin( math.radians(car_d[ll]) ) )
				V_c = ( - car_s[ll] * math.cos( math.radians(car_d[ll]) ) )

				time_corr_both.append(car_time[ll])
				wind_speed_corr_both.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))
				direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
				if direction >= 0:
					wind_direction_corr_both.append( direction )
				if direction < 0:
					wind_direction_corr_both.append( direction + 360 )



######## minute average

meteo_time_m, wind_speed_m, wind_direction_m = [], [], []
ws, wd, vxs, vys = [], [], [], []


# initialisation m0
h0 = time_corr_both[0].hour
m0 = time_corr_both[0].minute


for ll in range(0,len(time_corr_both)):
	if time_corr_both[ll].hour == h0 and time_corr_both[ll].minute == m0:
		ws.append(wind_speed_corr_both[ll])
		vxs.append(wind_speed_corr_both[ll] * np.sin(np.radians(wind_direction_corr_both[ll])))	
		vys.append(wind_speed_corr_both[ll] * np.cos(np.radians(wind_direction_corr_both[ll])))

	if time_corr_both[ll].minute != m0 and len(ws) != 0:
		meteo_time_m.append(time_corr_both[ll])
		wind_speed_m.append(np.mean(ws))
		# Wind conditions average
		# recombine into a theta, second line takes care of negative angles and angels greater than 360 and rotates into angel from North	
		thetas_avg = np.degrees(np.arctan2(np.average(vys), np.average(vxs)))
		wind_direction_m.append((450 - thetas_avg) % 360)

     	if time_corr_both[ll].minute != m0:
		h0 = time_corr_both[ll].hour
		m0 = time_corr_both[ll].minute
		ws, vxs, vys = [], [], []		


#time, data = df["gps_time"], df["ch4d"]
#data.rolling(window=filter_len,center=True).quantile(threshold)					




path_results = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Wind_correction/'

try:
	os.makedirs(path_results)
except OSError:
	pass
os.chdir(path_results)

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



#plot braking and car speed filter minute avg
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(meteo_time_m, wind_speed_m, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend(loc=2)
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.savefig("Speed_corr_both-avg_" + jour_mesure + ".png")
plt.close('all')

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(meteo_time_m, wind_direction_m, 'b+', label='Corrected wind')
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
ax.bar(wind_direction_m, wind_speed_m, normed=True, opening=0.8, edgecolor='white')
set_legend(ax)
plt.savefig("windrose_corr_both-avg_" + jour_mesure + ".png")
plt.close("all") 




'''
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
	for jj in range(n,len(meteo_time)):
		if meteo_time[jj].day == gps_time[ii].day and meteo_time[jj].hour == gps_time[ii].hour and meteo_time[jj].minute == gps_time[ii].minute and meteo_time[jj].second == gps_time[ii].second:
			print gps_time[ii].strftime("%Y-%m-%d %H:%M:%S.%f")
			nom_sebastien_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (gps_time[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt[ii],'Nan',ch4[ii],ch4d[ii],'Nan',co2[ii],co2d[ii],'Nan','Nan','Nan',h2o[ii],'Nan','Nan',lat[ii],lon[ii],Pressure[jj],'Nan','Nan','Nan','Nan',temperature[jj],'Nan','Nan','Nan','Nan'))
			n = jj
			break

nom_sebastien_interp.close()
'''


########################## 
# Felix GPS data
###########################




