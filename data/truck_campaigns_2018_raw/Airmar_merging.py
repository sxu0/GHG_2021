#!/usr/bin/env python


import os
import shutil
import datetime
import numpy as np


import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy import stats
import matplotlib.colors as colors	# To color the plumes
import collections 	# To preserve order in dct
import matplotlib.dates as md


os.chdir('/home/sebastien/Documents/Mobile_measurements/Data/Truck_campaigns_2018/Airmar/')

name = "Nov_28_2018.LOG"

try:
    os.remove(name)
except OSError:
    pass

nom = open(name,"a")		# creation et appending ('a') du fichier decoupe


filename = 'Nov_28_2018_4119942_0183.LOG' 	# chemin du fichier a traiter
fil=open(filename, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

print nbl

for ii in range(0,nbl):
	if (','.join(donnees[ii].split())).split(',')[0] != 'C' and (','.join(donnees[ii].split())).split(',')[0] != '$' and (','.join(donnees[ii].split())).split(',')[0] != 'Al' and (','.join(donnees[ii].split())).split(',')[0] != '' and (','.join(donnees[ii].split())).split(',')[0] != 'Co' and (','.join(donnees[ii].split())).split(',')[0] != 'A':
		d = (','.join(donnees[ii].split())).split(',')[0]
		hour = int( (':'.join(d.split())).split(':')[0] )
		minute = int( (':'.join(d.split())).split(':')[1] )
		seconde = float( (':'.join(d.split())).split(':')[2] )
		if (hour == 20 and minute == 36 and seconde == 53.594):
			continue
		if (hour == 20 and minute == 37 and seconde == 56.180):
			continue
		if (hour == 20 and minute == 50 and seconde == 23.358):
			continue
		else:
			nom.write("%s\n" % (donnees[ii]) )


filename = 'Nov_29_2018_4119942_0183.LOG' 	# chemin du fichier a traiter
fil=open(filename, mode='r') 					# ouverture du fichier
donnees = fil.readlines()						# lecture du fichier
nbl=len(donnees)							# nbl est le nombre de ligne du fichier

print nbl

for ii in range(0,nbl):
	if (','.join(donnees[ii].split())).split(',')[0] != 'C' and (','.join(donnees[ii].split())).split(',')[0] != '$' and (','.join(donnees[ii].split())).split(',')[0] != 'Al' and (','.join(donnees[ii].split())).split(',')[0] != '' and (','.join(donnees[ii].split())).split(',')[0] != 'Co' and (','.join(donnees[ii].split())).split(',')[0] != 'A':
		d = (','.join(donnees[ii].split())).split(',')[0]
		hour = int( (':'.join(d.split())).split(':')[0] )
		minute = int( (':'.join(d.split())).split(':')[1] )
		sec_ = float( (':'.join(d.split())).split(':')[2] )
		seconde = int(sec_)
		if hour < 3:
			nom.write("%s\n" % (donnees[ii]) )

nom.close()

















