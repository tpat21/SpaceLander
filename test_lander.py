import lander as L



def close(a, b, e=0.000001):
    return abs(a-b) < e

def test_lander_part1():
    L.thrust(1)
    assert close(L.velocity, 36) and close(L.fuel, 24), "thrust"

    L.thrust(1.7)
    assert close(L.velocity, 32) and close(L.fuel, 23), "thrust"

    L.thrust(6)
    assert close(L.velocity, 16) and close(L.fuel, 19), "thrust"

    L.fuel = 0
    L.thrust(1)
    assert close(L.velocity, 16) and close(L.fuel, 0), "thrust"

    L.update_onesecond()
    assert close(L.velocity, 17.622) and close(L.fuel, 0), "update_onesecond"

    L.altitude = 1
    L.update_onesecond()
    assert close(L.altitude, 0), "update_onesecond"

    L.altitude = 0
    assert L.has_crashed(), "has_crashed"

    L.velocity = 1
    assert L.has_safely_landed(), "has_safely_landed"

    assert L.get_status() == "Alt = 0.00 Vel = 1.00 Fuel = 0 Str = 4", \
           "get_status"

    print("test_lander part 1 SUCCESS!")

test_lander_part1()
