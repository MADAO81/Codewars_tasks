# This program tests the life of an evaporator containing a gas.

# We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) 
# and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. All numbers are strictly positive.

# The program reports the nth day (as an integer) on which the evaporator will be out of use.

# Example:
# evaporator(10, 10, 5) -> 29

def evaporator(content, evap_per_day, threshold):
    count = 0
    residue_substance = threshold/100*content
    while content > residue_substance :
        content -= evap_per_day/100*content
        count +=1
    return count
