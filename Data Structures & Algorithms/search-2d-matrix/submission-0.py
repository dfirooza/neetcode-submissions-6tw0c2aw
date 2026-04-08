class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix: 
            if target > row[-1]: 
                continue
            else: 
                start = 0 
                end = len(row) - 1
                while start <= end: 
                    mid = start + (end - start) // 2
                    if row[mid] == target: 
                        return True 
                    elif row[mid] < target: 
                        start = mid + 1
                    else: 
                        end = mid - 1
                return False
        return False