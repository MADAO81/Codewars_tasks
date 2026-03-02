# FIRE and FURY
# The President's phone is broken
# He is not very happy.

# The only letters still working are uppercase E, F, I, R, U, Y.

# An angry tweet is sent to the department responsible for presidential phone maintenance.

# Kata Task
# Decipher the tweet by looking for words with known meanings.

# FIRE = "You are fired!"
# FURY = "I am furious."
# If no known words are found, or unexpected letters are encountered, then it must be a "Fake tweet."

# Notes
# The tweet reads left-to-right.
# Any letters not spelling words FIRE or FURY are just ignored
# If multiple of the same words are found in a row then plural rules apply -
# FIRE x 1 = "You are fired!"
# FIRE x 2 = "You and you are fired!"
# FIRE x 3 = "You and you and you are fired!"
# etc...
# FURY x 1 = "I am furious."
# FURY x 2 = "I am really furious."
# FURY x 3 = "I am really really furious."
# etc...
# Examples
# ex1. FURYYYFIREYYFIRE = "I am furious. You and you are fired!"
# ex2. FIREYYFURYYFURYYFURRYFIRE = "You are fired! I am really furious. You are fired!"
# ex3. FYRYFIRUFIRUFURE = "Fake tweet."

import re
from itertools import groupby

CONFIG = {'FURY':   " really",
          'FIRE':   " and you",
          'FAKE':   "Fake tweet.",
          'FURY_f': "I am{} furious.",
          'FIRE_f': "You{} are fired!"}

def fire_and_fury(tweet):
    if re.findall(r'[^FURYIE]', tweet): return CONFIG['FAKE']
    lst = []
    for k,g in groupby(re.findall(r'FURY|FIRE', tweet)):
        lst += [ CONFIG[k+"_f"].format(CONFIG[k] * (len(list(g)) - 1)) ]
    return ' '.join(lst) or CONFIG['FAKE']
