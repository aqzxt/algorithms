"""
Created on Tue Mar 13 05:02:28 2018 ----------- @author: mxhfield
"""
a = [-40, -25, 5, 10, 14, 28, 29, 48, 56, 78]
b = [-48, -31, -15, -6, 1, 8]

def median_sorted_arrays(A, B):
    
    arr_max, arr_min = max(A, B), min(A, B)
    k1 = k2 = 0
    
    while k1 < len(max(A, B)):
        
        
        k1 += 1




def median_sorted_arrays2(A, B):
    imin, imax = 0, len(B)
    n, m = len(A), len(B)
    
    for e in range(imax):
#    Search in [imin, imax]:
        i = (imin + imax) // 2
        j = ((m + n + 1) // 2) - i
        if B[j - 1] > A[i]: 
            return median_sorted_arrays[i + 1, imax]
        elif A[i - 1] > B[j]:
            search in [imin, i - 1]
        else:
            if (m + n) % 2 == 1:
                return max(A[i - 1], B[j - 1])
            else:
                return (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2
    
#print(median_sorted_arrays([], [20]))
#print(median_sorted_arrays([0, 23], []))
#print(median_sorted_arrays([-40, -25, 5, 10, 14, 28, 29, 48], [-48, -31, -15, -6, 1, 8]))
#print(median_sorted_arrays([-37, -9, 10, 19], [-29, 18, 46]))

