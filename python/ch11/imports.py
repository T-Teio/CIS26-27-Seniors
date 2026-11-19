# -------------------------------------------------------
# Section 11.3 Practice: Other ways to import modules
# Demonstrates the different ways to bring math functions into a program
# -------------------------------------------------------

#Style 1: Import specific functions by name

from math import sqrt, ceil, floor
print("Style 1: from math import sqrt, ceil, floor")
print("sqrt(81) = ", sqrt(81))
print("ceil(4.2) = ", ceil(4.2))
print("floor(4.8) = ", floor(4.8))

# --------------------------------------------------------
#Style 2: Import the whole module and use module.function
#--------------------------------------------------------
import math
print("\nStyle 2: import math")
print("math.sqrt(81) = ", math.sqrt(81))
print("math.pi = ", math.pi)
print("math.pow(2, 5) = ", math.pow(2, 5))

#--------------------------------------------------------
#Style 3: Import everything with * (works but use with caution)
#--------------------------------------------------------
from math import *
print("\nStyle 3: from math import *")
print("cos(0) - ", cos(0))
e = 5

print(" e = ", e)