"""
Created on Mon Feb 19 16:59:21 2018 ----------- @author: mxhfield

"""
import random

def in_place_shuffle(array):
    rand = random.sample(range(0, len(array)), len(array))
    
    inc = 0
    l = len(array)
    
    print(rand)
    print()
    
    print(array)
    print()
    for k in rand:
        array[k], array[l-k] = array[l-k], array[k]
        
        if inc == len(array) //2:
            break
        inc += 1
    return array
        
#array = random.sample(range(200), 30)
array = [117, 92, 60, 179, 174, 105, 6, 140, 193, 64, 131, 116, 41, 81, 184, \
         54, 24, 102, 165, 90, 155, 14, 177, 91, 143, 129, 154, 45, 191, 156]
print(in_place_shuffle(array))
