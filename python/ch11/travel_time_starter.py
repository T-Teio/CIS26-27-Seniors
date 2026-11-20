##
#  Section 11.7 Worked Example: Computing Travel Time
#  A robot drives along a road (fast), then cuts straight across rocky
#  terrain (slow) to reach an item. Compute the total travel time.
#
#  HAND CALCULATION (dx = 10 km, dy = 3 km, l1 = 6 km, s1 = 5 km/h, s2 = 2 km/h):
#    Segment 1 time   = 6/5=1.2 hours = 1 hour and 12 minutes
#    Segment 2 length = 4**2 + 3**2 = c**2, c = 5
#    Segment 2 time   = 5/2=2.5 hours = 2 hours and 30 minutes
#    Total time       = 3 hours and 42 minutes
#
from math import sqrt
# Short hand-calculation names (dx, s1...) become DESCRIPTIVE names in code.
dx = input("What is the distance of the first road?")
dy = input("What is the distance of the second road?")
l1 = input("How much of the first road do you drive?")
s1 = input("How fast do you go on the first road? (in km/h)")
s2 = input("How fast do you go on the second road? (in km/h)")

l1Time = l1/s1
l2 = sqrt((dx-l1)**2)
l2Time = l2/s2

print("The total time is", l1Time+l2Time, "hours.")


