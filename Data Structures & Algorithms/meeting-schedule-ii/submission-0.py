"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        
        # Heap stores end times → heap[0] is the room that becomes free earliest.
        heap_end_times = []
        
        # push first meeting end time
        heapq.heappush(heap_end_times, intervals[0].end)
        
        for interval in intervals[1:]:
            earliest_end_time = heap_end_times[0]
            
            # If the earliest room is free before this meeting starts,
            # we can reuse that room.
            if earliest_end_time <= interval.start:
                heapq.heappop(heap_end_times)
            
            # Whether we reused a room or needed a new one,
            # this meeting is now occupying a room until interval.end.
            heapq.heappush(heap_end_times, interval.end)
        
        return len(heap_end_times)
    