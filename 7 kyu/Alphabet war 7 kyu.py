# Alphabet war
# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. 
# When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:

#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims. Sum up each side's letters' power values to determine which side wins.

# Example
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!

def alphabet_war(fight):
    fighter_dict = {"w":-4, "p":-3, "b":-2, "s":-1,"m":4, "q":3, "d":2, "z":1}
    result = 0
    for ch in fight:
        if ch in fighter_dict:
            result += fighter_dict.get(ch)
    if result > 0:
        return "Right side wins!"
    elif result < 0:
        return "Left side wins!"
    else:
        return "Let's fight again!"

# def alphabet_war(fight):
#     d = {'w':4,'p':3,'b':2,'s':1,
#          'm':-4,'q':-3,'d':-2,'z':-1}
#     r = sum(d[c] for c in fight if c in d)
    
#     return {r==0:"Let's fight again!",
#             r>0:"Left side wins!",
#             r<0:"Right side wins!"
#             }[True]
