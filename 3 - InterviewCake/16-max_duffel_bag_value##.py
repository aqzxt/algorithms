"""
Created on Wed Feb 21 21:08:03 2018 ----------- @author: mxhfield

"""

def max_duffel_bag_value(cakes, cap):
    if not cap:
        return 0
    each_cake_max = []
    biggest = 0
    for weight, value in cakes:
        if weight == 0:
            if value == 0:
                each_cake_max.append( (weight, value) )
                continue
            return float('inf')
        wv_limit = cap // weight
        each_cake_max.append( (wv_limit * weight, wv_limit * value) )
        if wv_limit * value > biggest:
            biggest = wv_limit * value
    
    index_left = 0
    index_right = 0
    flag = True
    while index_left < len(cakes):
        
        new_tuple = each_cake_max[index_left]
        old_tuple = cakes[index_right]
        if flag:
            cap_remainder = cap - (old_tuple[0] + new_tuple[0])
            flag = False
            
        print(old_tuple[0],cap_remainder,'===', old_tuple[1] + new_tuple[1], biggest)
        
        if old_tuple[0] + new_tuple[0] <= cap and old_tuple[1] + new_tuple[1] > biggest:
            biggest = old_tuple[1] + new_tuple[1]
            
        cap_remainder -= 1
        index_right += 1
        
        if index_right == len(cakes):
            index_right = 0
            index_left += 1
        if cap_remainder <= 0:
            flag = True
        
    return biggest




def max_duffel_bag_value2(cake_tuples, weight_capacity):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:

                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                max_value_using_cake = (
                    cake_value
                    + max_values_at_capacities[current_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake,
                                        current_max_value)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]


print(max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20))
print(max_duffel_bag_value([(9, 230), (5, 108), (3, 62), (0, 0)], 23))
print(max_duffel_bag_value2([(7, 160), (3, 90), (2, 15)], 20))
print(max_duffel_bag_value2([(9, 230), (5, 108), (3, 62), (0, 0)], 23))