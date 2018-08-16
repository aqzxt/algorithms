"""
Created on Thu Feb  1 16:36:22 2018 ----------- @author: mxhfield

"""

def get_products_of_all_ints_except_at_index2(int_list):
    
    def recur_product(new):
        if len(new) == 0:
            return 1
        return new[0] * recur_product(new[1:])
        
    answer = []
    # Make a list of the products
    for index in range(len(int_list)):
        new = int_list[:]
        new[index] = 1
        answer.append(recur_product(new))

    return answer

def products_of_all(int_list):
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    products = [None] * len(int_list)

    so_far = 1
    for i in range(len(int_list)):
        products[i] = so_far
        so_far *= int_list[i]
        
        print(products, so_far)
    print()
    
    so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        products[i] *= so_far
        so_far *= int_list[i]
        
        print(products, so_far)
        
    return products

test_input = [1, 7, 3, 4]
expected_output = [84, 12, 28, 21]
print('Got:', products_of_all(test_input))
print('Expected:', expected_output)
