# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

# def check_exam(arr1, arr2):
#     return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

def check_exam(arr1,arr2):
    total = 0
    if len(arr1)!=0 and len(arr2)!=0:
        if len(arr1)==len(arr2):
            while len(arr1)>0 and len(arr2)>0:
                correct = arr1.pop(0)
                answer = arr2.pop(0)
                if answer == "":
                    total += 0
                if answer != "" and answer != correct:
                    total -= 1
                if correct == answer:
                    total += 4
    if total <0:
        return 0
    return total
