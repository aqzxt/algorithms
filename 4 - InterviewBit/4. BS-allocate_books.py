"""
Created on Fri Mar 16 05:12:16 2018 ----------- @author: mxhfield
"""
from math import pi

def allocate_books(A, B):
    if len(A) < B or not B:
        return -1
    
    alt = []
    for k in A:
        alt.append(int(k/pi))
    print(alt)
    A = alt
    
    least_4each = sum(A)//B
    books = float('inf')
    i = 0
    while i < 2:
        lo, hi, mid = 0, len(A), len(A)//2
#        if not len(A) % 2 and i:
#            mid -=1
        while 0 < mid < len(A):
            first = A[:mid]
            second = A[mid:]
            
            if len(first) >= B-1 and sum(second) < books and sum(second) >= least_4each:
                books = sum(second)
                
            if len(second) >= B-1 and sum(first) < books and sum(first) >= least_4each:
                books = sum(first)
            
            if i:
                mid += 1
            
            if not i:
                mid -= 1
                
            print(least_4each,first, '__', second, books, '==',sum(first), sum(second),'==',lo, mid,hi)
        i += 1
    print()
    if books == float('inf'):
        return -1
    return books

def books(A, B):
   total = 0
   students = 0
   for k in A:
       if total + int(k*pi) > k # number_of_pages_in_current_book > V :
                  increment cnt_of_student
                  update Sum
        Else:
                  update Sum
   EndLoop;
  


    fix range LOW, HIGH
    Loop until LOW < HIGH:
            find MID_point
            Is number of students required to keep max number of pages below MID < M ? 
            IF Yes:
                update HIGH
            Else
                update LOW
    EndLoop;
    
#print(books([12, 34, 67, 90], 2))
#print(books([73, 58, 30, 72, 44, 78, 23, 9], 5))
#print(books([87, 3, 27, 29, 40, 12, 3, 69, 9, 57, 60, 33, 99], 3))