# https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0/train/python

def my_first_interpreter(code):
    memory, output = 0, ""
    
    for command in code:
        if   command == "+":  
          memory += 1
        elif command == ".":  
          output += chr(memory % 256)
    
    return output
