class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        
        while top <= bottom:
            mid_row = (top + bottom)//2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                row = matrix[mid_row]
                left = 0
                right = len(row) - 1

                while left <= right:
                    mid = (left + right)//2

                    if row[mid] < target:
                        left = mid + 1
                    elif row[mid] > target:
                        right = mid - 1
                    else:
                        return True
                return False
                
        return False
        