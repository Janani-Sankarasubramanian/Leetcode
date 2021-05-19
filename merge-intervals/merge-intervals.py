class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []      
        if intervals == [] or intervals == [[]]: return []        
        intervals.sort(key = lambda x: x[0])        
        active_start, active_end = intervals[0]
        
        for start, end in intervals:
            if active_start <= start <= active_end:
                if end > active_end: active_end = end
            else:
                result.append([active_start, active_end])
                active_start, active_end = start, end
        
        result.append([active_start, active_end])
        return result