# Cyrillic letters
# Cyrillic letters, used in languages like Russian and Ukrainian, have different unicode values than Latin letters.
# 2 of those cyrillic letters include а and у which, if you copy these 2, are not the same as the latin a and y
# Task
# Your task is to write a function that returns whether a given string (or char) 
# is a Cyrillic letter in the Cyrillic Unicode Block.

# The string (or char) will always be a single letter.

# def is_cyrillic(letter):
#     alphabet_cyr = set('''ЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийк
# лмнопрстуфхцчшщъыьэюяѐёђѓєѕіїјљњћќѝўџѠѡѢѣѤѥѦѧѨѩѪѫѬѭѮѯѰѱѲѳѴѵѶѷѸѹѺѻѼ
# ѽѾѿҀҁ҂◌҃◌҄◌҅◌҆◌҇◌҈◌҉ҊҋҌҍҎҏҐґҒғҔҕҖҗҘҙҚқҜҝҞҟҠҡҢңҤҥҦҧҨҩҪҫҬҭҮүҰұҲҳҴҵҶҷҸҹҺһҼ
# ҽҾҿӀӁӂӃӄӅӆӇӈӉӊӋӌӍӎӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹӺӻӼӽӾӿ''')
#     return not alphabet_cyr.isdisjoint(letter.lower())   # <- Hajime!
    
    
def is_cyrillic(letter):
    return 1024 <= ord(letter) <= 1279
