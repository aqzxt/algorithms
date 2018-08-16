"""
Created on Sun Mar 25 04:20:48 2018 ----------- @author: mxhfield
"""

def highest_product_of_3(A):
    so_far, answer = 0, [A[0], A[1], A[2]]
    for k in range(3, len(A)):
        a0, a1, a2, num = answer[0], answer[1], answer[2], A[k]
        
        if num*a1*a2 > so_far:
            answer[0], so_far = num, num*a1*a2
        
        if num*a0*a2 > so_far:
            answer[1], so_far = num, num*a0*a2
    
        if num*a0*a1 > so_far:
            answer[2], so_far = num, num*a0*a1
        print(so_far)
    return answer
    

    
print(highest_product_of_3([-10, -10, 2, 0, 4, 8, 1, -28]))
print(highest_product_of_3([2, 5, 8, 11]))
print(highest_product_of_3([-10, -10, 1, 3, 2]))



def highest_product_of_3(A):
    if len(A) < 3:
        raise ValueError('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # We could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(A[0], A[1])
    lowest  = min(A[0], A[1])
    highest_product_of_2 = A[0] * A[1]
    lowest_product_of_2  = A[0] * A[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = A[0] * A[1] * A[2]

    # Walk through items, starting at index 2
    for i in range(2, len(A)):
        current = A[i]

        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        # Do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3