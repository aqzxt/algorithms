"""
Created on Sun May 20 02:31:33 2018 ----------- @author: mxhfield
"""

def justified_text(A, B):
    answer = []
    i = 0
    while i < len(A):
        
        count = 0
        to_append = []
        while count <= B:
            
            current = len(A[i])
            
            # check current word length against the total count
            if current + count <= B:
                to_append.append(A[i])
                count += current
                
            i += 1
        
        
    
    
    
    
    

w = ["This", "is", "an", "example", "of", "text", "justification."]

print(justified_text(w, 16))