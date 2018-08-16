"""
Created on Tue Feb 20 03:31:50 2018 ----------- @author: mxhfield

"""

class TempTracker:
    
    def __init__(self):
        self._tracker = {}
        self._min_temp = None
        self._max_temp = None
        self._total_sum = None
        self._unique_key_count = 0
        self._most_common_keys = None
        self._reading_numbers = 0
        
    def insert(self, temp):
        if not 0 <= temp <= 110:
            raise ValueError("Fahrenheit temp. Value should be from 0 to 110.")
        
        if temp in self._tracker:
            self._tracker[ temp ] += 1
            self._reading_numbers += 1
            if self._tracker[ temp ] > self._unique_key_count:
                self._unique_key_count = self._tracker[ temp ]
                self._most_common_keys = temp
        else:
            self._tracker[ temp ] = 1
            self._reading_numbers += 1
            if not self._unique_key_count:
                self._unique_key_count = 1
                self._most_common_keys = temp
            
        if self._min_temp is None:
            self._min_temp = temp
            self._max_temp = temp
            self._total_sum = temp
            
        elif temp < self._min_temp:
            self._min_temp = temp
            
        elif temp > self._max_temp:
            self._max_temp = temp
            
        self._total_sum += temp
            
    def get_max(self):
        return self._max_temp
    
    def get_min(self):
        return self._min_temp
    
    def get_mean(self):
        return self._total_sum / self._reading_numbers
    
    def get_mode(self):
        return self._most_common_keys