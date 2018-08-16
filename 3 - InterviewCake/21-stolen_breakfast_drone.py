"""
Created on Sat Feb 24 21:59:57 2018 ----------- @author: mxhfield
"""

def stolen_breakfast_drone(delivery_id_list):
    dup_checker = {}
    for k in delivery_id_list:
        if dup_checker.get(k) == None:
            dup_checker[k] = k
        else:
            del dup_checker[k]
    return list(dup_checker)[0]
    
    
id_list = [1, 38, 3, 29, 32, 16, 27, 26, 29, 3, 38, 7, 31, 22, 18, 19, 10, 23, 31, \
           7, 35, 22, 39, 10, 33, 23, 35, 18, 19, 9, 26, 9, 34, 32, 16, 39, 1, 33, 34]

#print(stolen_breakfast_drone(id_list))


def find_unique_delivery_id(delivery_ids):

    unique_id = 0

    for id in delivery_ids:
#        print(unique_id,'-','{0:b}'.format(unique_id),'==', '{0:b}'.format(id),'-',id)
#        print()
        unique_id ^= id

    return unique_id #'{0:b}'.format(unique_id)

print(find_unique_delivery_id(id_list))