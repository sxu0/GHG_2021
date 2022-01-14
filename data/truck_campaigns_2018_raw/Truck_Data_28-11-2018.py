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
import time

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




# 2018-11-28
jour_mesure = '2018-11-28'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181128/' 				
fichier_Picarro='CFADS59-20181128-Data.dat'
fichier_airmar='Nov_28_2018.LOG'
fichier_interp='sync_data_2018-11-28.csv' 


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

print 'PICARRO'				
filename_Picarro = path_Picarro + fichier_Picarro 	# chemin du fichier a traiter

fil=open(filename_Picarro, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

Picarro_time, Picarro_time_epoch, co2, co2d, co2_cal, ch4, ch4d, ch4_cal, h2o = [], [], [], [], [], [], [], [], []
amb, gasp, temp_cav = [], [], []

Picarro_shift = timedelta(seconds=110)
#Picarro_shift = timedelta(seconds=110)
#Picarro_shift = timedelta(seconds=13+35)
#Picarro_shift = timedelta(seconds=20)

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

    if hour >= 19 and hour < 22:

    	Picarro_time.append(datetime(year,month,day,hour,minute,second,millisec) + Picarro_shift)
    	Picarro_time_epoch.append( (datetime(year,month,day,hour,minute,second,millisec) + Picarro_shift - datetime(1970,1,1)).total_seconds() )
    
    	amb.append( float((','.join(donnees[ll].split())).split(',')[5]) )
    	gasp.append( float((','.join(donnees[ll].split())).split(',')[4]) )
    	temp_cav.append( float((','.join(donnees[ll].split())).split(',')[3]) )

    	co2.append(float((','.join(donnees[ll].split())).split(',')[14]))
    	co2d.append(float((','.join(donnees[ll].split())).split(',')[15]))
    	co2_cal.append(float((','.join(donnees[ll].split())).split(',')[15]) * slope_CO2 + intercept_CO2)				
    	ch4.append(float((','.join(donnees[ll].split())).split(',')[16]))			
    	h2o.append(float((','.join(donnees[ll].split())).split(',')[17])*10000)
    	ch4d.append( float((','.join(donnees[ll].split())).split(',')[16]) / (1 - 0.00982 * float((','.join(donnees[ll].split())).split(',')[17]) - 2.393 * 10**-4 * float((','.join(donnees[ll].split())).split(',')[17]) * float((','.join(donnees[ll].split())).split(',')[17])) )
    	ch4_cal.append( float((','.join(donnees[ll].split())).split(',')[16]) / (1 - 0.00982 * float((','.join(donnees[ll].split())).split(',')[17]) - 2.393 * 10**-4 * float((','.join(donnees[ll].split())).split(',')[17]) * float((','.join(donnees[ll].split())).split(',')[17])) * slope_CH4 + intercept_CH4 )



#####

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

    if hour >= 22 or hour < 3:
    	Picarro_time.append(datetime(year,month,day,hour,minute,second,millisec) + Picarro_shift)
    	Picarro_time_epoch.append( (datetime(year,month,day,hour,minute,second,millisec) + Picarro_shift - datetime(1970,1,1)).total_seconds() )
    
    	amb.append( float((','.join(donnees[ll].split())).split(',')[5]) )
    	gasp.append( float((','.join(donnees[ll].split())).split(',')[4]) )
    	temp_cav.append( float((','.join(donnees[ll].split())).split(',')[3]) )

    	co2.append(float((','.join(donnees[ll].split())).split(',')[14]))
    	co2d.append(float((','.join(donnees[ll].split())).split(',')[15]))
    	co2_cal.append(float((','.join(donnees[ll].split())).split(',')[15]) * slope_CO2 + intercept_CO2)				
    	ch4.append(float((','.join(donnees[ll].split())).split(',')[16]))			
    	h2o.append(float((','.join(donnees[ll].split())).split(',')[17])*10000)
    	ch4d.append( float((','.join(donnees[ll].split())).split(',')[16]) / (1 - 0.00982 * float((','.join(donnees[ll].split())).split(',')[17]) - 2.393 * 10**-4 * float((','.join(donnees[ll].split())).split(',')[17]) * float((','.join(donnees[ll].split())).split(',')[17])) )
    	ch4_cal.append( float((','.join(donnees[ll].split())).split(',')[16]) / (1 - 0.00982 * float((','.join(donnees[ll].split())).split(',')[17]) - 2.393 * 10**-4 * float((','.join(donnees[ll].split())).split(',')[17]) * float((','.join(donnees[ll].split())).split(',')[17])) * slope_CH4 + intercept_CH4 )



######################################
## Airmar
############################################

print 'AIRMAR'

### part 1 ### 19:53 -> 20:14

path_airmar = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 					# chemin du dossier contenant le fichier a decouper
filename_airmar = path_airmar + fichier_airmar 	# chemin du fichier a traiter

fil=open(filename_airmar, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

meteo_shift = timedelta(seconds=0)

year_ = int(('-'.join(jour_mesure.split())).split('-')[0])
month_ = int(('-'.join(jour_mesure.split())).split('-')[1])
day_ = int(('-'.join(jour_mesure.split())).split('-')[2])

time_GPGGA, lat, lon, alt, hdop = [], [], [], [], []
time_WIMDA, pressure, temp, RH, dew_point, wd_corr, ws_corr = [], [], [], [], [], [], []
time_WIMWV, wd_uncorr, ws_uncorr = [], [], []
time_YXXDR, pres = [], []
time_HCHDG, hdg = [], []
time_GPZDA, t, t_epoch = [], [], []
time_GPRMC, cog, sog = [], [], []


for ll in range(0, nbl):
	if donnees[ll][17:23] == "$GPGGA" and (','.join(donnees[ll].split())).split(',')[4].strip():		# .strip() remove spaces and allow to select when there are GPS data available
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)
		
		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):

			if (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12) or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPGGA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPGGA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )	

			latitude = (','.join(donnees[ll].split())).split(',')[4]
			lat.append( float(latitude[0:2]) + float(latitude[2:])/60. )
			longitude = (','.join(donnees[ll].split())).split(',')[6]
			lon.append( -float(longitude[0:3]) - float(longitude[3:])/60. )
			alt.append( float( (','.join(donnees[ll].split())).split(',')[11] ) )
			hdop.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )

	if donnees[ll][17:23] == "$WIMDA" and (','.join(donnees[ll].split())).split(',')[21].strip():		# .strip() remove spaces and allow to select when there are GPS data available
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)
				
		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_WIMDA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_WIMDA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			pressure.append( float( (','.join(donnees[ll].split())).split(',')[5] ) * 1000 )
			temp.append( float( (','.join(donnees[ll].split())).split(',')[7] ) )
			RH.append( float( (','.join(donnees[ll].split())).split(',')[11] ) )
			dew_point.append( float( (','.join(donnees[ll].split())).split(',')[13] ) )
			wd_corr.append( float( (','.join(donnees[ll].split())).split(',')[15] ) )
			ws_corr.append( float( (','.join(donnees[ll].split())).split(',')[21] ) )

	if donnees[ll][17:23] == "$WIMWV" and (','.join(donnees[ll].split())).split(',')[3].strip():
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_WIMWV.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_WIMWV.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			wd_uncorr.append( float( (','.join(donnees[ll].split())).split(',')[3] ) )
			ws_uncorr.append( float( (','.join(donnees[ll].split())).split(',')[5] ) )

	if donnees[ll][17:23] == "$YXXDR" and donnees[ll][-10:-6] == "STNP":	
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):
	
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_YXXDR.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_YXXDR.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )
		
			pres.append( float( (','.join(donnees[ll].split())).split(',')[16] ) * 1000 )

	if donnees[ll][17:23] == "$HCHDG" and (','.join(donnees[ll].split())).split(',')[3].strip():	
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_HCHDG.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_HCHDG.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			hdg.append( float( (','.join(donnees[ll].split())).split(',')[3] ) )

	if donnees[ll][17:23] == "$GPZDA" and (','.join(donnees[ll].split())).split(',')[3].strip():
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPZDA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPZDA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )
			
			d = (','.join(donnees[ll].split())).split(',')[3]
			hour = int( d[0:2] )
			minute = int( d[2:4] )
			sec = float( d[4:9] )
	    		second = int(sec)
	    		millisec = int((sec - second)*1000000)
			day = int( (','.join(donnees[ll].split())).split(',')[4] )
			month = int( (','.join(donnees[ll].split())).split(',')[5] )
			year = int( (','.join(donnees[ll].split())).split(',')[6] )
			t_epoch.append( (datetime(year,month,day,hour,minute,second,millisec) - datetime(1970,1,1)).total_seconds() )
			t.append( datetime(year,month,day,hour,minute,second,millisec) )

	if donnees[ll][17:23] == "$GPRMC" and (','.join(donnees[ll].split())).split(',')[4] == 'A':
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ >= 19 and hour_ < 20) or (hour_ == 20 and minute_ < 14) or (hour_ == 20 and minute_ == 14 and second_ <= 37):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPRMC.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPRMC.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			cog.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )
			sog.append( float( (','.join(donnees[ll].split())).split(',')[9] ) * 1.852 )	# to convert knots to km/h


#### Interpolation of all data on GPZDA time

lat_interp, lon_interp, alt_interp, hdop_interp = [], [], [], []
pressure_interp, temp_interp, RH_interp, dew_point_interp, wd_corr_interp, ws_corr_interp = [], [], [], [], [], []
wd_uncorr_interp, ws_uncorr_interp = [], []
pres_interp = []
hdg_interp = []
sog_interp, cog_interp = [], []

for ii in range(0,len(time_GPZDA)):
	lat_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,lat))
	lon_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,lon))	
	alt_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,alt))
	hdop_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,hdop))

	pressure_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,pressure))
	temp_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,temp))
	RH_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,RH))
	dew_point_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,dew_point))
	wd_corr_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,wd_corr))
	ws_corr_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,ws_corr))

	wd_uncorr_interp.append(np.interp(time_GPZDA[ii],time_WIMWV,wd_uncorr))
	ws_uncorr_interp.append(np.interp(time_GPZDA[ii],time_WIMWV,ws_uncorr))

	pres_interp.append(np.interp(time_GPZDA[ii],time_YXXDR,pres))

	hdg_interp.append(np.interp(time_GPZDA[ii],time_HCHDG,hdg))

	sog_interp.append(np.interp(time_GPZDA[ii],time_GPRMC,sog))
	cog_interp.append(np.interp(time_GPZDA[ii],time_GPRMC,cog))


time_interp, time_interpol = [], []

for ii in range(0,int(t_epoch[-1]) - int(t_epoch[0]) + 1):
	time_interp.append(int(t_epoch[0]) + ii)
	time_interpol.append( datetime.fromtimestamp(int(t_epoch[0]) + ii) + timedelta(seconds=5*3600) )

A_time_interpol, lat_interpol, lon_interpol, alt_interpol, hdop_interpol = [], [], [], [], []
pressure_interpol, temp_interpol, RH_interpol, dew_point_interpol, wd_corr_interpol, ws_corr_interpol = [], [], [], [], [], []
wd_uncorr_interpol, ws_uncorr_interpol = [], []
pres_interpol = []
hdg_interpol = []
sog_interpol, cog_interpol = [], []

for ii in range(0,len(time_interp)):
	A_time_interpol.append(time_interpol[ii])
	lat_interpol.append(np.interp(time_interp[ii],time_GPZDA,lat_interp))
	lon_interpol.append(np.interp(time_interp[ii],time_GPZDA,lon_interp))	
	alt_interpol.append(np.interp(time_interp[ii],time_GPZDA,alt_interp))
	hdop_interpol.append(np.interp(time_interp[ii],time_GPZDA,hdop_interp))

	pressure_interpol.append(np.interp(time_interp[ii],time_GPZDA,pressure_interp))
	temp_interpol.append(np.interp(time_interp[ii],time_GPZDA,temp_interp))
	RH_interpol.append(np.interp(time_interp[ii],time_GPZDA,RH_interp))
	dew_point_interpol.append(np.interp(time_interp[ii],time_GPZDA,dew_point_interp))
	wd_corr_interpol.append(np.interp(time_interp[ii],time_GPZDA,wd_corr_interp))
	ws_corr_interpol.append(np.interp(time_interp[ii],time_GPZDA,ws_corr_interp))

	wd_uncorr_interpol.append(np.interp(time_interp[ii],time_GPZDA,wd_uncorr_interp))
	ws_uncorr_interpol.append(np.interp(time_interp[ii],time_GPZDA,ws_uncorr_interp))

	pres_interpol.append(np.interp(time_interp[ii],time_GPZDA,pres_interp))

	hdg_interpol.append(np.interp(time_interp[ii],time_GPZDA,hdg_interp))

	sog_interpol.append(np.interp(time_interp[ii],time_GPZDA,sog_interp))
	cog_interpol.append(np.interp(time_interp[ii],time_GPZDA,cog_interp))



### part 2 ### 20:42 -> 21:07


year_ = int(('-'.join(jour_mesure.split())).split('-')[0])
month_ = int(('-'.join(jour_mesure.split())).split('-')[1])
day_ = int(('-'.join(jour_mesure.split())).split('-')[2])

time_GPGGA, lat, lon, alt, hdop = [], [], [], [], []
time_WIMDA, pressure, temp, RH, dew_point, wd_corr, ws_corr = [], [], [], [], [], [], []
time_WIMWV, wd_uncorr, ws_uncorr = [], [], []
time_YXXDR, pres = [], []
time_HCHDG, hdg = [], []
time_GPZDA, t, t_epoch = [], [], []
time_GPRMC, cog, sog = [], [], []


for ll in range(0, nbl):
	if donnees[ll][17:23] == "$GPGGA" and (','.join(donnees[ll].split())).split(',')[4].strip():		# .strip() remove spaces and allow to select when there are GPS data available
		d = (','.join(donnees[ll].split())).split(',')[0]

		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)
		
		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):

			if (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12) or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPGGA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:

				time_GPGGA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )	

			latitude = (','.join(donnees[ll].split())).split(',')[4]
			lat.append( float(latitude[0:2]) + float(latitude[2:])/60. )
			longitude = (','.join(donnees[ll].split())).split(',')[6]
			lon.append( -float(longitude[0:3]) - float(longitude[3:])/60. )
			alt.append( float( (','.join(donnees[ll].split())).split(',')[11] ) )
			hdop.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )

	if donnees[ll][17:23] == "$WIMDA" and (','.join(donnees[ll].split())).split(',')[21].strip():		# .strip() remove spaces and allow to select when there are GPS data available
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)
				
		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_WIMDA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_WIMDA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			pressure.append( float( (','.join(donnees[ll].split())).split(',')[5] ) * 1000 )
			temp.append( float( (','.join(donnees[ll].split())).split(',')[7] ) )
			RH.append( float( (','.join(donnees[ll].split())).split(',')[11] ) )
			dew_point.append( float( (','.join(donnees[ll].split())).split(',')[13] ) )
			wd_corr.append( float( (','.join(donnees[ll].split())).split(',')[15] ) )
			ws_corr.append( float( (','.join(donnees[ll].split())).split(',')[21] ) )

	if donnees[ll][17:23] == "$WIMWV" and (','.join(donnees[ll].split())).split(',')[3].strip():
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_WIMWV.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_WIMWV.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			wd_uncorr.append( float( (','.join(donnees[ll].split())).split(',')[3] ) )
			ws_uncorr.append( float( (','.join(donnees[ll].split())).split(',')[5] ) )

	if donnees[ll][17:23] == "$YXXDR" and donnees[ll][-10:-6] == "STNP":	
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):
	
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_YXXDR.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_YXXDR.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )
		
			pres.append( float( (','.join(donnees[ll].split())).split(',')[16] ) * 1000 )

	if donnees[ll][17:23] == "$HCHDG" and (','.join(donnees[ll].split())).split(',')[3].strip():	
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_HCHDG.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_HCHDG.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			hdg.append( float( (','.join(donnees[ll].split())).split(',')[3] ) )

	if donnees[ll][17:23] == "$GPZDA" and (','.join(donnees[ll].split())).split(',')[3].strip():
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPZDA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPZDA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )
			
			d = (','.join(donnees[ll].split())).split(',')[3]
			hour = int( d[0:2] )
			minute = int( d[2:4] )
			sec = float( d[4:9] )
	    		second = int(sec)
	    		millisec = int((sec - second)*1000000)
			day = int( (','.join(donnees[ll].split())).split(',')[4] )
			month = int( (','.join(donnees[ll].split())).split(',')[5] )
			year = int( (','.join(donnees[ll].split())).split(',')[6] )
			t_epoch.append( (datetime(year,month,day,hour,minute,second,millisec) - datetime(1970,1,1)).total_seconds() )
			t.append( datetime(year,month,day,hour,minute,second,millisec) )

	if donnees[ll][17:23] == "$GPRMC" and (','.join(donnees[ll].split())).split(',')[4] == 'A':
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if (hour_ == 20 and minute_ >= 42) or (hour_ == 21 and minute_ < 07):

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPRMC.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPRMC.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			cog.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )
			sog.append( float( (','.join(donnees[ll].split())).split(',')[9] ) * 1.852 )	# to convert knots to km/h



#### Interpolation of all data on GPZDA time

lat_interp, lon_interp, alt_interp, hdop_interp = [], [], [], []
pressure_interp, temp_interp, RH_interp, dew_point_interp, wd_corr_interp, ws_corr_interp = [], [], [], [], [], []
wd_uncorr_interp, ws_uncorr_interp = [], []
pres_interp = []
hdg_interp = []
sog_interp, cog_interp = [], []

for ii in range(0,len(time_GPZDA)):
	lat_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,lat))
	lon_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,lon))	
	alt_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,alt))
	hdop_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,hdop))

	pressure_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,pressure))
	temp_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,temp))
	RH_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,RH))
	dew_point_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,dew_point))
	wd_corr_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,wd_corr))
	ws_corr_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,ws_corr))

	wd_uncorr_interp.append(np.interp(time_GPZDA[ii],time_WIMWV,wd_uncorr))
	ws_uncorr_interp.append(np.interp(time_GPZDA[ii],time_WIMWV,ws_uncorr))

	pres_interp.append(np.interp(time_GPZDA[ii],time_YXXDR,pres))

	hdg_interp.append(np.interp(time_GPZDA[ii],time_HCHDG,hdg))

	sog_interp.append(np.interp(time_GPZDA[ii],time_GPRMC,sog))
	cog_interp.append(np.interp(time_GPZDA[ii],time_GPRMC,cog))


time_interp, time_interpol = [], []

for ii in range(0,int(t_epoch[-1]) - int(t_epoch[0]) + 1):
	time_interp.append(int(t_epoch[0]) + ii)
	time_interpol.append( datetime.fromtimestamp(int(t_epoch[0]) + ii) + timedelta(seconds=5*3600) )


for ii in range(0,len(time_interp)):
	A_time_interpol.append(time_interpol[ii])
	lat_interpol.append(np.interp(time_interp[ii],time_GPZDA,lat_interp))
	lon_interpol.append(np.interp(time_interp[ii],time_GPZDA,lon_interp))	
	alt_interpol.append(np.interp(time_interp[ii],time_GPZDA,alt_interp))
	hdop_interpol.append(np.interp(time_interp[ii],time_GPZDA,hdop_interp))

	pressure_interpol.append(np.interp(time_interp[ii],time_GPZDA,pressure_interp))
	temp_interpol.append(np.interp(time_interp[ii],time_GPZDA,temp_interp))
	RH_interpol.append(np.interp(time_interp[ii],time_GPZDA,RH_interp))
	dew_point_interpol.append(np.interp(time_interp[ii],time_GPZDA,dew_point_interp))

	wd_corr_interpol.append(np.interp(time_interp[ii],time_GPZDA,wd_corr_interp))
	ws_corr_interpol.append(np.interp(time_interp[ii],time_GPZDA,ws_corr_interp))

	wd_uncorr_interpol.append(np.interp(time_interp[ii],time_GPZDA,wd_uncorr_interp))
	ws_uncorr_interpol.append(np.interp(time_interp[ii],time_GPZDA,ws_uncorr_interp))

	pres_interpol.append(np.interp(time_interp[ii],time_GPZDA,pres_interp))

	hdg_interpol.append(np.interp(time_interp[ii],time_GPZDA,hdg_interp))

	sog_interpol.append(np.interp(time_interp[ii],time_GPZDA,sog_interp))
	cog_interpol.append(np.interp(time_interp[ii],time_GPZDA,cog_interp))



### part 3 ### 22:42 -> 02:22

year_ = int(('-'.join(jour_mesure.split())).split('-')[0])
month_ = int(('-'.join(jour_mesure.split())).split('-')[1])
day_ = int(('-'.join(jour_mesure.split())).split('-')[2])

time_GPGGA, lat, lon, alt, hdop = [], [], [], [], []
time_WIMDA, pressure, temp, RH, dew_point, wd_corr, ws_corr = [], [], [], [], [], [], []
time_WIMWV, wd_uncorr, ws_uncorr = [], [], []
time_YXXDR, pres = [], []
time_HCHDG, hdg = [], []
time_GPZDA, t, t_epoch = [], [], []
time_GPRMC, cog, sog = [], [], []


for ll in range(0, nbl):
	if donnees[ll][17:23] == "$GPGGA" and (','.join(donnees[ll].split())).split(',')[4].strip():		# .strip() remove spaces and allow to select when there are GPS data available
		d = (','.join(donnees[ll].split())).split(',')[0]

		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)
		
		if hour_ >= 22 or hour_ < 3:

			if (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12) or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPGGA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:

				time_GPGGA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )	

			latitude = (','.join(donnees[ll].split())).split(',')[4]
			lat.append( float(latitude[0:2]) + float(latitude[2:])/60. )
			longitude = (','.join(donnees[ll].split())).split(',')[6]
			lon.append( -float(longitude[0:3]) - float(longitude[3:])/60. )
			alt.append( float( (','.join(donnees[ll].split())).split(',')[11] ) )
			hdop.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )

	if donnees[ll][17:23] == "$WIMDA" and (','.join(donnees[ll].split())).split(',')[21].strip():		# .strip() remove spaces and allow to select when there are GPS data available
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )

    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)
				

		if hour_ >= 22 or hour_ < 3:

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_WIMDA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_WIMDA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			pressure.append( float( (','.join(donnees[ll].split())).split(',')[5] ) * 1000 )
			temp.append( float( (','.join(donnees[ll].split())).split(',')[7] ) )
			RH.append( float( (','.join(donnees[ll].split())).split(',')[11] ) )
			dew_point.append( float( (','.join(donnees[ll].split())).split(',')[13] ) )
			wd_corr.append( float( (','.join(donnees[ll].split())).split(',')[15] ) )
			ws_corr.append( float( (','.join(donnees[ll].split())).split(',')[21] ) )

	if donnees[ll][17:23] == "$WIMWV" and (','.join(donnees[ll].split())).split(',')[3].strip():
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if hour_ >= 22 or hour_ < 3:

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):

				time_WIMWV.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_WIMWV.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			wd_uncorr.append( float( (','.join(donnees[ll].split())).split(',')[3] ) )
			ws_uncorr.append( float( (','.join(donnees[ll].split())).split(',')[5] ) )

	if donnees[ll][17:23] == "$YXXDR" and donnees[ll][-10:-6] == "STNP":	
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if hour_ >= 22 or hour_ < 3:
	
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_YXXDR.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:

				time_YXXDR.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )
		
			pres.append( float( (','.join(donnees[ll].split())).split(',')[16] ) * 1000 )

	if donnees[ll][17:23] == "$HCHDG" and (','.join(donnees[ll].split())).split(',')[3].strip():	
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)


		if hour_ >= 22 or hour_ < 3:

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_HCHDG.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:

				time_HCHDG.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			hdg.append( float( (','.join(donnees[ll].split())).split(',')[3] ) )

	if donnees[ll][17:23] == "$GPZDA" and (','.join(donnees[ll].split())).split(',')[3].strip():
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if hour_ >= 22 or hour_ < 3:

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPZDA.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPZDA.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )
			
			d = (','.join(donnees[ll].split())).split(',')[3]
			hour = int( d[0:2] )
			minute = int( d[2:4] )
			sec = float( d[4:9] )
	    		second = int(sec)
	    		millisec = int((sec - second)*1000000)
			day = int( (','.join(donnees[ll].split())).split(',')[4] )
			month = int( (','.join(donnees[ll].split())).split(',')[5] )
			year = int( (','.join(donnees[ll].split())).split(',')[6] )
			t_epoch.append( (datetime(year,month,day,hour,minute,second,millisec) - datetime(1970,1,1)).total_seconds() )
			t.append( datetime(year,month,day,hour,minute,second,millisec) )

	if donnees[ll][17:23] == "$GPRMC" and (','.join(donnees[ll].split())).split(',')[4] == 'A':
		d = (','.join(donnees[ll].split())).split(',')[0]
		hour_ = int( (':'.join(d.split())).split(':')[0] )
		minute_ = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
    		second_ = int(sec_)
    		millisec_ = int((sec_ - second_)*1000000)

		if hour_ >= 22 or hour_ < 3:

			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
				time_GPRMC.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
			if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
				time_GPRMC.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

			cog.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )
			sog.append( float( (','.join(donnees[ll].split())).split(',')[9] ) * 1.852 )	# to convert knots to km/h





#### Interpolation of all data on GPZDA time

lat_interp, lon_interp, alt_interp, hdop_interp = [], [], [], []
pressure_interp, temp_interp, RH_interp, dew_point_interp, wd_corr_interp, ws_corr_interp = [], [], [], [], [], []
wd_uncorr_interp, ws_uncorr_interp = [], []
pres_interp = []
hdg_interp = []
sog_interp, cog_interp = [], []

for ii in range(0,len(time_GPZDA)):
	lat_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,lat))
	lon_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,lon))	
	alt_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,alt))
	hdop_interp.append(np.interp(time_GPZDA[ii],time_GPGGA,hdop))

	pressure_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,pressure))
	temp_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,temp))
	RH_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,RH))
	dew_point_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,dew_point))
	wd_corr_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,wd_corr))
	ws_corr_interp.append(np.interp(time_GPZDA[ii],time_WIMDA,ws_corr))

	wd_uncorr_interp.append(np.interp(time_GPZDA[ii],time_WIMWV,wd_uncorr))
	ws_uncorr_interp.append(np.interp(time_GPZDA[ii],time_WIMWV,ws_uncorr))

	pres_interp.append(np.interp(time_GPZDA[ii],time_YXXDR,pres))

	hdg_interp.append(np.interp(time_GPZDA[ii],time_HCHDG,hdg))


	sog_interp.append(np.interp(time_GPZDA[ii],time_GPRMC,sog))
	cog_interp.append(np.interp(time_GPZDA[ii],time_GPRMC,cog))



time_interp, time_interpol = [], []

for ii in range(0,int(t_epoch[-1]) - int(t_epoch[0]) + 1):
	time_interp.append(int(t_epoch[0]) + ii)
	time_interpol.append( datetime.fromtimestamp(int(t_epoch[0]) + ii) + timedelta(seconds=5*3600) )


for ii in range(0,len(time_interp)):
	A_time_interpol.append(time_interpol[ii])
	lat_interpol.append(np.interp(time_interp[ii],time_GPZDA,lat_interp))
	lon_interpol.append(np.interp(time_interp[ii],time_GPZDA,lon_interp))	
	alt_interpol.append(np.interp(time_interp[ii],time_GPZDA,alt_interp))
	hdop_interpol.append(np.interp(time_interp[ii],time_GPZDA,hdop_interp))

	pressure_interpol.append(np.interp(time_interp[ii],time_GPZDA,pressure_interp))

	temp_interpol.append(np.interp(time_interp[ii],time_GPZDA,temp_interp))
	RH_interpol.append(np.interp(time_interp[ii],time_GPZDA,RH_interp))
	dew_point_interpol.append(np.interp(time_interp[ii],time_GPZDA,dew_point_interp))

	wd_corr_interpol.append(np.interp(time_interp[ii],time_GPZDA,wd_corr_interp))
	ws_corr_interpol.append(np.interp(time_interp[ii],time_GPZDA,ws_corr_interp))

	wd_uncorr_interpol.append(np.interp(time_interp[ii],time_GPZDA,wd_uncorr_interp))
	ws_uncorr_interpol.append(np.interp(time_interp[ii],time_GPZDA,ws_uncorr_interp))

	pres_interpol.append(np.interp(time_interp[ii],time_GPZDA,pres_interp))

	hdg_interpol.append(np.interp(time_interp[ii],time_GPZDA,hdg_interp))

	sog_interpol.append(np.interp(time_interp[ii],time_GPZDA,sog_interp))
	cog_interpol.append(np.interp(time_interp[ii],time_GPZDA,cog_interp))












####################### Garmin GPS data from 22:19 to 22:42

######################################
## GPSData
############################################


path_gps='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/GPS/' 
filename_gps = path_gps + "Garmin_20181128.csv" 	# chemin du fichier a traiter

fil=open(filename_gps, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

garmin_time, garmin_time_epoch, lat_garmin, lon_garmin, alt_garmin = [], [], [], [], []

for ll in range(1, nbl):
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

	if (hour < 22 and hour > 20) or (hour == 22 and minute <= 42 ):		
    			garmin_time.append(datetime(year,month,day,hour,minute,second,millisecond))
			garmin_time_epoch.append( (datetime(year,month,day,hour,minute,second,millisecond) - datetime(1970,1,1)).total_seconds() )

			lat_garmin.append(float((','.join(donnees[ll].split())).split(',')[1]))
			lon_garmin.append(float((','.join(donnees[ll].split())).split(',')[0]))
			alt_garmin.append(float((','.join(donnees[ll].split())).split(',')[5]))
		

time_interp, time_interpol = [], []

for ii in range(0,int(garmin_time_epoch[-1]) - int(garmin_time_epoch[0]) + 1):
	time_interp.append(int(garmin_time_epoch[0]) + ii)
	time_interpol.append( datetime.fromtimestamp(int(garmin_time_epoch[0]) + ii) + timedelta(seconds=5*3600) )

garmin_time_interpol, lat_garmin_interpol, lon_garmin_interpol, alt_garmin_interpol = [], [], [], []

for ii in range(0,len(time_interp)):
	garmin_time_interpol.append(time_interpol[ii])
	lat_garmin_interpol.append(np.interp(time_interp[ii],garmin_time_epoch,lat_garmin))
	lon_garmin_interpol.append(np.interp(time_interp[ii],garmin_time_epoch,lon_garmin))	
	alt_garmin_interpol.append(np.interp(time_interp[ii],garmin_time_epoch,alt_garmin))





###########################################
# Creation fichier data-sync
###########################################

try:
	os.makedirs('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')
except OSError:
	pass

os.chdir('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/')


if os.path.exists(fichier_interp):		# if file exists delete 
  os.remove(fichier_interp)

nom_interp = open(fichier_interp, "w")

nom_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')

start_Airmar, start_Garmin = 0, 0

for jj in range(0,len(Picarro_time)):
	print Picarro_time[jj].strftime("%Y-%m-%d %H:%M:%S.%f")
	for ii in range(start_Airmar,len(A_time_interpol)):
		if Picarro_time[jj].day == A_time_interpol[ii].day and Picarro_time[jj].hour == A_time_interpol[ii].hour and Picarro_time[jj].minute == A_time_interpol[ii].minute and Picarro_time[jj].second == A_time_interpol[ii].second:
			print 'ok'
			nom_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (A_time_interpol[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_interpol[ii],amb[jj],ch4[jj],ch4_cal[jj],'co[ii]',co2[jj],co2_cal[jj],'cod[ii]',cog_interpol[ii],gasp[jj],h2o[jj],hdop_interpol[ii],hdg_interpol[ii],lat_interpol[ii],lon_interpol[ii],pres_interpol[ii],'rd1[ii]','rd2[ii]',sog_interpol[ii],temp_cav[jj],temp_interpol[ii],wd_corr_interpol[ii],wd_uncorr_interpol[ii],ws_corr_interpol[ii],ws_uncorr_interpol[ii]))
			start_Airmar = ii

	for ii in range(start_Garmin,len(garmin_time_interpol)):
		if Picarro_time[jj].day == garmin_time_interpol[ii].day and Picarro_time[jj].hour == garmin_time_interpol[ii].hour and Picarro_time[jj].minute == garmin_time_interpol[ii].minute and Picarro_time[jj].second == garmin_time_interpol[ii].second:
			#print 'ok'
			#nom_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (garmin_time_interpol[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_garmin_interpol[ii],amb_interpol[jj],ch4_interpol[jj],ch4_cal_interpol[jj],'co[ii]',co2_interpol[jj],co2_cal_interpol[jj],'cod[ii]','cog_interpol[ii]',gasp_interpol[jj],h2o_interpol[jj],'hdop_interpol[ii]','hdg_interpol[ii]',lat_garmin_interpol[ii],lon_garmin_interpol[ii],'pres_interpol[ii]','rd1[ii]','rd2[ii]','sog_interpol[ii]',temp_cav_interpol[jj],'temp_interpol[ii]','wd_corr_interpol[ii]','wd_uncorr_interpol[ii]','ws_corr_interpol[ii]','ws_uncorr_interpol[ii]'))
			nom_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (garmin_time_interpol[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_garmin_interpol[ii],amb[jj],ch4[jj],ch4_cal[jj],'co[ii]',co2[jj],co2_cal[jj],'cod[ii]',0,gasp[jj],h2o[jj],0,0,lat_garmin_interpol[ii],lon_garmin_interpol[ii],0,'rd1[ii]','rd2[ii]',0,temp_cav[jj],0,0,0,0,0))
			start_Garmin = ii

nom_interp.close()




