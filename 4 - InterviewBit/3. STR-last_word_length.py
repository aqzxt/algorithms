"""
Created on Thu Mar 22 19:20:36 2018 ----------- @author: mxhfield
"""

def last_word_length(A):
        count = 0
        
        # mark first letter found
        flag = False
        
        # iterate in reverse
        for i in range(len(A)-1, -1, -1):
            
            # check if alphanumeric and first letter found
            if A[i].isalpha() and not flag:
                flag = True
                count += 1
            
            # else if alpha and past first letter
            elif A[i].isalpha() and flag:
                count += 1
             
            # if char ' or - and past first letter
            elif A[i] == "'" or A[i] == "-" and flag:
                count += 1
            
            # if flagged and not alpha, halt operation
            elif flag:
                break
        return count

print(last_word_length("   wewqq ----2 w's - ewr"))