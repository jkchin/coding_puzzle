Programming Challenge (Optional)

Calculate the detour distance between two different rides. Given four latitude
/ longitude pairs, where driver one is traveling from point A to point B and
driver two is traveling from point C to point D, write a function (in your
language of choice) to calculate the shorter of the detour distances the
drivers would need to take to pick-up and drop-off the other driver.

Usage Note:
Calculates the lesser of the detours distances between two
different rides and returns the results in km.

dist.py pt_a pt_b pt_c pt_d

Arguments:
    Coordinates expressed in latitude and longitude comma-separated signed
    decimal degree pairs: <lat>,<log>
    
    pt_a -- Starting coordinates of ride A
    pt_b -- Destination coordinates of ride A
    pt_c -- Starting coordinates of ride B
    pt_d -- Destination coordinates of ride B


Example:
./dist.py 0.0,0.0 1.0,1.0 -1.0,-1.0 -2.0,-2.0
