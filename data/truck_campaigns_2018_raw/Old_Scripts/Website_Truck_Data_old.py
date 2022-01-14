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
fichier_web_felix = 'datasource_felix_2018-08-15.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-08-15.txt'

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
fichier_web_felix = 'datasource_felix_2018-08-17.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-08-17.txt'

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
fichier_web_felix = 'datasource_felix_2018-08-27.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-08-27.txt'

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
fichier_web_felix = 'datasource_felix_2018-08-30.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-08-30.txt'

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
fichier_web_felix = 'datasource_felix_2018-09-26.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-09-26.txt'

#HEURE = [datetime(2018,9,27, i, 00, 00, 00) for i in range(2,11)]
#HEURE = [datetime(2018,8,30, i, 00, 00, 00) for i in range(15,24)]
#WIND_DIRECTION = [350, 10, 10, 20, 350, 340, 150, 160, 130]
#WIND_SPEED = [19, 17, 13, 11, 11, 6, 9, 9, 7]
#WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''
'''
# 2018-10-03
jour_mesure = '2018-10-03'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181003/' 				
fichier_Picarro='CFADS59-20181003-Data.dat'
fichier_meteo='Meteodata_Campaign20181003'
fichier_gps='20181003.csv'
fichier_garmin='Garmin_20181003.csv'
fichier_web_felix = 'datasource_felix_2018-10-03.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-10-03.txt'

#HEURE = [datetime(2018,9,27, i, 00, 00, 00) for i in range(2,11)]
#HEURE = [datetime(2018,8,30, i, 00, 00, 00) for i in range(15,24)]
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
fichier_web_felix = 'datasource_felix_2018-10-05.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-10-05.txt'

#HEURE = [datetime(2018,9,27, i, 00, 00, 00) for i in range(2,11)]
#HEURE = [datetime(2018,8,30, i, 00, 00, 00) for i in range(15,24)]
#WIND_DIRECTION = [350, 10, 10, 20, 350, 340, 150, 160, 130]
#WIND_SPEED = [19, 17, 13, 11, 11, 6, 9, 9, 7]
#WIND_SPEED = [x / 3.6 for x in WIND_SPEED]
'''

# 2018-10-12
jour_mesure = '2018-10-12'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181013/' 				
fichier_Picarro='CFADS59-20181013-Data.dat'
fichier_meteo='Meteodata_Campaign20181012'
fichier_gps='20181005.csv'	# !!
fichier_garmin='Garmin_20181012.csv'
fichier_web_felix = 'datasource_felix_2018-10-12.txt'
fichier_web_sebastien = 'datasource_sebastien_2018-10-12.txt'

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
    h2o.append(float((','.join(donnees[ll].split())).split(',')[17])*10000)
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
wind_direction_pol=[]


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
    #wind_direction.append(float((','.join(donnees[ll].split())).split(',')[3]))			
    temperature.append(float((','.join(donnees[ll].split())).split(',')[4]))
    Relative_Humidity.append(float((','.join(donnees[ll].split())).split(',')[5]))
    Pressure.append(float((','.join(donnees[ll].split())).split(',')[6]))

    if (90 - float((','.join(donnees[ll].split())).split(',')[3]) + 180 ) >= 0 :
    	wind_direction_pol.append( 90 - float((','.join(donnees[ll].split())).split(',')[3]) + 180 )
    if (90 - float((','.join(donnees[ll].split())).split(',')[3]) + 180 ) < 0 :
    	wind_direction_pol.append( 90 - float((','.join(donnees[ll].split())).split(',')[3]) + 180 + 360 )

    if (float((','.join(donnees[ll].split())).split(',')[3]) + 180) >= 360:
    	wind_direction.append(float((','.join(donnees[ll].split())).split(',')[3]) + 180 - 360)
    if (float((','.join(donnees[ll].split())).split(',')[3]) +180) < 360:
    	wind_direction.append(float((','.join(donnees[ll].split())).split(',')[3]) + 180 )



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

lat_gps_interp=[]	
lon_gps_interp=[]
alt_gps_interp=[]
time_gps_interp=[]
ch4_gps_interp=[]
co2_gps_interp=[]
ch4_cal_gps_interp=[]
co2_cal_gps_interp=[]
h2o_gps_interp=[]

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
time_garmin_interp=[]
ch4_garmin_interp=[]
co2_garmin_interp=[]
ch4_cal_garmin_interp=[]
co2_cal_garmin_interp=[]
h2o_garmin_interp=[]

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
# Creation fichier data-sync
###########################################

'''
## felix

p_time_avg = []
ch4_avg = []
co2_avg = []
h2o_avg = []
lat_avg = []
lon_avg = []
alt_avg = []
temp_avg = []
press_avg = []
ws_avg = []
wd_avg = []
temp_avg = []
press_avg = []

t1 = time_gps_interp[0]
check = time_gps_interp[0]

p_time = []
methane = []
carbon_dioxyde = []
water = []
lat = []
lon = []
alt = []
ws = []
wd = []
temp = []
press = []
vxs = []
vys = []


for ii in range(0,len(time_gps_interp)):
	#print time_gps_interp[ii]
	
	if (time_gps_interp[ii] - check).seconds < 4: 

		diff = (time_gps_interp[ii] - t1).seconds

		if diff <= 15:

			methane.append(ch4_cal_gps_interp[ii])
			carbon_dioxyde.append(co2_cal_gps_interp[ii])
			water.append(h2o_gps_interp[ii])
			p_time.append(time_gps_interp[ii])
			lat.append(lat_gps_interp[ii])
			lon.append(lon_gps_interp[ii])
			alt.append(alt_gps_interp[ii])

			check = time_gps_interp[ii]
			#print diff

			for ll in range(0,len(meteo_time)):
				if time_gps_interp[ii].day == meteo_time[ll].day and time_gps_interp[ii].hour == meteo_time[ll].hour and time_gps_interp[ii].minute == meteo_time[ll].minute and time_gps_interp[ii].second == meteo_time[ll].second:				
	
    					ws.append(wind_speed[ll])				
    					wd.append(wind_direction[ll])			
    					temp.append(temperature[ll])
    					press.append(Pressure[ll])
					vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
					vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))

	

		if diff > 15:
			ch4_avg.append(np.average(methane))
			co2_avg.append(np.average(carbon_dioxyde))
			h2o_avg.append(np.average(water))
			p_time_avg.append(p_time[3])
			lat_avg.append(lat[3])
			lon_avg.append(lon[3])
			alt_avg.append(alt[3])
    			ws_avg.append(np.average(ws))				

			# Wind conditions average
			# recombine into a theta, second line takes care of negative angles and angels greater than 360 and rotates into angel from North	
			thetas_avg = np.degrees(np.arctan2(np.average(vys), np.average(vxs)))
			wd_avg.append((450 - thetas_avg) % 360)
			#print '!!!!!'
			#print thetas_avg
			#print (450 - thetas_avg) % 360	


    			temp_avg.append(np.average(temp))
    			press_avg.append(np.average(press))

			

			p_time = []
			methane = []
			carbon_dioxyde = []
			water = []
			lat = []
			lon = []
			alt = []
			ws = []
			wd = []
			temp = []
			press = []
			vxs = []
			vys = []

			t1 = time_gps_interp[ii]
			methane.append(ch4_cal_gps_interp[ii])
			carbon_dioxyde.append(co2_cal_gps_interp[ii])
			water.append(h2o_gps_interp[ii])
			lat.append(lat_gps_interp[ii])
			lon.append(lon_gps_interp[ii])
			alt.append(alt_gps_interp[ii])


			check = time_gps_interp[ii]

			for ll in range(0,len(meteo_time)):
				if time_gps_interp[ii].day == meteo_time[ll].day and time_gps_interp[ii].hour == meteo_time[ll].hour and time_gps_interp[ii].minute == meteo_time[ll].minute and time_gps_interp[ii].second == meteo_time[ll].second:				
	
    					ws.append(wind_speed[ll])				
    					wd.append(wind_direction[ll])			
    					temp.append(temperature[ll])
    					press.append(Pressure[ll])
					vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
					vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))



	if (time_gps_interp[ii] - check).seconds >= 4: 
		print('Picarro stopped', check)	

		p_time = []
		methane = []
		carbon_dioxyde = []
		water = []
		lat = []
		lon = []
		alt = []
		ws = []
		wd = []
		temp = []
		press = []
		vxs = []
		vys = []

		t1 = time_gps_interp[ii]
		methane.append(ch4_cal_gps_interp[ii])
		carbon_dioxyde.append(co2_cal_gps_interp[ii])
		water.append(h2o_gps_interp[ii])
		lat.append(lat_gps_interp[ii])
		lon.append(lon_gps_interp[ii])
		alt.append(alt_gps_interp[ii])


		check = time_gps_interp[ii]

		for ll in range(0,len(meteo_time)):
				if time_gps_interp[ii].day == meteo_time[ll].day and time_gps_interp[ii].hour == meteo_time[ll].hour and time_gps_interp[ii].minute == meteo_time[ll].minute and time_gps_interp[ii].second == meteo_time[ll].second:				
	
    					ws.append(wind_speed[ll])				
    					wd.append(wind_direction[ll])			
    					temp.append(temperature[ll])
    					press.append(Pressure[ll])
					vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
					vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))







try:
	os.makedirs('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')
except OSError:
	pass

os.chdir('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')


if os.path.exists(fichier_web_felix):		# if file exists delete 
  os.remove(fichier_web_felix)

nom_felix = open(fichier_web_felix, "w")

for ii in range(0,len(ch4_avg)):

	#nom_felix.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s;\n" % (p_time_avg[ii],lat_avg[ii],lon_avg[ii],alt_avg[ii],temp_avg[ii],wd_avg[ii],ws_avg[ii],press_avg[ii],'nan',p_time_avg[ii],ch4_avg[ii],co2_avg[ii],'nan',h2o_avg[ii],p_time_avg[ii] ))
	nom_felix.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s;\n" % (p_time_avg[ii],lat_avg[ii],lon_avg[ii],alt_avg[ii],temp_avg[ii],'nan','nan',press_avg[ii],'nan',p_time_avg[ii],ch4_avg[ii],co2_avg[ii],'nan',h2o_avg[ii],p_time_avg[ii] ))

nom_felix.close()

'''


#### sebastien


p_time_avg = []
ch4_avg = []
co2_avg = []
h2o_avg = []
lat_garmin_avg = []
lon_garmin_avg = []
alt_garmin_avg = []
temp_avg = []
press_avg = []
ws_avg = []
wd_avg = []
temp_avg = []
press_avg = []

t1 = time_garmin_interp[0]
check = time_garmin_interp[0]

p_time = []
methane = []
carbon_dioxyde = []
water = []
lat_garmin = []
lon_garmin = []
alt_garmin = []
ws = []
wd = []
temp = []
press = []
vxs = []
vys = []


for ii in range(0,len(time_garmin_interp)):
	#print time_garmin_interp[ii]
	
	if (time_garmin_interp[ii] - check).seconds < 4: 

		diff = (time_garmin_interp[ii] - t1).seconds

		if diff <= 15:

			methane.append(ch4_cal_garmin_interp[ii])
			carbon_dioxyde.append(co2_cal_garmin_interp[ii])
			water.append(h2o_garmin_interp[ii])
			p_time.append(time_garmin_interp[ii])
			lat_garmin.append(lat_garmin_interp[ii])
			lon_garmin.append(lon_garmin_interp[ii])
			alt_garmin.append(alt_garmin_interp[ii])

			check = time_garmin_interp[ii]
			#print diff

			for ll in range(0,len(meteo_time)):
				if time_garmin_interp[ii].day == meteo_time[ll].day and time_garmin_interp[ii].hour == meteo_time[ll].hour and time_garmin_interp[ii].minute == meteo_time[ll].minute and time_garmin_interp[ii].second == meteo_time[ll].second:				
	
    					ws.append(wind_speed[ll])				
    					wd.append(wind_direction[ll])			
    					temp.append(temperature[ll])
    					press.append(Pressure[ll])
					vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
					vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))

	

		if diff > 15:
			ch4_avg.append(np.average(methane))
			co2_avg.append(np.average(carbon_dioxyde))
			h2o_avg.append(np.average(water))
			p_time_avg.append(p_time[3])
			lat_garmin_avg.append(lat_garmin[3])
			lon_garmin_avg.append(lon_garmin[3])
			alt_garmin_avg.append(alt_garmin[3])
    			ws_avg.append(np.average(ws))				

			# Wind conditions average
			# recombine into a theta, second line takes care of negative angles and angels greater than 360 and rotates into angel from North	
			thetas_avg = np.degrees(np.arctan2(np.average(vys), np.average(vxs)))
			wd_avg.append((450 - thetas_avg) % 360)
			#print '!!!!!'
			#print thetas_avg
			#print (450 - thetas_avg) % 360	


    			temp_avg.append(np.average(temp))
    			press_avg.append(np.average(press))

			

			p_time = []
			methane = []
			carbon_dioxyde = []
			water = []
			lat_garmin = []
			lon_garmin = []
			alt_garmin = []
			ws = []
			wd = []
			temp = []
			press = []
			vxs = []
			vys = []

			t1 = time_garmin_interp[ii]
			methane.append(ch4_cal_garmin_interp[ii])
			carbon_dioxyde.append(co2_cal_garmin_interp[ii])
			water.append(h2o_garmin_interp[ii])
			lat_garmin.append(lat_garmin_interp[ii])
			lon_garmin.append(lon_garmin_interp[ii])
			alt_garmin.append(alt_garmin_interp[ii])

			check = time_garmin_interp[ii]

			for ll in range(0,len(meteo_time)):
				if time_garmin_interp[ii].day == meteo_time[ll].day and time_garmin_interp[ii].hour == meteo_time[ll].hour and time_garmin_interp[ii].minute == meteo_time[ll].minute and time_garmin_interp[ii].second == meteo_time[ll].second:				
	
    					ws.append(wind_speed[ll])				
    					wd.append(wind_direction[ll])			
    					temp.append(temperature[ll])
    					press.append(Pressure[ll])
					vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
					vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))



	if (time_garmin_interp[ii] - check).seconds >= 4: 
		print('Picarro stopped', check)	

		p_time = []
		methane = []
		carbon_dioxyde = []
		water = []
		lat_garmin = []
		lon_garmin = []
		alt_garmin = []
		ws = []
		wd = []
		temp = []
		press = []
		vxs = []
		vys = []

		t1 = time_garmin_interp[ii]
		methane.append(ch4_cal_garmin_interp[ii])
		carbon_dioxyde.append(co2_cal_garmin_interp[ii])
		water.append(h2o_garmin_interp[ii])
		lat_garmin.append(lat_garmin_interp[ii])
		lon_garmin.append(lon_garmin_interp[ii])
		alt_garmin.append(alt_garmin_interp[ii])

		check = time_garmin_interp[ii]

		for ll in range(0,len(meteo_time)):
				if time_garmin_interp[ii].day == meteo_time[ll].day and time_garmin_interp[ii].hour == meteo_time[ll].hour and time_garmin_interp[ii].minute == meteo_time[ll].minute and time_garmin_interp[ii].second == meteo_time[ll].second:				
	
    					ws.append(wind_speed[ll])				
    					wd.append(wind_direction[ll])			
    					temp.append(temperature[ll])
    					press.append(Pressure[ll])
					vxs.append(wind_speed[ll] * np.sin(np.radians(wind_direction[ll])))	
					vys.append(wind_speed[ll] * np.cos(np.radians(wind_direction[ll])))



try:
	os.makedirs('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')
except OSError:
	pass



os.chdir('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')



if os.path.exists(fichier_web_sebastien):		# if file exists delete 
  os.remove(fichier_web_sebastien)

nom_sebastien = open(fichier_web_sebastien, "w")

for ii in range(0,len(ch4_avg)):

	#nom_sebastien.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s;\n" % (p_time_avg[ii],lat_garmin_avg[ii],lon_garmin_avg[ii],alt_garmin_avg[ii],temp_avg[ii],wd_avg[ii],ws_avg[ii],press_avg[ii],'nan',p_time_avg[ii],ch4_avg[ii],co2_avg[ii],'nan',h2o_avg[ii],p_time_avg[ii] ))
	nom_sebastien.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s;\n" % (p_time_avg[ii],lat_garmin_avg[ii],lon_garmin_avg[ii],alt_garmin_avg[ii],temp_avg[ii],'nan','nan',press_avg[ii],'nan',p_time_avg[ii],ch4_avg[ii],co2_avg[ii],'nan',h2o_avg[ii],p_time_avg[ii] ))

nom_sebastien.close()





