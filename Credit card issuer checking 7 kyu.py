# Credit card issuer checking
# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.
# Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. 
# If the number cannot be matched then the function should return the string Unknown.

def get_issuer(number):
    number = str(number)
    if len(number) == 15 and number[0:2] == "34" or number[0:2] == "37":
        return "AMEX"
    elif len(number) == 16 and number[0:4] == "6011":
        return "Discover"
    elif (len(number) == 16 and number[0:2] == "51" or number[0:2] == "52" or number[0:2] == "53" 
          or number[0:2] == "54" or number[0:2] == "55") :
        return "Mastercard"
    elif len(number) == 13 and number[0] == "4" or len(number) == 16 and number[0] == "4":
        return "VISA"
    else:
        return "Unknown"
         
         
# def get_issuer(number):
#     s = str(number)
#     return ("AMEX"       if len(s)==15 and s[:2] in ("34","37") else
#             "Discover"   if len(s)==16 and s.startswith("6011") else
#             "Mastercard" if len(s)==16 and s[0]=="5" and s[1] in "12345" else
#             "VISA"       if len(s) in [13,16] and s[0]=='4' else
#             "Unknown")
