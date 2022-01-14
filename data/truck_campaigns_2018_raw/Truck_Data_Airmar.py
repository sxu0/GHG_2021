# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:38:05 2018

@author: Sébastien
"""

# dans la premiere version, les donnees picarro etaient interpolees toutes les secondes. Cette fonction est retire ici. 


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
import pandas as pd


# Convert the gps_time strings into real date&times
def convert_to_time(x):
    return datetime.strptime(x,"%Y-%m-%d %H:%M:%S.%f")

def convert_to_time_meteo(x):
    return datetime.strptime(x,"%Y/%m/%d %H:%M:%S")


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





# 2018-11-20
jour_mesure = '2018-11-20'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181120/' 			
fichier_Picarro='CFADS59-20181120-Data.dat'
Picarro_shift = timedelta(seconds=42)
fichier_airmar='Airmar_2018-11-20.csv'
fichier_interp='sync_data_2018-11-20.csv' 

'''
# 2018-11-22
jour_mesure = '2018-11-22'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181122/' 			
fichier_Picarro='CFADS59-20181122-Data.dat'
Picarro_shift = timedelta(seconds=42)
fichier_airmar='Airmar_2018-11-22.csv'
fichier_interp='sync_data_2018-11-22.csv' 
'''
'''
# 2018-11-29
jour_mesure = '2018-11-29'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181129/' 			
fichier_Picarro='CFADS59-20181129-Data.dat'
Picarro_shift = timedelta(seconds=42)
fichier_airmar='Airmar_2018-11-29.csv'
fichier_interp='sync_data_2018-11-29.csv' 
'''
'''
# 2018-12-04
jour_mesure = '2018-12-04'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181204/' 			
fichier_Picarro='CFADS59-20181204-Data.dat'
Picarro_shift = timedelta(seconds=42)
fichier_airmar='Airmar_2018-12-04.csv'
fichier_interp='sync_data_2018-12-04.csv' 
'''
'''
# 2018-12-07
jour_mesure = '2018-12-07'
path_Picarro='/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Picarro/20181207/' 			
fichier_Picarro='CFADS59-20181207-Data.dat'
Picarro_shift = timedelta(seconds=42)
fichier_airmar='Airmar_2018-12-07.csv'
fichier_interp='sync_data_2018-12-07.csv' 
'''


path_results = '/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Sync_data/' + jour_mesure + '/Data_files/'


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
filename_airmar = path_results + fichier_airmar 	# chemin du fichier a traiter

df = pd.read_csv(filename_airmar)
df["Airmar_time"] = df["Airmar_time"].apply(convert_to_time)
Airmar_time = df["Airmar_time"]

df.set_index('Airmar_time',inplace=True)
alt, cog, hdop, heading, lat, lon, pressure, sog, temp, wd_corr, wd_uncorr, ws_corr, ws_uncorr = df['alt'], df['cog'], df['hdop'], df['heading'], df['lat'], df['lon'], df['pressure'], df['sog'], df['temp'], df['wd_corr'], df['wd_uncorr'], df['ws_corr'], df['ws_uncorr']



###########################################
# Creation fichier data-sync
###########################################

try:
	os.makedirs(path_results)
except OSError:
	pass

os.chdir(path_results)


if os.path.exists(fichier_interp):		# if file exists delete 
  os.remove(fichier_interp)

nom_interp = open(fichier_interp, "w")

nom_interp.write('gps_time,alt,amb,ch4,ch4d,co,co2,co2d,cod,cog,gasp,h2o,hdop,heading,lat,lon,pressure,rd1,rd2,sog,t,temp,wd_corr,wd_uncorr,ws_corr,ws_uncorr\n')

start = 0

for jj in range(0,len(Picarro_time)):
	print Picarro_time[jj].strftime("%Y-%m-%d %H:%M:%S.%f")
	for ii in range(start,len(Airmar_time)):
		#print 's'
		if Picarro_time[jj].day == Airmar_time[ii].day and Picarro_time[jj].hour == Airmar_time[ii].hour and Picarro_time[jj].minute == Airmar_time[ii].minute and Picarro_time[jj].second == Airmar_time[ii].second:
			print 'ok'
			nom_interp.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (Airmar_time[ii].strftime("%Y-%m-%d %H:%M:%S.%f"),alt[ii],amb[jj],ch4[jj],ch4_cal[jj],'co[ii]',co2[jj],co2_cal[jj],'cod[ii]',cog[ii],gasp[jj],h2o[jj],hdop[ii],heading[ii],lat[ii],lon[ii],pressure[ii],'rd1[ii]','rd2[ii]',sog[ii],temp_cav[jj],temp[ii],wd_corr[ii],wd_uncorr[ii],ws_corr[ii],ws_uncorr[ii]))
	
			start = ii
			break
nom_interp.close()




