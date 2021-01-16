import math
import unittest



altitude = 1000
velocity = 40
fuel = 25
strength = 4
gravity = 1.622
velocity_change_per_thrust = 4


def get_status():
    global altitude
    global velocity
    global fuel
    global strength

    print('Alt = {0:.2f} Vel = {0:.2f} Fuel = {0:.2f} Str = {0:.2f}'.format(altitude,velocity,fuel,strength))


def thrust(number):
    global fuel
    global velocity


    if(type(number) == int or type(number) == float):
        number = int(number)
        if number > strength:
            number = strength
        if number > fuel:
            number = fuel
        fuel = fuel - number
        velocity = velocity - number * velocity_change_per_thrust


def update_onesecond():
    global velocity
    global altitude
    global gravity

    velocity = velocity + gravity
    altitude = altitude - velocity
    if altitude < 0:
        altitude=0


def has_crashed():
    return(altitude <= 0 and velocity >strength)

def has_safely_landed():
    return(altitude <= 0 and velocity<=strength)
