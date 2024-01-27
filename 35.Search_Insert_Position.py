"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0 
        end = len(nums)
        while start < end:
            middle = start + (end-start)//2
            if nums[middle] < target:
                start = middle + 1
            else:
                end = middle
        return start
if __name__ == "__main__":
    obj = Solution()
    show = obj.searchInsert([1,3,5,6],5)
    print(show)
