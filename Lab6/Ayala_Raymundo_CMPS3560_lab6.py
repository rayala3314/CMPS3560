import sys
#Lab 6 - Monotonic Inference in Python
# Modified by: Raymundo Ayala 10/27/2021

#Water an output variable
#0L to 2l
#0.0 - 0.4 --> none
#1 - 2 --> Bottle
#2 ---> alot

#Temperature(input var)
#32F to 120F

#Distance(input var)
#0.25 to 20 miles
#or 0.4km to 32km


#Water sets (three linguistic values)
waterNone = ((1.0,0.0), (0.75,0.1), (0.50,0.2), (0.25,0.3), (0.0,0.4))
waterBottle = ((0.0,0.2), (0.5,0.5), (1.0,1.0), (0.5,1.5), (0.0,2.0))
waterAlot = ((0.0,1.00), (0.25, 1.25), (0.5,1.50), (0.75,1.75), (1.0,2.00))

#Task 1 - Create remaining variables
#Temperature sets (two linguistic values)
#32F to 120F
tempModerate = ((0.0,32), (0.25,42), (0.5,52), (0.75,62), (1.0,72),)
tempHot = ((0.0, 62), (0.25, 82), (0.50, 92), (0.75, 112), (1.0, 120))

#Distance sets (three linguistic values)
#0.25miles - 20miles
#0.4km - 32km
distanceShort = ((1.00,0.4), (0.75,3.4), (0.50,6.4), (0.25,9.4), (0.0,12.4))
distanceMedium = ((0.0,8.0), (0.5,12), (1.0,16), (0.5,20), (0.0, 24))
distanceLong = ((0.0,16), (0.25,20), (0.5,24), (0.75,28), (1.00,32))

#Task 2 - Implement Fuzzy Membershiop
#Modify to get nearest Val

def membership(inputVal, fuzzySet):
    nearestCrisp = sys.float_info.max
    retVal = 0.0
    for p in fuzzySet:
        fuzzyVal, crisp = p 
        diff = abs(inputVal - crisp)
        if diff < nearestCrisp:
            nearestCrisp = diff
            retVal = crisp
    for p in fuzzySet:
        fuzzyVal, crisp = p 
        if retVal == crisp:
            return fuzzyVal

        

#Task 3 - Inverse Membership Functions
#Should return the corresponding crisp Val
#matches nearest fuzzyVal and resturns the crisp val
def inverseMembership(inputVal, fuzzySet):
    nearestFuzzval = sys.float_info.max
    retVal = 0.0
    for p in fuzzySet:
        fuzzyVal, crisp = p
        diff = abs(inputVal - fuzzyVal)
        if diff < nearestFuzzval:
            nearestFuzzval = diff
            retVal = fuzzyVal
    for p in fuzzySet:
        fuzzyVal, crisp = p
        if retVal == fuzzyVal:
            return crisp
            break
#Test Case - Rule 1:
#IF distance is long
#OR Temp is hot
#Then water is alot
#User traveling 3km and it is 80F outside
km = 30
temp = 80
fuzzyDistance = membership(km, distanceLong)
fuzzyTemp = membership(temp, tempHot)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, waterAlot)
print(f"The user walked: {km} km and it is {temp} F. Fuzzy system recommends {crispOutput} bottles of water")

#Test Case - Rule 2:
#IF distance is medium
#OR Temp is moderate
#Then water is bottle
km = 16
temp = 92
fuzzyDistance = membership(km, distanceShort)
fuzzyTemp = membership(temp, tempModerate)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, waterBottle)
print(f"The user walked: {km} km and it is {temp} F. Fuzzy system recommends {crispOutput} bottles of water")



#Test Case - Rule 3
#IF distance is short
#AND Temp is moderate
#Then water is none
km = 2.75
temp = 75
fuzzyDistance = membership(km, distanceShort)
fuzzyTemp = membership(temp, tempModerate)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, waterNone)
print(f"The user walked: {km} km and it is {temp} F. Fuzzy system recommends {crispOutput} bottles of water")
