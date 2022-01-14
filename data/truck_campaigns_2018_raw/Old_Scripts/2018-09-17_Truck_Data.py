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


'''
# 2018-08-15
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180816/' 				
fichier_Picarro='CFADS59-20180816-0148-Data.dat'
fichier_meteo='Meteodata_Campaign20180815'
fichier_gps='20180815.csv'
fichier_garmin='Garmin_20180815.csv'
fichier_felix_interp = 'sync_data_2018-08-15_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-15_sebastien_interp.csv'
'''
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

# 2018-08-30
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20180830/' 				
fichier_Picarro='CFADS59-20180830-1436-Data.dat'
fichier_meteo='Meteodata_Campaign20180830'
fichier_gps='20180830.csv'
fichier_garmin='Garmin_20180830.csv'
fichier_felix_interp = 'sync_data_2018-08-30_felix_interp.csv'
fichier_sebastien_interp = 'sync_data_2018-08-30_sebastien_interp.csv'



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
wind_vector=[]

#meteo_shift = timedelta(seconds=7)
meteo_shift = timedelta(seconds=29)

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

    if (float((','.join(donnees[ll].split())).split(',')[3]) - 180) >= 0:
    	wind_vector.append(float((','.join(donnees[ll].split())).split(',')[3]) - 180)
    if (float((','.join(donnees[ll].split())).split(',')[3]) - 180) < 0:
    	wind_vector.append(float((','.join(donnees[ll].split())).split(',')[3]) - 180 + 360)


plt.plot(meteo_time, wind_speed, 'b+')
plt.ylabel('Measured wind speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(meteo_time, wind_vector, 'b+')
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

R = 6371000	# meters


# garmin gps data
car_s_garmin = []
car_d_garmin = []
garmin_time_w = []


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



plt.plot(garmin_time_w, car_s_garmin, 'b+')
plt.ylabel('Car speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(garmin_time_w, car_d_garmin, 'b+')
plt.ylabel('Car direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

wind_speed_garmin_corr=[]
wind_direction_garmin_corr=[]





U_w = []
V_w = []

for ii in range(0,len(wind_speed)):
	U_w.append( - wind_speed[ii] *math.sin(math.radians(wind_direction[ii])) )
	V_w.append( - wind_speed[ii] *math.cos(math.radians(wind_direction[ii])) )

U_c = []
V_c = []

for ii in range(0,len(car_s_garmin)):
	U_c.append( - car_s_garmin[ii] *math.sin(math.radians(car_d_garmin[ii] + 180)) )
	V_c.append( - car_s_garmin[ii] *math.cos(math.radians(car_d_garmin[ii] + 180)) )


time_corr=[]
test=[]

for ii in range(0,len(meteo_time)):
	for ll in range(0,len(garmin_time_w)):
			if meteo_time[ii].day == garmin_time_w[ll].day and meteo_time[ii].hour == garmin_time_w[ll].hour and meteo_time[ii].minute == garmin_time_w[ll].minute and meteo_time[ii].second == garmin_time_w[ll].second:


				time_corr.append(garmin_time_w[ll])
				test.append(wind_speed[ii]-car_s_garmin[ll])
				print('!!!!!!!')
				print(wind_speed[ii], wind_direction[ii], U_w[ii], V_w[ii])
				print(car_s_garmin[ll], car_d_garmin[ll] -180, U_c[ll], V_c[ll])
				print math.sqrt( (U_w[ii] - U_c[ll])**2 + (V_w[ii] - V_c[ll])**2 )

				wind_speed_garmin_corr.append(math.sqrt( (U_w[ii] - U_c[ll])**2 + (V_w[ii] - V_c[ll])**2 ))


plt.plot(time_corr, test, 'b+')

plt.ylabel('Wind speed - Car speed (m/s)')

ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(time_corr, wind_speed_garmin_corr, 'b+')
plt.ylabel('Corrected wind speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()






"""
# convert angles to polar

wind_direction_pol=[]
time_corr=[]
test=[]

'''
for ii in range(0,len(wind_vector)):
	if wind_vector[ii] >= 0 and wind_vector[ii] < 90:
		wind_direction_pol.append(90-wind_vector[ii]) 
	if wind_vector[ii] >= 90 and wind_vector[ii] < 180:
		wind_direction_pol.append(wind_vector[ii]-90) 
	if wind_vector[ii] >= 180 and wind_vector[ii] < 270:
		wind_direction_pol.append(270-wind_vector[ii]) 
	if wind_vector[ii] >= 270 and wind_vector[ii] < 360:
		wind_direction_pol.append(wind_vector[ii]-270) 
'''


#####################################################
# conversion des directions du vent pour polyphemus #
#####################################################

for ii in range(0,len(wind_vector)):						    
	if wind_vector[ii] >= 0 and wind_vector[ii] <= 90:			    
		wind_direction_pol.append( (- wind_vector[ii] + 90) )	    	    
	if wind_vector[ii] > 90 and wind_vector[ii] <=360:			    
		wind_direction_pol.append( (- wind_vector[ii] +450) )	            
						    
#####################################################



car_d_garmin_pol=[]

'''
for ii in range(0,len(car_d_garmin)):
	if car_d_garmin[ii] >= 0 and car_d_garmin[ii] < 90:
		car_d_garmin_pol.append(90-car_d_garmin[ii]) 
	if car_d_garmin[ii] >= 90 and car_d_garmin[ii] < 180:
		car_d_garmin_pol.append(car_d_garmin[ii]-90) 
	if car_d_garmin[ii] >= 180 and car_d_garmin[ii] < 270:
		car_d_garmin_pol.append(270-car_d_garmin[ii]) 
	if car_d_garmin[ii] >= 270 and car_d_garmin[ii] < 360:
		car_d_garmin_pol.append(car_d_garmin[ii]-270) 
''' 

#####################################################
# conversion des directions du vent pour polyphemus #
#####################################################

for ii in range(0,len(car_d_garmin)):						    
	if car_d_garmin[ii] >= 0 and car_d_garmin[ii] <= 90:			    
		car_d_garmin_pol.append( (- car_d_garmin[ii] + 90) )	    	    
	if car_d_garmin[ii] > 90 and car_d_garmin[ii] <=360:			    
		car_d_garmin_pol.append( (- car_d_garmin[ii] +450) )	            
						    
#####################################################


#t = 0

for ii in range(0,len(meteo_time)):
	for ll in range(0,len(garmin_time_w)):

			if meteo_time[ii].day == garmin_time_w[ll].day and meteo_time[ii].hour == garmin_time_w[ll].hour and meteo_time[ii].minute == garmin_time_w[ll].minute and meteo_time[ii].second == garmin_time_w[ll].second:

				time_corr.append(garmin_time_w[ll])

				wind_speed_garmin_corr.append(math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll])), 2 ) ))

				
				#if math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll])), 2 ) ) > 6:
			
					#t = t + 1
					#print 


				
				if math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) >= 0:
					#wind_direction_garmin_corr_pol = math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) ))
					wind_direction_garmin_corr.append( 270 - math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) )

				if math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) < 0:
					#wind_direction_garmin_corr_pol = math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) + 360
					wind_direction_garmin_corr.append( 270 - math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) + 360 )
				
				'''
				if wind_direction_garmin_corr_pol >= 0 and wind_direction_garmin_corr_pol < 90:
					wind_direction_garmin_corr.append(90 - wind_direction_garmin_corr_pol + 180) 
				if wind_direction_garmin_corr_pol >= 90 and wind_direction_garmin_corr_pol < 180:
					wind_direction_garmin_corr.append(wind_direction_garmin_corr_pol - 90 + 180) 
				if wind_direction_garmin_corr_pol >= 180 and wind_direction_garmin_corr_pol < 270:
					wind_direction_garmin_corr.append(270 - wind_direction_garmin_corr_pol + 180) 
				if wind_direction_garmin_corr_pol >= 270 and wind_direction_garmin_corr_pol < 360:
					wind_direction_garmin_corr.append(wind_direction_garmin_corr_pol - 270 + 180) 
				
				'''



plt.plot(time_corr, wind_speed_garmin_corr, 'b+')
plt.ylabel('Corrected wind speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()


'''
plt.plot(time_corr, wind_direction_garmin_corr, 'b+')
plt.ylabel('Corrected wind direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()
'''
'''
plt.plot(test, wind_direction_garmin_corr, 'b+')
plt.ylabel('Corrected wind direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()
'''
"""









"""
# correction with Felix gps Data

car_s = []
car_d = []
time_w = []


for ii in range(1,len(lat_interp)):
	time_w.append(Picarro_time[ii])

	distance = R * math.radians( math.sqrt(math.pow(math.cos(math.radians(lat_interp[ii-1])) * (lon_interp[ii-1] - lon_interp[ii]) , 2) + math.pow(lat_interp[ii-1] - lat_interp[ii], 2)) )
	temps = Picarro_time[ii]-Picarro_time[ii-1]
	car_s.append( distance / temps.total_seconds())
	
	X = math.cos(math.radians(lat_interp[ii])) * math.sin(math.radians(lon_interp[ii]-lon_interp[ii-1]))
	Y = math.cos(math.radians(lat_interp[ii-1])) * math.sin(math.radians(lat_interp[ii])) - math.sin(math.radians(lat_interp[ii-1])) * math.cos(math.radians(lat_interp[ii])) * math.cos(math.radians(lon_interp[ii] - lon_interp[ii-1]))
	if math.degrees(math.atan2( X , Y )) >= 0:
		car_d.append(math.degrees(math.atan2( X , Y )) ) 	# /!\ car direction to 
	if math.degrees(math.atan2( X , Y )) < 0:
		car_d.append(math.degrees(math.atan2( X , Y )) + 360)



plt.plot(time_w, car_s, 'b+')
plt.ylabel('Car speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

plt.plot(time_w, car_d, 'b+')
plt.ylabel('Car direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()

wind_speed_corr=[]
wind_direction_corr=[]


'''
				
for ii in range(0,len(meteo_time)):
	for ll in range(0,len(Picarro_time)):

			if meteo_time[ii].day == Picarro_time[ll].day and meteo_time[ii].hour == Picarro_time[ll].hour and meteo_time[ii].minute == Picarro_time[ll].minute and meteo_time[ii].second == Picarro_time[ll].second:


				if math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) >= 0:
					wind_direction_garmin_corr.append(math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )))
				if math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) < 0:
					wind_direction_garmin_corr.append(math.degrees( math.atan2( -(wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll]))) , -(wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll]))) )) + 360)

				wind_speed_garmin_corr.append(math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin[ll])), 2 ) ))
'''


# Test avec modification des angles

wind_direction_pol=[]
time_corr=[]

for ii in range(0,len(wind_vector)):
	if wind_vector[ii] >= 0 and wind_vector[ii] < 90:
		wind_direction_pol.append(90-wind_vector[ii]) 
	if wind_vector[ii] >= 90 and wind_vector[ii] < 180:
		wind_direction_pol.append(wind_vector[ii]-90) 
	if wind_vector[ii] >= 180 and wind_vector[ii] < 270:
		wind_direction_pol.append(270-wind_vector[ii]) 
	if wind_vector[ii] >= 270 and wind_vector[ii] < 360:
		wind_direction_pol.append(wind_vector[ii]-270) 

car_d_pol=[]

for ii in range(0,len(car_d)):
	if car_d[ii] >= 0 and car_d[ii] < 90:
		car_d_pol.append(90-car_d[ii]) 
	if car_d[ii] >= 90 and car_d[ii] < 180:
		car_d_pol.append(car_d[ii]-90) 
	if car_d[ii] >= 180 and car_d[ii] < 270:
		car_d_pol.append(270-car_d[ii]) 
	if car_d[ii] >= 270 and car_d[ii] < 360:
		car_d_pol.append(car_d[ii]-270) 

#t = 0

for ii in range(0,len(meteo_time)):
	for ll in range(0,len(time_w)):

			if meteo_time[ii].day == time_w[ll].day and meteo_time[ii].hour == time_w[ll].hour and meteo_time[ii].minute == time_w[ll].minute and meteo_time[ii].second == time_w[ll].second:

				time_corr.append(time_w[ll])

				wind_speed_corr.append(math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s[ll]*math.cos(math.radians(car_d_pol[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s[ll]*math.sin(math.radians(car_d_pol[ll])), 2 ) ))

				
				#if math.sqrt( math.pow( wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s[ll]*math.cos(math.radians(car_d_pol[ll])), 2 ) + math.pow( wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s[ll]*math.sin(math.radians(car_d_pol[ll])), 2 ) ) > 6:
					#t = t + 1
					#print t


				'''
				if math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) >= 0:
					wind_direction_garmin_corr_pol = math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) ))

				if math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) < 0:
					wind_direction_garmin_corr_pol = math.degrees(math.atan2( (wind_speed[ii]*math.cos(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.cos(math.radians(car_d_garmin_pol[ll]))) , (wind_speed[ii]*math.sin(math.radians(wind_direction_pol[ii])) - car_s_garmin[ll]*math.sin(math.radians(car_d_garmin_pol[ll]))) )) + 360


				if wind_direction_garmin_corr_pol >= 0 and wind_direction_garmin_corr_pol < 90:
					wind_direction_garmin_corr.append(90 - wind_direction_garmin_corr_pol + 180) 
				if wind_direction_garmin_corr_pol >= 90 and wind_direction_garmin_corr_pol < 180:
					wind_direction_garmin_corr.append(wind_direction_garmin_corr_pol - 90 + 180) 
				if wind_direction_garmin_corr_pol >= 180 and wind_direction_garmin_corr_pol < 270:
					wind_direction_garmin_corr.append(270 - wind_direction_garmin_corr_pol + 180) 
				if wind_direction_garmin_corr_pol >= 270 and wind_direction_garmin_corr_pol < 360:
					wind_direction_garmin_corr.append(wind_direction_garmin_corr_pol - 270 + 180) 

				'''


plt.plot(time_corr, wind_speed_corr, 'b+')
plt.ylabel('Corrected wind speed (m/s)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()
'''
plt.plot(time_corr, wind_direction_garmin_corr, 'b+')
plt.ylabel('Corrected wind direction (degree)')
ax = plt.gca()
ax.xaxis.set_major_locator(md.MinuteLocator(interval=50))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.show()
'''

"""






"""

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


"""







