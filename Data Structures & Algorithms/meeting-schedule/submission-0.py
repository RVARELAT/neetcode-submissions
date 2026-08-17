"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x.start)
        
        current = intervals[0]
        
        for interval in intervals[1:]:
            start = interval.start
            
            if start < current.end:
                return False
            else:
                current = interval
                
        
        return True