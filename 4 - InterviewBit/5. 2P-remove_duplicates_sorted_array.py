"""
Created on Sun Mar 18 07:13:43 2018 ----------- @author: mxhfield
"""

def remove_duplicates(A):
    if len(A) < 2:
        return len(A)
    
    k = 1
    flag = True
    pointer = 0
    while k < len(A):
        
        if A[k-1] == A[k] and flag:
            pointer = k
            flag = False
        
        elif not flag:
            if k > 1:
                
                if A[pointer] < A[k] and A[pointer -1] != A[k]:
                    A[pointer], A[k] = A[k], A[pointer]
                    pointer += 1
                    
            elif A[pointer] < A[k]:
                A[pointer], A[k] = A[k], A[pointer]
                pointer = k
        k += 1
    if pointer > 0:
        A = A[:pointer]
    print(A)
    return pointer

#print(remove_duplicates([1,1,1,2,3,4,5,5,5,5,6,7,7,7,7,8,9]))
print(remove_duplicates([-4,-4,-3,-1, 0, 0,1,1]))
#print(remove_duplicates([0, 1, 3]))


def remove_duplicates2(A):
    if len(A)<2:
        return len(A)
    
    #Maintain an end pointer indicating the end of array
    #current pointer i, that compares ith and i+1th element!
    #If you encounter equals, end pointer need not be incremented 
    #We append element at end and increment end if and only if
    #i and i+1 (the elements ahead) are different , 
    #that is whenever we encounter non repeating elements!!
    end =0
    #i goes from 0 to N-1 , i+1 goes from 1 to N
    #This is because end needs to be incremented atleast once
    for i in range(len(A)):
        #Make sure i+1 doesn't give list index out of bounds
        if i+1 < len(A) and A[i] == A[i+1]:
            continue
        #If i and i+1 have unequal elements
        A[end] = A[i]
        end+=1
    
    return end


def remove_duplicates3(A):
    n = len(A)
    if n <= 1:
        return n
    j = 1
    prev = A[0]
    for i in range(j,n):
        if A[i] != prev:
            prev = A[i]
            A[j] = A[i]
            j += 1
            
    return j
            


def remove_duplicates4(A):
    i=0
    j=1
    while(j<len(A)):
        if A[i]<A[j]:
            A[i+1],A[j]=A[j],A[i+1]
            i+=1
        j+=1
    j-=1
    while(j>i):
        A.pop()
        j-=1
    return len(A)

