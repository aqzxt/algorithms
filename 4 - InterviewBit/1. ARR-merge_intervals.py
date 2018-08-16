"""
Created on Fri Mar  2 02:51:32 2018 ----------- @author: mxhfield

1) Size of interval array as 0.

2) newInterval being an interval preceding all intervals in the array.
    Given interval (3,6),(8,10), insert and merge (1,2)

3) newInterval being an interval succeeding all intervals in the array.
    Given interval (1,2), (3,6), insert and merge (8,10)

4) newInterval not overlapping with any interval and falling
   in between 2 intervals in the array.
    Given interval (1,2), (8,10) insert and merge (3,6) 

5) newInterval covering all given intervals.
    Given interval (3, 5), (7, 9) insert and merge (1, 10)
"""

def merge_intervals(intervals, new):
    if not intervals:
        return new
    
    if intervals[0][0] > new[1]:
        intervals.insert(0 ,new)
        return intervals
        
    if intervals[-1][1] <= new[0]:
        intervals.append(new)
        return intervals
    
    if new[0] <= intervals[0][0] and intervals[-1][1] <= new[1]:
        return new
    
    indices = []
    no_overlap = {}
    k = 0
    while k < 2:
        hi, lo, mid = len(intervals)-1, 0, len(intervals)//2
        target = new[k]
        
        while lo < hi:
            print(lo, mid, hi)
            
            if intervals[mid][0] <= target <= intervals[mid][1]:
                indices.append(mid)
                break
            
            elif mid -1 >= 0 and mid +1 < len(intervals):
                if intervals[mid-1][1] < target < intervals[mid][0]:
                    indices.append(mid)
                    no_overlap[k] = 'before'
                    break
                
                if intervals[mid][1] < target < intervals[mid+1][0]:
                    indices.append(mid)
                    no_overlap[k] = 'after'
                    break
            
            if target < intervals[mid][0]:
                hi = mid
                mid //= 2
            
            else:
                lo = mid
                mid += ((hi - lo)//2) +1
        k += 1
    
    len_before = len(intervals)
    if no_overlap.get(0) == 'before':
        bak = intervals[mid]
        intervals.insert( mid, (new[0], bak[1]) )
        
    elif no_overlap.get(0) == 'after':
        bak = intervals[mid+1]
        intervals.insert( mid+1, (new[0], bak[1]) )
        
    if no_overlap.get(1) == 'before':
        bak = intervals[mid]
        if len_before < len(intervals):
            intervals[mid] = (bak[0], new[1])
        else:
            intervals.insert( mid, (bak[0], new[1]) )
        
    elif no_overlap.get(1) == 'after':
        bak = intervals[mid+1]
        if len_before < len(intervals):
            intervals[mid+1] = (bak[0], new[1])
        else:
            intervals.insert( mid+1, (bak[0], new[1]) )
        
    else:
        if len(indices) == 1:
            indices.append( indices[0] )
        first, second = indices[0], indices[1]
        mod = [( intervals[first][0], intervals[second][1] )]
        print(no_overlap)
        intervals = intervals[ :first] + mod + intervals[second +1: ]
        
    return intervals

a1 = [(6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097)]
a2 = (36210193, 61984219)

#print(merge_intervals([(3, 6), (8, 10)], (1, 2)))
#print(merge_intervals([(1, 2), (3, 5), (7, 9), (10, 12)], (8, 11)))
#print(merge_intervals([(1, 2), (3, 6)], (6, 10)))
#print(merge_intervals([(1, 2), (8, 10)], (3, 6)))


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class MergeIntervals:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        right = left = 0
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            else:
                left += 1
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]