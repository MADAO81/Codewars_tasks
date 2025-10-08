# https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python


def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        cmd, r, v = (program[i] + ' 0').split()[:3]
        if cmd == 'inc': 
            d[r] += 1
        if cmd == 'dec': 
            d[r] -= 1        
        if cmd == 'mov': 
            d[r] = d[v] if v in d else int(v)
        if cmd == 'jnz' and (d[r] if r in d else int(r)): 
            i += int(v) - 1
        i += 1
    return d
