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

'''
# 2018-11-20
jour_mesure = '2018-11-20'
path_airmar='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 				
fichier_airmar='Nov_20_2018.LOG'
fichier_interp='Airmar_2018-11-20.csv' 
'''
'''
# 2018-11-22
jour_mesure = '2018-11-22'
path_airmar='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 				
fichier_airmar='Nov_22_2018.LOG'
fichier_interp='Airmar_2018-11-22.csv' 
'''

# 2018-11-28
jour_mesure = '2018-11-28'
path_airmar='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 				
fichier_airmar='Nov_28_2018.LOG'
fichier_interp='Airmar_2018-11-28.csv' 

'''
# 2018-11-29
jour_mesure = '2018-11-29'
path_airmar='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 				
fichier_airmar='Nov_29_2018.LOG'
fichier_interp='Airmar_2018-11-29.csv' 
'''
'''
# 2018-12-04
jour_mesure = '2018-12-04'
path_airmar='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 				
fichier_airmar='Dec_04_2018.LOG'
fichier_interp='Airmar_2018-12-04.csv'
'''
'''
# 2018-12-07
jour_mesure = '2018-12-07'
path_airmar='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/' 				
fichier_airmar='Dec_07_2018_4119942_0183.LOG'
fichier_interp='Airmar_2018-12-07.csv' 
'''




######################################
## Airmar
############################################

print 'AIRMAR'
filename_airmar = path_airmar + fichier_airmar 	# chemin du fichier a traiter

fil=open(filename_airmar, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

meteo_time, wind_speed, wind_direction, temperature, Relative_Humidity, Pressure = [], [], [], [], [], []

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
		if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ >= 12 or (int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) <= 12):
			time_GPRMC.append( (datetime(year_,month_,day_,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )		
		if int( (':'.join((','.join(donnees[0].split())).split(',')[0].split())).split(':')[0] ) >= 12 and hour_ <= 12:
			time_GPRMC.append( (datetime(year_,month_,day_ + 1,hour_,minute_,second_,millisec_) - datetime(1970,1,1)).total_seconds() )

		cog.append( float( (','.join(donnees[ll].split())).split(',')[10] ) )
		sog.append( float( (','.join(donnees[ll].split())).split(',')[9] ) * 1.852 )	# to convert knots to km/h


print(t[0], datetime.fromtimestamp(int(t_epoch[0])) )

time_interp, time_interpol = [], []

for ii in range(0,int(time_GPZDA[-1]) - int(time_GPZDA[0]) + 1):
	time_interp.append(int(time_GPZDA[0]) + ii)
	#time_interpol.append( datetime.fromtimestamp(int(t_epoch[0]) + ii) + timedelta(seconds=4*3600) )	#/!\ 4 in summer and 5 in winter (changement d heure)


#### Interpolation of all data on time_interp

lat_interp, lon_interp, alt_interp, hdop_interp = [], [], [], []
pressure_interp, temp_interp, RH_interp, dew_point_interp, wd_corr_interp, ws_corr_interp = [], [], [], [], [], []
wd_uncorr_interp, ws_uncorr_interp = [], []
pres_interp = []
hdg_interp = []
sog_interp, cog_interp = [], []
time = []

start_hdg, start_wimwv = 0, 0

print 'start'

for ii in range(0,len(time_interp)):
	print datetime.fromtimestamp(int(time_interp[ii])).strftime("%Y-%m-%d %H:%M:%S.%f")
	for jj in range(start_hdg, len(time_HCHDG)):
		if round(time_interp[ii]) == round(time_HCHDG[jj]):
			for kk in range(start_wimwv, len(time_WIMWV)):
				if round(time_interp[ii]) == round(time_WIMWV[kk]):				
					lat_interp.append(np.interp(time_interp[ii],time_GPGGA,lat))
					lon_interp.append(np.interp(time_interp[ii],time_GPGGA,lon))	
					alt_interp.append(np.interp(time_interp[ii],time_GPGGA,alt))
					hdop_interp.append(np.interp(time_interp[ii],time_GPGGA,hdop))

					pressure_interp.append(np.interp(time_interp[ii],time_WIMDA,pressure))
					temp_interp.append(np.interp(time_interp[ii],time_WIMDA,temp))
					RH_interp.append(np.interp(time_interp[ii],time_WIMDA,RH))
					dew_point_interp.append(np.interp(time_interp[ii],time_WIMDA,dew_point))
					wd_corr_interp.append(np.interp(time_interp[ii],time_WIMDA,wd_corr))
					ws_corr_interp.append(np.interp(time_interp[ii],time_WIMDA,ws_corr))

					pres_interp.append(np.interp(time_interp[ii],time_YXXDR,pres))

					sog_interp.append(np.interp(time_interp[ii],time_GPRMC,sog))
					cog_interp.append(np.interp(time_interp[ii],time_GPRMC,cog))

					time.append(np.interp(time_interp[ii],time_GPZDA,t_epoch))

					hdg_interp.append(hdg[jj])

					wd_uncorr_interp.append(wd_uncorr[kk])
					ws_uncorr_interp.append(ws_uncorr[kk])	
					
					start_wimwv = kk

					break	
			start_hdg = jj
			break
	


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

nom_interp.write('Airmar_time,alt,cog,hdop,heading,lat,lon,pressure,sog,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')


for ii in range(1,len(time)):
	'''
	print time_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f")

	nom_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (time_interp[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt_interp[ii],cog_interp[ii],hdop_interp[ii],hdg_interp[ii],lat_interp[ii],lon_interp[ii],pres_interp[ii],sog_interp[ii],temp_interp[ii],wd_corr_interp[ii],wd_uncorr_interp[ii],ws_corr_interp[ii],ws_uncorr_interp[ii]))
	'''
	#print datetime.fromtimestamp(int(time[ii])).strftime("%Y-%m-%d %H:%M:%S.%f")
	if (datetime.fromtimestamp(int(time[ii]))+ timedelta(seconds=4*3600)).strftime("%Y-%m-%d %H:%M:%S.%f") != (datetime.fromtimestamp(int(time[ii-1]))+ timedelta(seconds=4*3600)).strftime("%Y-%m-%d %H:%M:%S.%f"):		# avoid having twice the same hour
		nom_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % ((datetime.fromtimestamp(int(time[ii]))+ timedelta(seconds=5*3600)).strftime("%Y-%m-%d %H:%M:%S.%f"),alt_interp[ii],cog_interp[ii],hdop_interp[ii],hdg_interp[ii],lat_interp[ii],lon_interp[ii],pres_interp[ii],sog_interp[ii],temp_interp[ii],wd_corr_interp[ii],wd_uncorr_interp[ii],ws_corr_interp[ii],ws_uncorr_interp[ii]))	#/!\ 4 in summer and 5 in winter (changement d heure)
	
nom_interp.close()




