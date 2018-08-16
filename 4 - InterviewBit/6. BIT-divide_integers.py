"""
Created on Sun Apr  1 03:21:29 2018 ----------- @author: mxhfield
"""

def divide_integers(dividend, divisor):
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    neg = False
    if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
        neg = True
        
    dividend, divisor = abs(dividend), abs(divisor)
    
    if divisor == 1:
        ans = dividend
        if neg:
            if -ans <= MIN_INT: return MIN_INT
            return -ans
        if ans >= MAX_INT: return MAX_INT
        return ans
    
    if divisor == 2:
        ans = dividend >> 1
        if neg:
            ans = -ans
            if -ans <= MIN_INT: return MIN_INT
            return ans
        
        if ans >= MAX_INT: return MAX_INT
        return ans
    
    if dividend <= divisor or not divisor: return 0
    
    ans = 0
    for k in range(divisor, dividend, divisor):
        if ans + divisor <= dividend:
            ans += 1
    
    if neg:
        if -ans <= MIN_INT:
            return MIN_INT
        return -ans
    if ans >= MAX_INT: return MAX_INT
    return ans

print(divide_integers(-2147483648, -1))




def divide(x, y):
    result = 0
    is_neg = (x < 0) ^ (y < 0)
    x, y = abs(x), abs(y)
    power = 0
    y_power = y << power
    
    while y_power <= x:
        power += 1
        y_power = y << power
        
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
            
        result += (1 << power)
        x -= y_power
        
    result = result if is_neg == False else -result
    return min(result, 2147483647)
    
    

def divide(dividend, divisor):
    s = -1 if dividend < 0 else 1
    t = -1 if divisor < 0 else 1
    dividend = s * dividend
    divisor = t * divisor
    d = divisor
    x = 1
    while d < dividend:
        d = d * 2
        x = x * 2
    
    ans = 0
    while dividend >= divisor:
        if d <= dividend:
            dividend = dividend - d
            ans = ans + x
        else:
            d = d / 2
            x = x / 2
    ans = ans * t * s
    ans = 2147483647 if ans > 2147483647L else ans
    ans = 2147483647 if ans < -2147483648L else ans
    return ans


    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        p = abs(dividend)
        q = abs(divisor)
        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX) :
            return INT_MAX
        if dividend <= INT_MIN and divisor == -1 :
            return INT_MAX
        if abs(divisor) == 1 :
            return dividend * divisor
        while p >= q :
            c = 0
            while p > (q << c) :
                c += 1
            res += 1 << (c -1)
            p -= q << (c - 1)

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) :
            return res
        else :
            return -res
        
        
        def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        p = abs(dividend)
        q = abs(divisor)
        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX) :
            return INT_MAX
        if dividend <= INT_MIN and divisor == -1 :
            return INT_MAX
        if abs(divisor) == 1 :
            return dividend * divisor
        while p >= q :
            c = 0
            while p > (q << c) :
                c += 1
            res += 1 << (c -1)
            p -= q << (c - 1)

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) :
            return res
        else :
            return -res