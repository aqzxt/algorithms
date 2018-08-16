"""
Created on Thu Feb  8 17:55:44 2018 ----------- @author: mxhfield

"""

def merge_ranges(m):
    m.sort()
    k = 1
    while k < len(m):
        if m[k-1] is not None and m[k] is not None:

            if m[k][0] > m[k-1][0] < m[k][1] and m[k][0] < m[k-1][1] < m[k][1]:
                m[k] = (m[k-1][0], m[k][1])
                m[k-1] = None

            elif m[k-1][0] <= m[k][0] and m[k][1] <= m[k-1][1]:
                m[k] = None
        k += 1
    return [k for k in m if k is not None]

m = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10), (1, 2), (2, 3), (6, 7), (11,12)]
n = [(1, 10), (2, 6), (3, 5), (7, 9)]
#print(merge_ranges(m))

def merge_ranges2(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting,
        # use the later end time of the two
        if (current_meeting_start < last_merged_meeting_end):
            
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

print(merge_ranges2(m))


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        merged = [intervals[0]]
        for k in range(1, len(intervals)):
            current = intervals[k]
            if merged[-1].end > current.start:
                merged[-1].end = max(merged[-1].end, current.end)
            else:
                merged.append(current)
        return merged