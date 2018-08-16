"""
Created on Sat Feb 17 04:21:31 2018 ----------- @author: mxhfield

"""

def rectangular_love(rectangle):
    
    rectangle['left_x'] += rectangle['width'] + rectangle['height']
    rectangle['bottom_y'] += rectangle['height'] + rectangle['width']
    
    
        
    return rectangle['left_x'] -1
    
    
    


    
rectangle = {
    # Coordinates of bottom-left corner
    'left_x'   : -4,
    'bottom_y' : -2,

    # Width and height
    'width'    : 14,
    'height'   : 30}

print(rectangular_love(rectangle))