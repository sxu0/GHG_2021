# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:38:05 2018

@author: Sébastien
"""


import os
import datetime
from datetime import datetime
from datetime import timedelta
import pylab as pl
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates as md
from matplotlib.ticker import MaxNLocator
from scipy import stats
import math


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

# 2018-08-15
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180816/' 				
fichier_Picarro='CFADS59-20180816-0148-Data.dat'
fichier_meteo='Meteodata_Campaign20180815'
fichier_gps='20180815.csv'
fichier_garmin='Garmin_20180815.csv'
fichier_felix_interp = 'sync_data_2018-08-15_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-15_sebastien_interp.csv'

'''
# 2018-08-16
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180817/' 				
fichier_Picarro='CFADS59-20180817-0627-Data.dat'
fichier_meteo='Meteodata_Campaign20180817'
fichier_gps='20180817.csv'
fichier_garmin='Garmin_20180815.csv'
fichier_felix_interp = 'sync_data_2018-08-17_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-17_sebastien_interp.csv'
'''
'''
# 2018-08-27
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180828/' 				
fichier_Picarro='CFADS59-20180828-0317-Data.dat'
fichier_meteo='Meteodata_Campaign20180827'
fichier_gps='20180827.csv'
fichier_garmin='Garmin_20180827.csv'
fichier_felix_interp = 'sync_data_2018-08-27_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-27_sebastien_interp.csv'
'''
'''
# 2018-08-30
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180830/' 				
fichier_Picarro='CFADS59-20180830-1436-Data.dat'
fichier_meteo='Meteodata_Campaign20180830'
fichier_gps='20180830.csv'
fichier_garmin='Garmin_20180830.csv'
fichier_felix_interp = 'sync_data_2018-08-30_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-30_sebastien_interp.csv'
'''


######################################
## Calibration factors 
############################################

filename_calibration = path_calibration + fichier_calibration 	# chemin du fichier a traiter

fil=open(filename_calibration, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

calibration_time=[]
co2=[]
co2d=[]
ch4=[]

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

tps_1=[]
tps_2=[]
tps_3=[]
tps_4=[]
ch4_low_1=[]
co2_low_1=[]
ch4_high_1=[]
co2_high_1=[]
ch4_low_2=[]
co2_low_2=[]
ch4_high_2=[]
co2_high_2=[]

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

Picarro_time=[]
Picarro_time_epoch=[]
co2=[]
co2d=[]
co2_cal=[]
ch4=[]
ch4d=[]
ch4_cal=[] 
h2o=[]

Picarro_shift = timedelta(seconds=20)

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

meteo_time=[]
wind_speed=[]
wind_direction=[]
temperature=[]
Relative_Humidity=[]
Pressure=[]

meteo_shift = timedelta(seconds=7)

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

plt.plot(meteo_time, wind_speed, 'b+')
plt.ylabel('Measured wind speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(meteo_time, wind_direction, 'b+')
plt.ylabel('Measured wind direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

######################################
## GPSData
############################################

# Felix

path_gps='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/GPS/' 
filename_gps = path_gps + fichier_gps 	# chemin du fichier a traiter

fil=open(filename_gps, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

gps_time=[]
gps_time_epoch=[]
lat=[]
lon=[]
alt=[]

for ll in range(1, nbl):
    #print (','.join(donnees[ll].split())).split(',')[8]
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

lat_interp=[]	
lon_interp=[]
alt_interp=[]

for ii in range(0,len(Picarro_time)):
	lat_interp.append(np.interp(Picarro_time_epoch[ii],gps_time_epoch,lat))
	lon_interp.append(np.interp(Picarro_time_epoch[ii],gps_time_epoch,lon))
	alt_interp.append(np.interp(Picarro_time_epoch[ii],gps_time_epoch,alt))

# garmin

filename_garmin = path_gps + fichier_garmin
fil=open(filename_garmin, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)

garmin_time=[]
garmin_time_epoch=[]		
lat_garmin=[]	
lon_garmin=[]
alt_garmin=[]	

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


lat_garmin_interp=[]	
lon_garmin_interp=[]
alt_garmin_interp=[]

for ii in range(0,len(Picarro_time)):
	lat_garmin_interp.append(np.interp(Picarro_time_epoch[ii],garmin_time_epoch,lat_garmin))
	lon_garmin_interp.append(np.interp(Picarro_time_epoch[ii],garmin_time_epoch,lon_garmin))
	alt_garmin_interp.append(np.interp(Picarro_time_epoch[ii],garmin_time_epoch,alt_garmin))


###########################################
# wind correction
###########################################

degToRad = math.pi / 180
RadToDeg = 180 / math.pi
R = 6371000	# meters

car_s_garmin = []
car_d_garmin = []
garmin_time_w = []


'''
for ii in range(1,len(lat_garmin)):
	garmin_time_w.append(garmin_time[ii])

	distance = R * math.radians( math.sqrt(math.pow(math.cos(math.radians(lat_garmin[ii-1])) * (lon_garmin[ii-1] - lon_garmin[ii]) , 2) + math.pow(lat_garmin[ii-1] - lat_garmin[ii], 2)) )
	temps = garmin_time[ii]-garmin_time[ii-1]
	car_s_garmin.append( distance / temps.total_seconds())
	
	X = math.cos(math.radians(lat_garmin[ii])) * math.sin(math.radians(lon_garmin[ii]-lon_garmin[ii-1]))
	Y = math.cos(math.radians(lat_garmin[ii-1])) * math.sin(math.radians(lat_garmin[ii])) - math.sin(math.radians(lat_garmin[ii-1])) * math.cos(math.radians(lat_garmin[ii])) * math.cos(math.radians(lon_garmin[ii] - lon_garmin[ii-1]))
	if math.degrees(math.atan2( X , Y )) -180 >= 0:
		car_d_garmin.append(math.degrees(math.atan2( X , Y ))-180) 	# /!\ car direction from 
	if math.degrees(math.atan2( X , Y )) -180 < 0:
		car_d_garmin.append(math.degrees(math.atan2( X , Y )) -180 + 360)
'''

for ii in range(1,len(lat_garmin_interp)):
	garmin_time_w.append(Picarro_time[ii])

	distance = R * math.radians( math.sqrt(math.pow(math.cos(math.radians(lat_garmin_interp[ii-1])) * (lon_garmin_interp[ii-1] - lon_garmin_interp[ii]) , 2) + math.pow(lat_garmin_interp[ii-1] - lat_garmin_interp[ii], 2)) )
	temps = Picarro_time[ii]-Picarro_time[ii-1]
	car_s_garmin.append( distance / temps.total_seconds())
	
	X = math.cos(math.radians(lat_garmin_interp[ii])) * math.sin(math.radians(lon_garmin_interp[ii]-lon_garmin_interp[ii-1]))
	Y = math.cos(math.radians(lat_garmin_interp[ii-1])) * math.sin(math.radians(lat_garmin_interp[ii])) - math.sin(math.radians(lat_garmin_interp[ii-1])) * math.cos(math.radians(lat_garmin_interp[ii])) * math.cos(math.radians(lon_garmin_interp[ii] - lon_garmin_interp[ii-1]))
	if math.degrees(math.atan2( X , Y )) -180 >= 0:
		car_d_garmin.append(math.degrees(math.atan2( X , Y ))-180) 	# /!\ car direction from 
	if math.degrees(math.atan2( X , Y )) -180 < 0:
		car_d_garmin.append(math.degrees(math.atan2( X , Y )) -180 + 360)




plt.plot(garmin_time_w, car_s_garmin, 'b+')
plt.ylabel('Car speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(garmin_time_w, car_d_garmin, 'b+')
plt.ylabel('Direction from which the car comes (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

wind_speed_garmin_corr=[]
wind_direction_garmin_corr=[]


'''
for ii in range(0,len(meteo_time)):
	for ll in range(0,len(garmin_time_w)):
			if meteo_time[ii].day == garmin_time_w[ll].day and meteo_time[ii].hour == garmin_time_w[ll].hour and meteo_time[ii].minute == garmin_time_w[ll].minute and meteo_time[ii].second == garmin_time_w[ll].second:

				if math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) >= 0:
					wind_direction_garmin_corr.append(math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )))
				if math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) < 0:
					wind_direction_garmin_corr.append(math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) + 360)

				wind_speed_garmin_corr.append(math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll])), 2 ) ))
'''

diff_sp=[]
diff_dir=[]
meteo_sp_sc=[]
car_sp_sc=[]
				
for ii in range(0,len(meteo_time)):
	for ll in range(0,len(Picarro_time)):

			if meteo_time[ii].day == Picarro_time[ll].day and meteo_time[ii].hour == Picarro_time[ll].hour and meteo_time[ii].minute == Picarro_time[ll].minute and meteo_time[ii].second == Picarro_time[ll].second:

				diff_sp.append(wind_speed[ii]-car_s_garmin[ll])
				diff_dir.append(wind_direction[ii]-car_d_garmin[ll])

				meteo_sp_sc.append(wind_speed[ii])
				car_sp_sc.append(car_s_garmin[ll])


				if math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) >= 0:
					wind_direction_garmin_corr.append(math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )))
				if math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) < 0:
					wind_direction_garmin_corr.append(math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) + 360)

				wind_speed_garmin_corr.append(math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll])), 2 ) ))



plt.plot(meteo_sp_sc,car_sp_sc,'b+')
plt.xlabel('Measured wind speed (m/s)')
plt.ylabel('Car speed (m/s)')
plt.show()

plt.plot(garmin_time_w, wind_speed_garmin_corr, 'b+')
plt.ylabel('Corrected wind speed (m/s)')
#plt.plot(garmin_time_w, diff_sp, 'b+')
#plt.ylabel('Measured wind speed - Truck speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(garmin_time_w, wind_direction_garmin_corr, 'b+')
plt.ylabel('Corrected wind direction (degree)')
#plt.plot(garmin_time_w, diff_dir, 'b+')
#plt.ylabel('Measured wind direction - Truck direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()





car_s_gps = []
car_d_gps = []
gps_time_w = []

for ii in range(1,len(lat)):
	gps_time_w.append(gps_time[ii])

	distance = R * degToRad * math.sqrt(math.pow(math.cos(lat[ii-1] * degToRad ) * (lon[ii-1] - lon[ii]) , 2) + math.pow(lat[ii-1] - lat[ii], 2))
	temps = gps_time[ii]-gps_time[ii-1]
	car_s_gps.append( distance / temps.total_seconds() *3.6)
	
	X = math.cos(lat[ii]* degToRad) * math.sin((lon[ii]-lon[ii-1])* degToRad)
	Y = math.cos(lat[ii-1]* degToRad) * math.sin(lat[ii]* degToRad) - math.sin(lat[ii-1]* degToRad) * math.cos(lat[ii]* degToRad) * math.cos((lon[ii] - lon[ii-1])* degToRad)
	if math.degrees(math.atan2( X , Y )) >= 0:
		car_d_gps.append(math.degrees(math.atan2( X , Y )))
	if math.degrees(math.atan2( X , Y )) < 0:
		car_d_gps.append(math.degrees(math.atan2( X , Y )))





###########################################
# Creation fichier data-sync
###########################################

print(len(Picarro_time),len(gps_time),len(garmin_time))

os.chdir('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/')


if os.path.exists(fichier_felix_interp):		# if file exists delete 
  os.remove(fichier_felix_interp)
if os.path.exists(fichier_sebastien_interp):		# if file exists delete 
  os.remove(fichier_sebastien_interp)


nom_felix_interp = open(fichier_felix_interp, "w")
nom_sebastien_interp = open(fichier_sebastien_interp, "w")


nom_felix_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')
nom_sebastien_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')

for ii in range(0,len(Picarro_time)):
	print Picarro_time[ii]
	
	for ll in range(0,len(meteo_time)):
			if Picarro_time[ii].day == meteo_time[ll].day and Picarro_time[ii].hour == meteo_time[ll].hour and Picarro_time[ii].minute == meteo_time[ll].minute and Picarro_time[ii].second == meteo_time[ll].second:				
	
    				ws_uncorr = wind_speed[ll]				
    				wd_uncorr = wind_direction[ll]			
    				temp = temperature[ll]
    				#Relative_Humidity[ll]
    				pressure = Pressure[ll]
	

	#### GPS Data

	nom_felix_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (Picarro_time[ii],alt_interp[ii],'amb[ii]',ch4[ii],ch4d[ii],'co[ii]',co2[ii],co2d[ii],'cod[ii]','cog[jj]','gasp[ii]',h2o[ii],'hdop[jj]','heading[jj]',lat_interp[ii],lon_interp[ii],pressure,'rd1[ii]','rd2[ii]','sog[jj]','t[ii]',temp,'wd_corr[jj]',wd_uncorr,'ws_corr[jj]',ws_uncorr))
	nom_sebastien_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (Picarro_time[ii],alt_garmin_interp[ii],'amb[ii]',ch4[ii],ch4d[ii],'co[ii]',co2[ii],co2d[ii],'cod[ii]','cog[jj]','gasp[ii]',h2o[ii],'hdop[jj]','heading[jj]',lat_garmin_interp[ii],lon_garmin_interp[ii],pressure,'rd1[ii]','rd2[ii]','sog[jj]','t[ii]',temp,'wd_corr[jj]',wd_uncorr,'ws_corr[jj]',ws_uncorr))


nom_felix_interp.close()
nom_sebastien_interp.close()










