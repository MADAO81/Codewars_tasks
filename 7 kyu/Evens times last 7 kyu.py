# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python


# def even_last(numbers): 
#     return sum(numbers[::2]) * numbers[-1] if numbers else 0


# def even_last(numbers): 
#     return sum(numbers[::2]) * sum(numbers[-1:])



def even_last(numbers): 
    if numbers == []:
        return 0
    s=sum([el for i,el in enumerate(numbers) if i%2==0])
    return numbers[-1]*s
