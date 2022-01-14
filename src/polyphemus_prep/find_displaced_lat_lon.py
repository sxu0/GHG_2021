# -*- coding: utf-8 -*-

from math import *

'''
formulae:
φ2 = asin( sin φ1 ⋅ cos δ + cos φ1 ⋅ sin δ ⋅ cos θ )
λ2 = λ1 + atan2( sin θ ⋅ sin δ ⋅ cos φ1, cos δ − sin φ1 ⋅ sin φ2 )
where φ is latitude, λ is longitude, θ is bearing (clockwise from north), δ is angular distance d/R (d being distance travelled, R earth’s radius)

source: https://www.movable-type.co.uk/scripts/latlong.html
'''

def find_displaced_lat_lon(lat0, lon0, deltax, deltay):
    '''
    takes lat/lon input in degrees, deltax/deltay input in metres
    '''
    R = 6371000     # m
    d = ( deltax ** 2 + deltay ** 2 ) ** 0.5
    theta = (pi/2 - atan(deltay/deltax)) % (2*pi)
    lat1 = degrees( asin( sin( radians(lat0) ) * cos(d/R) + cos( radians(lat0) ) * sin(d/R) * cos(theta) ) )
    lon1 = degrees( radians(lon0) + atan2( sin(theta) * sin(d/R) * cos( radians(lat0) ), cos(d/R) - sin( radians(lat0) ) * sin( radians(lat1) ) ) )
    return lat1, lon1


lat, lon = find_displaced_lat_lon(43.81753, -79.37802, 199, 44)
print("lat:\t" + str(lat))
print("lon:\t" + str(lon))
