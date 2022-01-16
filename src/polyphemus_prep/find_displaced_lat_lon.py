# -*- coding: utf-8 -*-

"""
find.displaced_lat_lon.py

Finds new coordinates given starting coordinates and displacement.

Formulae:
φ2 = asin( sin φ1 ⋅ cos δ + cos φ1 ⋅ sin δ ⋅ cos θ )
λ2 = λ1 + atan2( sin θ ⋅ sin δ ⋅ cos φ1, cos δ - sin φ1 ⋅ sin φ2 )
where φ is latitude, λ is longitude, θ is bearing (clockwise from north),
    δ is angular distance d/R (d being distance travelled, R earth's radius)

Reference: https://www.movable-type.co.uk/scripts/latlong.html
"""


from math import asin, atan, atan2, cos, degrees, pi, radians, sin

RADIUS_EARTH = 6371000  # m


def find_displaced_lat_lon(lat_0, lon_0, delta_x, delta_y):
    """Computes new coordinates given old coordinates and displacement.

    Args:
        lat_0 (float): Starting latitude, in degrees.
        lon_0 (float): Starting longitude, in degrees.
        delta_x (float): East-west displacement, in m. East is positive.
        delta_y (float): North-south displacement, in m. North is positive.

    Returns:
        lat_1: Resulting latitude, in degrees.
        lon_1: Resulting longitude, in degrees.
    """

    dist = (delta_x ** 2 + delta_y ** 2) ** 0.5
    theta = (pi / 2 - atan(delta_y / delta_x)) % (2 * pi)
    lat_1 = degrees(
        asin(
            sin(radians(lat_0)) * cos(dist / RADIUS_EARTH)
            + cos(radians(lat_0)) * sin(dist / RADIUS_EARTH) * cos(theta)
        )
    )
    lon_1 = degrees(
        radians(lon_0)
        + atan2(
            sin(theta) * sin(dist / RADIUS_EARTH) * cos(radians(lat_0)),
            cos(dist / RADIUS_EARTH) - sin(radians(lat_0)) * sin(radians(lat_1)),
        )
    )
    return lat_1, lon_1


lat, lon = find_displaced_lat_lon(43.81753, -79.37802, 199, 44)
print("lat:\t" + str(lat))
print("lon:\t" + str(lon))
