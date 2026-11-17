# Variables, arithmatic, and importing modules

#demo 1 - variables and assignment
import math


def demo1_variables():
    Can_Volume = 0.355     #in liters
    bottle_volume = 2.0

    cansperpack = 6
    packVolume = cansperpack * Can_Volume
    print("six pack volume:", packVolume, "liters")
    print("two litter bottle:", bottle_volume, "liters")

demo1_variables()

lives = 3
print("lives at start:" , lives)

# DEMO 3 - Operators and precedence (11.2)
print("\n\nOperators and precidence")
def demo3_operators():
    a = 10
    b = 4
    print("a + b / 2 =", a + b / 2)     #12.0
    print("(a + b) / 2 =", (a + b) / 2) #7.0
    print("10 - 2 - 3 =", 10 - 2 - 3)   #5
    print("7 + 4.0 =", 7 + 4.0)         #11.0

    # Powers
    print("10 * 2 ** 3 =", 10 * 2 ** 3) #80 (** before *)
    print("2 ** 3 ** 2 =", 2 ** 3 ** 2)     #512 (** right to left)

    #Compound interest: balance * (1 + rate/100) ** years
    balance = 1000
    rate = 5.0
    years = 10
    future = balance * (1 + rate/100) ** 10
    print("future value:", future)

demo3_operators()


#Demo 4 - Floor division and modulus
print("\n\nFloor division & modulus")
def demo4_floor_and_mod():
    print("17 /5 =", 17 / 5)       #3.4
    print("17 // 5 =", 17 // 5)     #3
    print("17 % 5 =", 17 % 5)       #2

    screenMinutes = 437
    MPH = 60
    hours = screenMinutes // MPH
    minutes = screenMinutes % MPH
    print(hours, "hours and", minutes, "minutes")


    import math

    radius = math.sqrt(50)
    print(round(math.pi * radius ** 2, 2))

demo4_floor_and_mod()