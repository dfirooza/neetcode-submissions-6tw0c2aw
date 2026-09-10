"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #given: an array of meeting time interval objects consisting of start and end times 
        #return: whether a person could add all meeting to their schedule without any conflicts 
        #solution: sort them by start date, then go through and if the current end date is greater than the next one 
        #then return false otherwise if the loop ends then return ture 

        intervals.sort(key=lambda x: x.start) 

        for i in range(len(intervals)-1): 
            curr = intervals[i]
            n = intervals[i+1]
            
            if curr.end > n.start: 
                return False
        return True

            

