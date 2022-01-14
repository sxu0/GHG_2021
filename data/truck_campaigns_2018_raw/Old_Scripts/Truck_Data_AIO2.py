# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:38:05 2018

@author: Sébastien
"""


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


######################################
## Files
############################################

# campagne 1
path_calibration='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180814/' 				
fichier_calibration='CFADS59-20180814-1433-Data.dat'
beginning = '15:07:00'
ending = '15:47:00'

tanks = []
tanks = [['HIGH', 2.0916, 455.963],
	['LOW', 1.948, 402.858]]


'''
# 2018-08-15
jour_mesure = '2018-08-15'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180816/' 				
fichier_Picarro='CFADS59-20180816-0148-Data.dat'
fichier_meteo='Meteodata_Campaign20180815'
fichier_gps='20180815.csv'
fichier_garmin='Garmin_20180815.csv'
fichier_felix_interp = 'sync_data_2018-08-15_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-15_sebastien_interp.csv'

HEURE = [datetime(2018,8,16,i,00,00,00) for i in range(2,9)]
WIND_DIRECTION = [270, 280, 240, 260, 280, 270, 310]
WIND_SPEED = [9, 11, 11, 9, 9, 9, 6]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-08-16
jour_mesure = '2018-08-16'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180817/' 				
fichier_Picarro='CFADS59-20180817-0627-Data.dat'
fichier_meteo='Meteodata_Campaign20180817'
fichier_gps='20180817.csv'
fichier_garmin='Garmin_20180815.csv'
fichier_felix_interp = 'sync_data_2018-08-17_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-17_sebastien_interp.csv'

HEURE = [datetime(2018,8,17, i, 00, 00, 00) for i in range(7,11)]
WIND_DIRECTION = [180, 140, 160, 170]
WIND_SPEED = [9, 9, 9, 7]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-08-27
jour_mesure = '2018-08-27'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180828/' 				
fichier_Picarro='CFADS59-20180828-0317-Data.dat'
fichier_meteo='Meteodata_Campaign20180827'
fichier_gps='20180827.csv'
fichier_garmin='Garmin_20180827.csv'
fichier_felix_interp = 'sync_data_2018-08-27_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-27_sebastien_interp.csv'

HEURE = [datetime(2018,8,28,i,00,00,00) for i in range(3,11)]
WIND_DIRECTION = [240, 230, 190, 220, 220, 220, 220, 230]
WIND_SPEED = [13, 13, 7, 13, 17, 20, 19, 19]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-08-30
jour_mesure = '2018-08-30'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180830/' 				
fichier_Picarro='CFADS59-20180830-1436-Data.dat'
fichier_meteo='Meteodata_Campaign20180830'
fichier_gps='20180830.csv'
fichier_garmin='Garmin_20180830.csv'
fichier_felix_interp = 'sync_data_2018-08-30_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-30_sebastien_interp.csv'

HEURE = [datetime(2018,8,30, i, 00, 00, 00) for i in range(15,24)]
WIND_DIRECTION = [350, 10, 10, 20, 350, 340, 150, 160, 130]
WIND_SPEED = [19, 17, 13, 11, 11, 6, 9, 9, 7]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-09-26
jour_mesure = '2018-09-26'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180926/' 				
fichier_Picarro='CFADS59-20180926-Data.dat'
fichier_meteo='Meteodata_Campaign20180927'
fichier_gps='20180926.csv'
fichier_garmin='Garmin_20180926.csv'
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
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181003/' 				
fichier_Picarro='CFADS59-20181003-Data.dat'
fichier_meteo='Meteodata_Campaign20181003'
fichier_gps='20181003.csv'
fichier_garmin='Garmin_20181003.csv'
fichier_felix_interp = 'sync_data_2018-10-03_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-10-03_sebastien_interp.csv'

#HEURE = [datetime(2018,10,03, i, 00, 00, 00) for i in range(15,24)]
#WIND_DIRECTION = [350, 10, 10, 20, 350, 340, 150, 160, 130]
#WIND_SPEED = [19, 17, 13, 11, 11, 6, 9, 9, 7]
#WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-10-05
jour_mesure = '2018-10-05'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181006/' 				
fichier_Picarro='CFADS59-20181006-0156-Data.dat'
fichier_meteo='Meteodata_Campaign20181005'
fichier_gps='20181005.csv'
fichier_garmin='Garmin_20181005.csv'
fichier_felix_interp = 'sync_data_2018-10-05_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-10-05_sebastien_interp.csv'

HEURE = [datetime(2018,10,06, i, 00, 00, 00) for i in range(2,14)]
WIND_DIRECTION = [110, 110, 100, 100, 100, 10, 50, 30, 40, 20, 40, 100]
WIND_SPEED = [19, 17, 11, 9, 7, 15, 11, 9, 11, 9, 9, 9]
WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''

# 2018-10-12
jour_mesure = '2018-10-12'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181013/' 				
fichier_Picarro='CFADS59-20181013-Data.dat'
fichier_meteo='Meteodata_Campaign20181012'
fichier_gps='20181012.csv'
fichier_garmin='Garmin_20181012.csv'
fichier_felix_interp = 'sync_data_2018-10-12_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-10-12_sebastien_interp.csv'

#HEURE = [datetime(2018,10,06, i, 00, 00, 00) for i in range(2,14)]
#WIND_DIRECTION = [110, 110, 100, 100, 100, 10, 50, 30, 40, 20, 40, 100]
#WIND_SPEED = [19, 17, 11, 9, 7, 15, 11, 9, 11, 9, 9, 9]
#WIND_SPEED = [x / 3.6 for x in WIND_SPEED]


######################################
## Calibration factors 
############################################

filename_calibration = path_calibration + fichier_calibration 	# chemin du fichier a traiter

fil=open(filename_calibration, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

calibration_time, co2, co2d, ch4 = [], [], [], []

for ll in range(1, nbl):

    d = (' '.join(donnees[ll].split())).split(' ')[0]
    year = int(('/'.join(donnees[ll].split())).split('/')[2]) + 2000
    month = int(('/'.join(donnees[ll].split())).split('/')[0])
    day = int(('/'.join(donnees[ll].split())).split('/')[1])
   
    d = (' '.join(donnees[ll].split())).split(' ')[1]
    hour = int((':'.join(d.split())).split(':')[0])
    minute = int((':'.join(d.split())).split(':')[1])
    sec = float((':'.join(d.split())).split(':')[2])
    second = int(sec)
    
    if hour == int((':'.join(beginning.split())).split(':')[0]) and minute >= int((':'.join(beginning.split())).split(':')[1]) and minute <= int((':'.join(ending.split())).split(':')[1]):
		calibration_time.append(datetime(year,month,day,hour,minute,second))
		co2.append(float((','.join(donnees[ll].split())).split(',')[14]))
		co2d.append(float((','.join(donnees[ll].split())).split(',')[15]))				
		ch4.append(float((','.join(donnees[ll].split())).split(',')[16]))			

#plt.plot(calibration_time,ch4)
#plt.show()

tps_1, tps_2, tps_3, tps_4 = [], [], [], []
ch4_low_1, ch4_high_1, ch4_low_2, ch4_high_2 = [], [], [], []
co2_low_1, co2_high_1, co2_low_2, co2_high_2 = [], [], [], []

for ll in range(0, len(calibration_time)):
	if (calibration_time[ll].minute >= int((':'.join(beginning.split())).split(':')[1]) + 4) and (calibration_time[ll].minute <= int((':'.join(beginning.split())).split(':')[1]) + 9):
		tps_1.append(calibration_time[ll])
		ch4_low_1.append(ch4[ll])
		co2_low_1.append(co2[ll])

	if (calibration_time[ll].minute >= int((':'.join(beginning.split())).split(':')[1]) + 14) and (calibration_time[ll].minute <= int((':'.join(beginning.split())).split(':')[1]) + 19):
		tps_2.append(calibration_time[ll])
		ch4_high_1.append(ch4[ll])
		co2_high_1.append(co2[ll])

	if (calibration_time[ll].minute >= int((':'.join(beginning.split())).split(':')[1]) + 24) and (calibration_time[ll].minute <= int((':'.join(beginning.split())).split(':')[1]) + 29):
		tps_3.append(calibration_time[ll])
		ch4_low_2.append(ch4[ll])
		co2_low_2.append(co2[ll])

	if (calibration_time[ll].minute >= int((':'.join(beginning.split())).split(':')[1]) + 34) and (calibration_time[ll].minute <= int((':'.join(beginning.split())).split(':')[1]) + 39):
		tps_4.append(calibration_time[ll])
		ch4_high_2.append(ch4[ll])
		co2_high_2.append(co2[ll])

#plt.plot(tps_1,ch4_low_1)
#plt.plot(tps_2,ch4_high_1)
#plt.plot(tps_3,ch4_low_2)
#plt.plot(tps_4,ch4_high_2)
#plt.show()

print np.mean(ch4_low_1)
print np.mean(ch4_low_2)
print np.mean([np.mean(ch4_low_1),np.mean(ch4_low_2)])

slope_CH4, intercept_CH4, r_value_CH4, p_value, std_errb = stats.linregress( [np.mean([np.mean(ch4_low_1),np.mean(ch4_low_2)]),np.mean([np.mean(ch4_high_1),np.mean(ch4_high_2)])] , [tanks[1][1],tanks[0][1]] )
print('CH4:', slope_CH4,intercept_CH4)

slope_CO2, intercept_CO2, r_value_CO2, p_value, std_errb = stats.linregress( [np.mean([np.mean(co2_low_1),np.mean(co2_low_2)]),np.mean([np.mean(co2_high_1),np.mean(co2_high_2)])] , [tanks[1][2],tanks[0][2]] )
print('CO2:', slope_CO2,intercept_CO2)		



######################################
## Picarro
############################################
				
filename_Picarro = path_Picarro + fichier_Picarro 	# chemin du fichier a traiter

fil=open(filename_Picarro, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

Picarro_time, Picarro_time_epoch, co2, co2d, co2_cal, ch4, ch4d, ch4_cal, h2o = [], [], [], [], [], [], [], [], []

Picarro_shift = timedelta(seconds=20)

for ll in range(1, nbl):

    d = (' '.join(donnees[ll].split())).split(' ')[0]
    year = int(('/'.join(d.split())).split('/')[2]) + 2000
    month = int(('/'.join(d.split())).split('/')[0])
    day = int(('/'.join(d.split())).split('/')[1])

    d = (' '.join(donnees[ll].split())).split(' ')[1]
    hour = int((':'.join(d.split())).split(':')[0])
    minute = int((':'.join(d.split())).split(':')[1])
    sec = float((':'.join(d.split())).split(':')[2])
    second = int(sec)
    millisec = int((sec - second)*1000000)  

    Picarro_time.append(datetime(year,month,day,hour,minute,second,millisec)+Picarro_shift)
    Picarro_time_epoch.append( (datetime(year,month,day,hour,minute,second,millisec) - datetime(1970,1,1)).total_seconds() )
    
    co2.append(float((','.join(donnees[ll].split())).split(',')[14]))
    co2d.append(float((','.join(donnees[ll].split())).split(',')[15]))
    co2_cal.append(float((','.join(donnees[ll].split())).split(',')[15]) * slope_CO2 + intercept_CO2)				
    ch4.append(float((','.join(donnees[ll].split())).split(',')[16]))			
    h2o.append(float((','.join(donnees[ll].split())).split(',')[17]))
    ch4d.append( float((','.join(donnees[ll].split())).split(',')[16]) / (1 - 0.00982 * float((','.join(donnees[ll].split())).split(',')[17]) - 2.393 * 10**-4 * float((','.join(donnees[ll].split())).split(',')[17]) * float((','.join(donnees[ll].split())).split(',')[17])) )
    ch4_cal.append( float((','.join(donnees[ll].split())).split(',')[16]) / (1 - 0.00982 * float((','.join(donnees[ll].split())).split(',')[17]) - 2.393 * 10**-4 * float((','.join(donnees[ll].split())).split(',')[17]) * float((','.join(donnees[ll].split())).split(',')[17])) * slope_CH4 + intercept_CH4 )




######################################
## MeteoData
############################################

path_meteo = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Weather_Station/' 					# chemin du dossier contenant le fichier a decouper
filename_meteo = path_meteo + fichier_meteo 	# chemin du fichier a traiter

fil=open(filename_meteo, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

meteo_time, wind_speed, wind_direction, temperature, Relative_Humidity, Pressure = [], [], [], [], [], []

meteo_shift = timedelta(seconds=0)
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

    meteo_time.append(datetime(year,month,day,hour,minute,second)+meteo_shift)
    wind_speed.append(float((','.join(donnees[ll].split())).split(',')[2]))				
    wind_direction.append(float((','.join(donnees[ll].split())).split(',')[3]))			
    temperature.append(float((','.join(donnees[ll].split())).split(',')[4]))
    Relative_Humidity.append(float((','.join(donnees[ll].split())).split(',')[5]))
    Pressure.append(float((','.join(donnees[ll].split())).split(',')[6]))

'''
plt.plot(meteo_time, wind_speed, 'b+')
plt.ylabel('Measured wind speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()

plt.plot(meteo_time, wind_direction, 'b+')
plt.ylabel('Measured wind direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()
'''
######################################
## GPSData
############################################

# Felix

path_gps='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/GPS/' 
filename_gps = path_gps + fichier_gps 	# chemin du fichier a traiter

fil=open(filename_gps, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

gps_time, gps_time_epoch, lat, lon, alt = [], [], [], [], []

for ll in range(1, nbl):
	    if	str((','.join(donnees[ll].split())).split(',')[8]) != 'network':
    		d = (','.join(donnees[ll].split())).split(',')[0]
   		d = ('T'.join(d.split())).split('T')[0]
    		year = int(('-'.join(d.split())).split('-')[0])
    		month = int(('-'.join(d.split())).split('-')[1])
    		day = int(('-'.join(d.split())).split('-')[2])

    		d = (','.join(donnees[ll].split())).split(',')[0]
    		d = ('T'.join(d.split())).split('T')[1]
    		hour = int((':'.join(d.split())).split(':')[0])
    		minute = int((':'.join(d.split())).split(':')[1])
    		sec = float((':'.join(d.split())).split(':')[2][0:2])
    		second = int(sec)

    		gps_time.append(datetime(year,month,day,hour,minute,second))
    		gps_time_epoch.append( (datetime(year,month,day,hour,minute,second) - datetime(1970,1,1)).total_seconds() )
    		lat.append(float((','.join(donnees[ll].split())).split(',')[1]))				
    		lon.append(float((','.join(donnees[ll].split())).split(',')[2]))
    		alt.append(float((','.join(donnees[ll].split())).split(',')[3]))		


lat_gps_interp, lon_gps_interp, alt_gps_interp, time_gps_interp, ch4_gps_interp, co2_gps_interp, ch4_cal_gps_interp, co2_cal_gps_interp, h2o_gps_interp = [], [], [], [], [], [], [], [], []	

for ii in range(0,len(Picarro_time)):
	if Picarro_time[ii] >= gps_time[0] and Picarro_time[ii] <= gps_time[-1]:
		lat_gps_interp.append(np.interp(Picarro_time_epoch[ii],gps_time_epoch,lat))
		lon_gps_interp.append(np.interp(Picarro_time_epoch[ii],gps_time_epoch,lon))
		alt_gps_interp.append(np.interp(Picarro_time_epoch[ii],gps_time_epoch,alt))
		time_gps_interp.append(Picarro_time[ii])
		ch4_gps_interp.append(ch4[ii])
		co2_gps_interp.append(co2[ii])
		ch4_cal_gps_interp.append(ch4_cal[ii])
		co2_cal_gps_interp.append(co2_cal[ii])
		h2o_gps_interp.append(h2o[ii])



# garmin

path_gps='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/GPS/' 
filename_garmin = path_gps + fichier_garmin
fil=open(filename_garmin, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)

garmin_time, garmin_time_epoch, lat_garmin, lon_garmin, alt_garmin = [], [], [], [], []

for ll in range(1, nbl):
	lat_garmin.append(float((','.join(donnees[ll].split())).split(',')[1]))
	lon_garmin.append(float((','.join(donnees[ll].split())).split(',')[0]))
	alt_garmin.append(float((','.join(donnees[ll].split())).split(',')[5]))

	d = (','.join(donnees[ll].split())).split(',')[6]
	year = int(('/'.join(d.split())).split('/')[0])
	month = int(('/'.join(d.split())).split('/')[1])
	day = int(('/'.join(d.split())).split('/')[2])
	d = (','.join(donnees[ll].split())).split(',')[7]
	hour = int((':'.join(d.split())).split(':')[0])
	minute = int((':'.join(d.split())).split(':')[1])
	sec = float((':'.join(d.split())).split(':')[2][:2])
	second = int(sec)
	millisecond = int(0)
    	garmin_time.append(datetime(year,month,day,hour,minute,second,millisecond))
	garmin_time_epoch.append( (datetime(year,month,day,hour,minute,second,millisecond) - datetime(1970,1,1)).total_seconds() )


lat_garmin_interp, lon_garmin_interp, alt_garmin_interp, time_garmin_interp, ch4_garmin_interp, co2_garmin_interp, ch4_cal_garmin_interp, co2_cal_garmin_interp, h2o_garmin_interp = [], [], [], [], [], [], [], [], []	

for ii in range(0,len(Picarro_time)):
	if Picarro_time[ii] >= garmin_time[0] and Picarro_time[ii] <= garmin_time[-1]:
		lat_garmin_interp.append(np.interp(Picarro_time_epoch[ii],garmin_time_epoch,lat_garmin))
		lon_garmin_interp.append(np.interp(Picarro_time_epoch[ii],garmin_time_epoch,lon_garmin))
		alt_garmin_interp.append(np.interp(Picarro_time_epoch[ii],garmin_time_epoch,alt_garmin))
		time_garmin_interp.append(Picarro_time[ii])
		ch4_garmin_interp.append(ch4[ii])
		co2_garmin_interp.append(co2[ii])
		ch4_cal_garmin_interp.append(ch4_cal[ii])
		co2_cal_garmin_interp.append(co2_cal[ii])
		h2o_garmin_interp.append(h2o[ii])






###########################################
# wind correction
###########################################

R = 6371000	# meters



################################
# garmin gps data
###############################

car_s_garmin, car_d_garmin, garmin_time_w = [], [], []

for ii in range(1,len(lat_garmin_interp)):
	garmin_time_w.append(Picarro_time[ii])

	distance = R * math.radians( math.sqrt(math.pow(math.cos(math.radians(lat_garmin_interp[ii-1])) * (lon_garmin_interp[ii-1] - lon_garmin_interp[ii]) , 2) + math.pow(lat_garmin_interp[ii-1] - lat_garmin_interp[ii], 2)) )
	temps = Picarro_time[ii]-Picarro_time[ii-1]
	car_s_garmin.append( distance / temps.total_seconds() )


	X = math.cos(math.radians(lat_garmin_interp[ii])) * math.sin(math.radians(lon_garmin_interp[ii]-lon_garmin_interp[ii-1]))
	Y = math.cos(math.radians(lat_garmin_interp[ii-1])) * math.sin(math.radians(lat_garmin_interp[ii])) - math.sin(math.radians(lat_garmin_interp[ii-1])) * math.cos(math.radians(lat_garmin_interp[ii])) * math.cos(math.radians(lon_garmin_interp[ii] - lon_garmin_interp[ii-1]))
	if math.degrees(math.atan2( X , Y )) >= 0:
		car_d_garmin.append(math.degrees(math.atan2( X , Y )) ) 	# /!\ car direction to 
	if math.degrees(math.atan2( X , Y )) < 0:
		car_d_garmin.append(math.degrees(math.atan2( X , Y )) + 360)


#plt.plot(meteo_time, wind_speed, 'yx', label='Measured speed')
#plt.plot(garmin_time_w, car_s_garmin, 'b+', label='Car speed')
#plt.ylabel('Speed (m/s)')
#ax = plt.gca()
#ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
#ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
#plt.legend()
#plt.show()

#plt.plot(meteo_time, wind_direction, 'yx', label='Measured Direction')
#plt.plot(garmin_time_w, car_d_garmin, 'r+', label='Car Direction')
#plt.ylabel('Direction (degree)')
#ax = plt.gca()
#ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
#ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
#plt.legend()
#plt.show()


wind_speed_garmin_corr, wind_direction_garmin_corr, time_corr = [], [], []
Cs, Ws, Cd, Wd = [], [], [], []

#time_test = []
#speed_test = []
#direction_test = []
wind_speed_garmin_corr_stop, wind_direction_garmin_corr_stop, time_corr_stop = [], [], []

for ii in range(0,len(meteo_time)):
	#for ll in range(0,len(garmin_time_w)):
	for ll in range(0,len(garmin_time_w)-1):
			if meteo_time[ii].day == garmin_time_w[ll].day and meteo_time[ii].hour == garmin_time_w[ll].hour and meteo_time[ii].minute == garmin_time_w[ll].minute and meteo_time[ii].second == garmin_time_w[ll].second:

				#if wind_speed[ii] > car_s_garmin[ll] :			# filter data when car speed higher than wind speed
				#if car_s_garmin[ll] > 1:				# filter data when car stop
				#if abs(wind_direction_pol[ii] - car_d_garmin_pol[ll]) < 25 and wind_speed[ii] > car_s_garmin[ll]:	

				if abs(car_s_garmin[ll]-car_s_garmin[ll+1]) < 0.5: 			# filter when big acceleration and braking
					#time_test.append(garmin_time_w[ll])
					#speed_test.append(car_s_garmin[ll])
					#direction_test.append(car_d_garmin[ll])					
						

					U_w = ( - wind_speed[ii] * math.sin( math.radians(wind_direction[ii]) ) )
					V_w = ( - wind_speed[ii] * math.cos( math.radians(wind_direction[ii]) ) )

					U_c = ( - car_s_garmin[ll] * math.sin( math.radians(car_d_garmin[ll]) ) )
					V_c = ( - car_s_garmin[ll] * math.cos( math.radians(car_d_garmin[ll]) ) )

					Cs.append(car_s_garmin[ll])
					Ws.append(wind_speed[ii])
					Cd.append(car_d_garmin[ll])
					Wd.append(wind_direction[ii])

					time_corr.append(garmin_time_w[ll])

					wind_speed_garmin_corr.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))


					
												

					#	print(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ), wind_speed[ii],wind_direction[ii],car_s_garmin[ll],car_d_garmin[ll])

					#if car_d_garmin[ll] > 330 :
					#	print(math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) ), wind_speed[ii],wind_direction[ii],car_s_garmin[ll],car_d_garmin[ll])

					direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
					if direction >= 0:
						wind_direction_garmin_corr.append( direction )
					if direction < 0:
						wind_direction_garmin_corr.append( direction + 360 )


					if car_s_garmin[ll] <= 1:
						time_corr_stop.append(garmin_time_w[ll])
						wind_speed_garmin_corr_stop.append(math.sqrt( (U_w - U_c)**2 + (V_w - V_c)**2 ))		
						direction = math.degrees( math.atan2( -(U_w - U_c), -(V_w - V_c) ) )
						if direction >= 0:
							wind_direction_garmin_corr_stop.append( direction )
						if direction < 0:
							wind_direction_garmin_corr_stop.append( direction + 360 )



#plt.plot(meteo_time, wind_speed, 'yx', label='Measured speed')
#plt.plot(garmin_time_w, car_s_garmin, 'b+', label='Car speed')
#plt.plot(time_test, speed_test, 'r+', label='Acceleration or braking')
#plt.ylabel('Speed (m/s)')
#ax = plt.gca()
#ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
#ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
#plt.legend()
#plt.show()

#plt.plot(meteo_time, wind_direction, 'yx', label='Measured Direction')
#plt.plot(garmin_time_w, car_d_garmin, 'b+', label='Car Direction')
#plt.plot(time_test, direction_test, 'r+', label='Acceleration or braking')
#plt.ylabel('Direction (degree)')
#ax = plt.gca()
#ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
#ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
#plt.legend()
#plt.show()


# plot correlation
plt.plot(wind_direction_garmin_corr,Wd,'b+')
plt.xlabel('Corrected wind direction (degree)')
plt.ylabel('Measured direction (degree)')
plt.show()

plt.plot(wind_direction_garmin_corr,Cd,'b+')
plt.xlabel('Corrected wind direction (degree)')
plt.ylabel('Car direction (degree)')
plt.show()

plt.plot(wind_speed_garmin_corr,Ws,'b+')
plt.xlabel('Corrected wind speed (degree)')
plt.ylabel('Measured speed (degree)')
plt.show()

plt.plot(wind_speed_garmin_corr,Cs,'b+')
plt.xlabel('Corrected wind speed (degree)')
plt.ylabel('Car speed (degree)')
plt.show()


plt.plot(Cs,Ws,'b+')
#plt.plot(speed_test,Ms_test,'r+')
plt.xlabel('Car speed (m/s)')
plt.ylabel('Measured speed (m/s)')
plt.show()

plt.plot(Cd,Wd,'b+')
#plt.plot(direction_test,Md_test,'r+')
plt.xlabel('Car direction (degree)')
plt.ylabel('Measured direction (degree)')
plt.show()

#plot time series
plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr, wind_speed_garmin_corr, 'b+', label='Corrected wind')
#plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()


plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr, wind_direction_garmin_corr, 'b+', label='Corrected wind')
#plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()




plt.plot(time_corr, wind_speed_garmin_corr, 'b+', label='Corrected wind')
plt.plot(time_corr_stop, wind_speed_garmin_corr_stop, 'cx', label='Corrected wind with stopped car')
#plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()

plt.plot(time_corr, wind_direction_garmin_corr, 'b+', label='Corrected wind')
plt.plot(time_corr_stop, wind_direction_garmin_corr_stop, 'cx', label='Corrected windwith stopped car')
#plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()


"""

########################## 
# Felix GPS data
###########################


car_s_gps = []
car_d_gps = []
gps_time_w = []
car_d_gps_pol=[]


for ii in range(1,len(lat_gps_interp)):
	gps_time_w.append(Picarro_time[ii])

	distance = R * math.radians( math.sqrt(math.pow(math.cos(math.radians(lat_gps_interp[ii-1])) * (lon_gps_interp[ii-1] - lon_gps_interp[ii]) , 2) + math.pow(lat_gps_interp[ii-1] - lat_gps_interp[ii], 2)) )
	temps = Picarro_time[ii]-Picarro_time[ii-1]
	car_s_gps.append( distance / temps.total_seconds() )


	X = math.cos(math.radians(lat_gps_interp[ii])) * math.sin(math.radians(lon_gps_interp[ii]-lon_gps_interp[ii-1]))
	Y = math.cos(math.radians(lat_gps_interp[ii-1])) * math.sin(math.radians(lat_gps_interp[ii])) - math.sin(math.radians(lat_gps_interp[ii-1])) * math.cos(math.radians(lat_gps_interp[ii])) * math.cos(math.radians(lon_gps_interp[ii] - lon_gps_interp[ii-1]))
	if math.degrees(math.atan2( X , Y )) >= 0:
		car_d_gps.append(math.degrees(math.atan2( X , Y )) ) 	# /!\ car direction to 
	if math.degrees(math.atan2( X , Y )) < 0:
		car_d_gps.append(math.degrees(math.atan2( X , Y )) + 360)
	if ( 90 - math.degrees(math.atan2( X , Y )) + 180 ) <= 360:
		car_d_gps_pol.append( 90 - math.degrees(math.atan2( X , Y )) + 180)
	if ( 90 - math.degrees(math.atan2( X , Y )) + 180 ) > 360:
		car_d_gps_pol.append( 90 - math.degrees(math.atan2( X , Y )) + 180 - 360)


plt.plot(meteo_time, wind_speed, 'yx', label='Measured speed')
plt.plot(gps_time_w, car_s_gps, 'b+', label='Car speed')
plt.ylabel('Speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.legend()
plt.show()


plt.plot(meteo_time, wind_direction_pol, 'yx', label='Measured Direction')
plt.plot(gps_time_w, car_d_gps_pol, 'r+', label='Car Direction')
plt.ylabel('Direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.legend()
plt.show()

wind_speed_gps_corr=[]
wind_direction_gps_corr=[]
time_corr=[]


U_w=[]
V_w=[]
U_c=[]
V_c=[] 

for ii in range(0,len(wind_direction)):
	U_w.append( wind_speed[ii] * math.cos( math.radians(wind_direction_pol[ii]) ) )
	V_w.append( wind_speed[ii] * math.sin( math.radians(wind_direction_pol[ii]) ) )	

for ii in range(0,len(car_s_gps)):
	U_c.append( car_s_gps[ii] * math.cos( math.radians(car_d_gps_pol[ii]) ) )
	V_c.append( car_s_gps[ii] * math.sin( math.radians(car_d_gps_pol[ii]) ) )

Cs=[]
Ws=[]
Cd=[]
Wd=[]


for ii in range(0,len(meteo_time)):
	for ll in range(0,len(gps_time_w)):
			if meteo_time[ii].day == gps_time_w[ll].day and meteo_time[ii].hour == gps_time_w[ll].hour and meteo_time[ii].minute == gps_time_w[ll].minute and meteo_time[ii].second == gps_time_w[ll].second:

				Cs.append(car_s_gps[ll])
				Ws.append(wind_speed[ii])
				Cd.append(car_d_gps_pol[ll])
				Wd.append(wind_direction_pol[ii])

				time_corr.append(gps_time_w[ll])

				wind_speed_gps_corr.append(math.sqrt( (U_w[ii] - U_c[ll])**2 + (V_w[ii] - V_c[ll])**2 ))
				direction = 90 - math.degrees( math.atan2( V_w[ii] - V_c[ll] , U_w[ii] - U_c[ll] ) )
				if direction >= 0:
						wind_direction_gps_corr.append( direction )
				if direction < 0:
						wind_direction_gps_corr.append( direction + 360 )				
				
plt.plot(time_corr, Ws, 'yx', label='Measured speed')
plt.plot(time_corr, Cs, 'b+', label='Car speed')
plt.ylabel('Speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.legend()
plt.show()


plt.plot(Cs,Ws,'b+')
plt.xlabel('Car speed (m/s)')
plt.ylabel('Measured speed (m/s)')
plt.show()

plt.plot(Cd,Wd,'b+')
plt.xlabel('Car direction (degree)')
plt.ylabel('Measured direction (degree)')
plt.show()

plt.plot(meteo_time, wind_speed, 'cx', label='Measured wind')
plt.plot(time_corr, wind_speed_gps_corr, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_SPEED, 'ko', label='Pearson wind')
plt.ylabel('Wind speed (m/s)')
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()

plt.plot(meteo_time, wind_direction, 'cx', label='Measured wind')
plt.plot(time_corr, wind_direction_gps_corr, 'b+', label='Corrected wind')
plt.plot(HEURE, WIND_DIRECTION, 'ko', label='Pearson wind')
plt.ylabel('Wind direction (degree)')
plt.legend()
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=100))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))
plt.show()

"""





###########################################
# Creation fichier data-sync
###########################################

try:
	os.makedirs('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')
except OSError:
	pass

os.chdir('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')



#### felix

if os.path.exists(fichier_felix_interp):		# if file exists delete 
  os.remove(fichier_felix_interp)


nom_felix_interp = open(fichier_felix_interp, "w")

pressure = 0

nom_felix_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')

for ii in range(0,len(time_gps_interp)):
	print time_gps_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f")
	
	for ll in range(0,len(meteo_time)):
			if time_gps_interp[ii].day == meteo_time[ll].day and time_gps_interp[ii].hour == meteo_time[ll].hour and time_gps_interp[ii].minute == meteo_time[ll].minute and time_gps_interp[ii].second == meteo_time[ll].second:				
	
    				ws_uncorr = wind_speed[ll]				
    				wd_uncorr = wind_direction[ll]			
    				temp = temperature[ll]
    				#Relative_Humidity[ll]
    				pressure = Pressure[ll]
	

	#### GPS Data
	
	if pressure != 0:

		nom_felix_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (time_gps_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_gps_interp[ii],'amb[ii]',ch4_gps_interp[ii],ch4_cal_gps_interp[ii],'co[ii]',co2_gps_interp[ii],co2_cal_gps_interp[ii],'cod[ii]','cog[jj]','gasp[ii]',h2o_gps_interp[ii],'hdop[jj]','heading[jj]',lat_gps_interp[ii],lon_gps_interp[ii],pressure,'rd1[ii]','rd2[ii]','sog[jj]','t[ii]',temp,'wd_corr[jj]',wd_uncorr,'ws_corr[jj]',ws_uncorr))

	if pressure == 0:

		nom_felix_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (time_gps_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_gps_interp[ii],'amb[ii]',ch4_gps_interp[ii],ch4_cal_gps_interp[ii],'co[ii]',co2_gps_interp[ii],co2_cal_gps_interp[ii],'cod[ii]','cog[jj]','gasp[ii]',h2o_gps_interp[ii],'hdop[jj]','heading[jj]',lat_gps_interp[ii],lon_gps_interp[ii],'Nan','rd1[ii]','rd2[ii]','sog[jj]','t[ii]','Nan','wd_corr[jj]','Nan','ws_corr[jj]','Nan'))
	
nom_felix_interp.close()




#### sebastien

if os.path.exists(fichier_sebastien_interp):		# if file exists delete 
  os.remove(fichier_sebastien_interp)


nom_sebastien_interp = open(fichier_sebastien_interp, "w")

pressure = 0

nom_sebastien_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')

for ii in range(0,len(time_garmin_interp)):
	print time_garmin_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f")
	
	for ll in range(0,len(meteo_time)):
			if time_garmin_interp[ii].day == meteo_time[ll].day and time_garmin_interp[ii].hour == meteo_time[ll].hour and time_garmin_interp[ii].minute == meteo_time[ll].minute and time_garmin_interp[ii].second == meteo_time[ll].second:				
	
    				ws_uncorr = wind_speed[ll]				
    				wd_uncorr = wind_direction[ll]			
    				temp = temperature[ll]
    				#Relative_Humidity[ll]
    				pressure = Pressure[ll]
	

	#### GPS Data
	
	if pressure != 0:

		nom_sebastien_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (time_garmin_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_garmin_interp[ii],'amb[ii]',ch4_garmin_interp[ii],ch4_cal_garmin_interp[ii],'co[ii]',co2_garmin_interp[ii],co2_cal_garmin_interp[ii],'cod[ii]','cog[jj]','gasp[ii]',h2o_garmin_interp[ii],'hdop[jj]','heading[jj]',lat_garmin_interp[ii],lon_garmin_interp[ii],pressure,'rd1[ii]','rd2[ii]','sog[jj]','t[ii]',temp,'wd_corr[jj]',wd_uncorr,'ws_corr[jj]',ws_uncorr))


	if pressure == 0:

		nom_sebastien_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (time_garmin_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_garmin_interp[ii],'amb[ii]',ch4_garmin_interp[ii],ch4_cal_garmin_interp[ii],'co[ii]',co2_garmin_interp[ii],co2_cal_garmin_interp[ii],'cod[ii]','cog[jj]','gasp[ii]',h2o_garmin_interp[ii],'hdop[jj]','heading[jj]',lat_garmin_interp[ii],lon_garmin_interp[ii],'Nan','rd1[ii]','rd2[ii]','sog[jj]','t[ii]','Nan','wd_corr[jj]','Nan','ws_corr[jj]','Nan'))
	
nom_sebastien_interp.close()



#######################################################################
# create kml_convert intermediate file
########################################################################

# Lecture du fichier de donnees
path_in='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/'+ jour_mesure +'/Data_files/'  					# chemin du dossier contenant le fichier a decouper
path_out='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/'+ jour_mesure +'/Inter_files/'
name = 'sync_data_'+ jour_mesure +'_felix' 	

filename=path_in + name + '_interp.csv'	# chemin du fichier a traiter
fil=open(filename, mode='r') 					
donnees = fil.readlines()						
nbl=len(donnees)							
					

try:
    os.makedirs(path_out)
except OSError:
    pass


EPOCH_TIME=[]
ALARM_STATUS=[]              
INST_STATUS=[]               
CavityPressure=[]            
CavityTemp=[]                
DasTemp=[]                   
EtalonTemp=[]                
WarmBoxTemp=[]                
species=[]                   
MPVPosition=[]               
OutletValve=[]               
solenoid_valves=[]           
C2H2=[]                      
CH4=[]                       
H2O=[]                       
GPS_ABS_LAT=[]              
GPS_ABS_LONG=[]

WS_PRESSURE=[]
WS_REL_HUMIDITY=[]
WS_TEMP=[]
WS_WIND_DIRECTION=[]
WS_WIND_SPEED=[]
GPS_FIT=[]
WS_WIND_LON=[]
WS_WIND_LAT=[]
WS_COS_HEADING=[]
WS_SIN_HEADING=[]
CAR_SPEED=[]             
  


os.chdir(path_out)
if os.path.exists(name + "_kml.dat"):
	os.remove(name + "_kml.dat")


nom = open(name + "_kml.dat", "w")  # titre du fichier creer
nom.write('EPOCH_TIME ALARM_STATUS INST_STATUS CavityPressure CavityTemp DasTemp EtalonTemp WarmBoxTemp species MPVPosition OutletValve solenoid_valves C2H2 CH4 H2O GPS_ABS_LAT GPS_ABS_LONG WS_PRESSURE WS_REL_HUMIDITY WS_TEMP WS_WIND_DIRECTION WS_WIND_SPEED GPS_FIT WS_WIND_LON WS_WIND_LAT WS_COS_HEADING WS_SIN_HEADING CAR_SPEED\n') 


for ll in range(1, nbl-1):                     ## modifier nb de lignes a decaler
    d = donnees[ll][0:19] 
    EPOCH_TIME.append((datetime.strptime(d,'%Y-%m-%d %H:%M:%S')- datetime(1970,1,1)).total_seconds())
    #EPOCH_TIME.append(float((','.join(donnees[ll].split())).split(',')[5]))
    #ALARM_STATUS.append(float((' '.join(donnees[ll].split())).split(' ')[6]))
    #INST_STATUS.append(float((' '.join(donnees[ll].split())).split(' ')[7]))    
    #CavityPressure.append(float((' '.join(donnees[ll].split())).split(' ')[8]))	
    #CavityTemp.append(float((' '.join(donnees[ll].split())).split(' ')[9]))
    #DasTemp.append(float((' '.join(donnees[ll].split())).split(' ')[10]))
    #EtalonTemp.append(float((' '.join(donnees[ll].split())).split(' ')[11]))
    #WarmBoxTemp.append(float((' '.join(donnees[ll].split())).split(' ')[12]))
    #species.append(float((' '.join(donnees[ll].split())).split(' ')[13]))
    #MPVPosition.append(float((' '.join(donnees[ll].split())).split(' ')[14]))
    #OutletValve.append(float((' '.join(donnees[ll].split())).split(' ')[15]))
    #solenoid_valves.append(float((' '.join(donnees[ll].split())).split(' ')[16]))
  
    C2H2.append(str((','.join(donnees[ll].split())).split(',')[8]))	
    CH4.append(str((','.join(donnees[ll].split())).split(',')[5]))
    H2O.append(str((','.join(donnees[ll].split())).split(',')[12]))
   
    GPS_ABS_LAT.append(float((','.join(donnees[ll].split())).split(',')[15]))
    GPS_ABS_LONG.append(float((','.join(donnees[ll].split())).split(',')[16]))      
    #WS_PRESSURE.append(float((' '.join(donnees[ll].split())).split(',')[24]))
    #WS_REL_HUMIDITY.append(float((' '.join(donnees[ll].split())).split(' ')[25]))

for ii in range(0,len(C2H2)):
    #nom.write("%-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s\n" %(EPOCH_TIME[ii], ALARM_STATUS[ii], INST_STATUS[ii], CavityPressure[ii], CavityTemp[ii], DasTemp[ii], EtalonTemp[ii], WarmBoxTemp[ii], species[ii], MPVPosition[ii], OutletValve[ii], solenoid_valves[ii], C2H2[ii], CH4[ii], H2O[ii], GPS_ABS_LAT[ii], GPS_ABS_LONG[ii], WS_PRESSURE[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii]))

	nom.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" %(EPOCH_TIME[ii], 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', C2H2[ii], CH4[ii], H2O[ii], GPS_ABS_LAT[ii], GPS_ABS_LONG[ii], 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan'))

nom.close()






####

name = 'sync_data_'+ jour_mesure +'_sebastien' 	

filename=path_in + name + '_interp.csv'	# chemin du fichier a traiter
fil=open(filename, mode='r') 					
donnees = fil.readlines()						
nbl=len(donnees)							
					

try:
    os.makedirs(path_out)
except OSError:
    pass


EPOCH_TIME=[]
ALARM_STATUS=[]              
INST_STATUS=[]               
CavityPressure=[]            
CavityTemp=[]                
DasTemp=[]                   
EtalonTemp=[]                
WarmBoxTemp=[]                
species=[]                   
MPVPosition=[]               
OutletValve=[]               
solenoid_valves=[]           
C2H2=[]                      
CH4=[]                       
H2O=[]                       
GPS_ABS_LAT=[]              
GPS_ABS_LONG=[]

WS_PRESSURE=[]
WS_REL_HUMIDITY=[]
WS_TEMP=[]
WS_WIND_DIRECTION=[]
WS_WIND_SPEED=[]
GPS_FIT=[]
WS_WIND_LON=[]
WS_WIND_LAT=[]
WS_COS_HEADING=[]
WS_SIN_HEADING=[]
CAR_SPEED=[]             
  


os.chdir(path_out)
if os.path.exists(name + "_kml.dat"):
	os.remove(name + "_kml.dat")


nom = open(name + "_kml.dat", "w")  # titre du fichier creer
nom.write('EPOCH_TIME ALARM_STATUS INST_STATUS CavityPressure CavityTemp DasTemp EtalonTemp WarmBoxTemp species MPVPosition OutletValve solenoid_valves C2H2 CH4 H2O GPS_ABS_LAT GPS_ABS_LONG WS_PRESSURE WS_REL_HUMIDITY WS_TEMP WS_WIND_DIRECTION WS_WIND_SPEED GPS_FIT WS_WIND_LON WS_WIND_LAT WS_COS_HEADING WS_SIN_HEADING CAR_SPEED\n') 


for ll in range(1, nbl-1):                     ## modifier nb de lignes a decaler
    d = donnees[ll][0:19] 
    EPOCH_TIME.append((datetime.strptime(d,'%Y-%m-%d %H:%M:%S')- datetime(1970,1,1)).total_seconds())
    #EPOCH_TIME.append(float((','.join(donnees[ll].split())).split(',')[5]))
    #ALARM_STATUS.append(float((' '.join(donnees[ll].split())).split(' ')[6]))
    #INST_STATUS.append(float((' '.join(donnees[ll].split())).split(' ')[7]))    
    #CavityPressure.append(float((' '.join(donnees[ll].split())).split(' ')[8]))	
    #CavityTemp.append(float((' '.join(donnees[ll].split())).split(' ')[9]))
    #DasTemp.append(float((' '.join(donnees[ll].split())).split(' ')[10]))
    #EtalonTemp.append(float((' '.join(donnees[ll].split())).split(' ')[11]))
    #WarmBoxTemp.append(float((' '.join(donnees[ll].split())).split(' ')[12]))
    #species.append(float((' '.join(donnees[ll].split())).split(' ')[13]))
    #MPVPosition.append(float((' '.join(donnees[ll].split())).split(' ')[14]))
    #OutletValve.append(float((' '.join(donnees[ll].split())).split(' ')[15]))
    #solenoid_valves.append(float((' '.join(donnees[ll].split())).split(' ')[16]))
  
    C2H2.append(str((','.join(donnees[ll].split())).split(',')[8]))	
    CH4.append(str((','.join(donnees[ll].split())).split(',')[5]))
    H2O.append(str((','.join(donnees[ll].split())).split(',')[12]))
   
    GPS_ABS_LAT.append(float((','.join(donnees[ll].split())).split(',')[15]))
    GPS_ABS_LONG.append(float((','.join(donnees[ll].split())).split(',')[16]))      
    #WS_PRESSURE.append(float((' '.join(donnees[ll].split())).split(',')[24]))
    #WS_REL_HUMIDITY.append(float((' '.join(donnees[ll].split())).split(' ')[25]))

for ii in range(0,len(C2H2)):
    #nom.write("%-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s %-25s\n" %(EPOCH_TIME[ii], ALARM_STATUS[ii], INST_STATUS[ii], CavityPressure[ii], CavityTemp[ii], DasTemp[ii], EtalonTemp[ii], WarmBoxTemp[ii], species[ii], MPVPosition[ii], OutletValve[ii], solenoid_valves[ii], C2H2[ii], CH4[ii], H2O[ii], GPS_ABS_LAT[ii], GPS_ABS_LONG[ii], WS_PRESSURE[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii], WS_REL_HUMIDITY[ii]))

	nom.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" %(EPOCH_TIME[ii], 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', C2H2[ii], CH4[ii], H2O[ii], GPS_ABS_LAT[ii], GPS_ABS_LONG[ii], 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan'))

nom.close()




