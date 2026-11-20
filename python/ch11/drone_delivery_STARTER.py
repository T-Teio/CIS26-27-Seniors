##
#  
#  Plans drone delivery trips from a warehouse to a customer and reports
#  the straight-line distance, number of trips, total distance flown,
#  and total time (flying + loading).
#
# Part A - HAND CALCULATION (3 km east, )
#  segment 1 distance = 3km
#  segment 2 distance = 4km
#  total distance = 3 + 4 = 7km
#  time per trip = 7 / 40 = 0.175 hours
#  trips = 7 / 2 = 3.5 round up to 4
#  total distance flown = 4 * 7 = 28km
#  loading time = 4 * 0.5 = 2 minutes - 0.033 hours
#  total time = 4 * 0.175 = 0.7 = 42 minutes
#
#  Import style: "import math" - writing math.sqrt and math.ceil makes it
#  clear to any reader which module each function comes from.
#
import math

segment1Distance = float(input("How far east is the customer? (in km)"))
segment2Distance = float(input("How far north is the customer? (in km)"))
totalDistance = segment1Distance + segment2Distance
speed = float(input("How fast does the drone fly? (in km/h)"))
timePerTrip = totalDistance / speed
numPackages = float(input("How many packages are being delivered?"))
PACKAGESPERTRIP = 2
numTrips = math.ceil(numPackages / PACKAGESPERTRIP)
totalDistanceFlown = numTrips * totalDistance
loadingTime = numTrips * 0.5 / 60  # Convert minutes to hours
totalTime = numTrips * timePerTrip + loadingTime

print("the total delivery time is", totalTime, "hours.")
