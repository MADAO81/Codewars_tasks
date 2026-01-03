# https://www.codewars.com/kata/541629460b198da04e000bb9/train/python


# def last(a, *b):
#     if(b): return b[-1]
#     try: return a[-1]
#     except: return a


def last(*arr):
    try:
        if len(arr) == 1 :
            arr = list(arr[0])
            print(arr)
            return arr[-1]

        else:
            return arr[-1]
    
    except:
        return arr[-1]
