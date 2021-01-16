import math
import unittest



altitude = 1000
velocity = 40
fuel = 25
strength = 4
gravity = 1.622
velocity_change_per_thrust = 4
atmosphere_lower = -1
atmosphere_upper = -1


def get_status():
    """
    the get_status function
    returns a string representation of the current status
    """
    global altitude
    global velocity
    global fuel
    global strength

    return "Alt = " + '{0:.2f}'.format(altitude) + " Vel = " + '{0:.2f}'.format(velocity) + " Fuel = " + '{0:.0f}'.format(fuel) + " Str = " + '{0:.0f}'.format(strength)


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
    global altitude
    global atmosphere_lower
    global atmosphere_upper
    global strength
    global gravity
    global velocity

    velocity = velocity + gravity
    altitude = altitude - velocity
    if altitude < 0:
        altitude=0

    if altitude < atmosphere_upper and altitude > atmosphere_lower:
        strength = strength -1


def has_crashed():
    return(altitude <= 0 and velocity >strength)

def has_safely_landed():
    return(altitude <= 0 and velocity<=strength)


def reset_lander(a,v,f):
    global altitude
    global velocity
    global fuel

    altitude = a
    velocity = v
    fuel = f


def human_controller():


    print (get_status())
    thrust = input("How much thrust this round? ")
    return (int(thrust))


def simulate_landing(player):
    while not(has_crashed()) and not(has_safely_landed()):
        thrust(player())
        update_onesecond()
        if has_crashed():
            return ("Oh no the lander has crashed! Better skill next time!")
        elif has_safely_landed():
            return ("Great success! You should apply for an internship with NASA!")



def reset_world(g,s,a_l,a_u):
    global gravity
    global strength
    global atmosphere_lower
    global atmosphere_upper

    gravity = g
    strength = s
    atmosphere_lower = a_l
    atmosphere_upper = a_u





def has_disintegrated():
    global strength
    return(strength <= 0)


if __name__ == "__main__":
    simulate_landing(human_controller)



def smart_controller():

    local_altitude = altitude
    local_velocity = velocity

    count = 0
    while local_altitude > 0:
        local_velocity = local_velocity + gravity
        local_altitude = local_altitude - local_velocity
        count = count + 1

    max_vel_charge = velocity_change_per_thrust * min(fuel,strength)

    if max_vel_charge == 0:
        return 0

    rstop = math.ceil(local_velocity/max_vel_charge)
    if rstop >= count:
        number = local_velocity / (rstop * velocity_change_per_thrust)
        for n in range(1,int(number)+1):
            n = min(strength, fuel, int(n))
            v = velocity - int(n) * velocity_change_per_thrust
            if int(v) == 0:
                return n
            return number
        else:
            return 0
