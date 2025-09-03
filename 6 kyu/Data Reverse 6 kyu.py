# https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python



# def data_reverse(data):
#     rever = []
#     final = []
#     for i in range(0,len(data),8):
#         rever.append(data[i:i+8])
#     for i in reversed(rever):
#         final.extend(i)
#     return final

# def data_reverse(data):
#   res = []
  
#   for i in range(len(data)-8, -1, -8):
#     res.extend(data[i:i+8])
  
#   return res


def chunk(data,chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
def data_reverse(data):
    chunk_size = 8
    chunked_list = chunk(data,chunk_size)
    result = []
    for i in reversed(chunked_list):
        result.extend(i)
    return result
