"""
Created on Sat Mar 31 03:15:33 2018 ----------- @author: mxhfield
"""

def find_min_xor(A):
    A.sort()
    smallest = float('inf')
    gap = A[0] ^ A[1]
    
    repeat = False
    for j in range(len(A)-1):
        if A[j] == A[j+1]:
            repeat = True
            break
    
    for k in range(len(A)):
        
        print(A[k], gap, repeat)

        if k +1 < len(A) and not repeat:
            cur_gap = A[k] ^ A[k+1]
            if cur_gap <= gap:
                gap = cur_gap
            else:
                break
#        cur_gap = A[k] ^ A[k+1]
#        print(cur_gap)
        
        for j in range(k+1, len(A)):
            cur = A[k] ^ A[j]
            if cur < smallest:
                smallest = cur
    return smallest




#print(find_min_xor([0, 2, 5, 7]))
#print(find_min_xor([12, 4, 6, 2]))
#print(find_min_xor([15, 5, 1, 10, 2]))
#print(find_min_xor([12, 4, 6, 2]))
#print(find_min_xor([3, 2, 13, 1, 5, 13, 0, 13, 13]))

a = [492416, 275153, 684032, 319360, 543232, 804480, 525824, 671825, 1036753, 940625, 909521, 405120, 1076689, 80081, 57856, 1000145, 13649, 596049, 429649, 289489, 907136, 261120, 1247313, 902609, 576465, 1133696, 1128576, 877440, 1058432, 554449, 1206225, 1007953, 1066705, 1237329, 491601, 300753, 789073, 1233408, 513617, 657152, 993664, 93568, 324689, 457169, 254208, 1250560, 217169, 557568, 416896, 256465, 687313, 21888, 433536, 276224, 536145, 466304, 3200, 162176, 341376, 589824, 1075840, 411345, 401873, 52561, 653649, 1077376, 1011456, 339281, 297472, 931200, 869969, 1131601, 326272, 94801, 1246464, 646400, 727040, 1001856, 120192, 1093585, 309632, 313169, 160977, 1102720, 1126993]

print(find_min_xor(a))