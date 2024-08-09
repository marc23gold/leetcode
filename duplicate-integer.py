"""
Below is the hashset solution to the duplicate integer problem 
from neetcode150. 
The time complexity of this solution is O(n) and the space complexity O(n).
The solution starts by initializing a hashset, then a for loop is created to loop through the nums 
integer array. Then a condtional is evulated to see if there are any elements "n" from the integer array
that are in the hashset. Since the hashset is initally empty the conditional will return false on the first
turn but after that the conditional will return true if there are any elements "n" from the integer array 
that are in the hashset. This works because a set can only have unique elements, so comparing the elements in the nums array
will tell us if there are any elements from the nums array that have already been evaluated and added to the hashset from the 
nums array. 
after the condional the element "n" from the nums arrray is added to the hashset for the next iteration of the loop.
If the loop exits withought returning true then the function will return false because it has not found any duplicates.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize the set
        hashset = set()
        #create a for loop to loop through the nums integer array
        for n in nums:
            #create a conditional to see if an element within hashset
            #has is in the nums array 
            if n in hashset:
                return True
            hashset.add(n)
        return False

"""
Below is the two pointer solution to the duplicate integer problem. This solution has a time complexity of 
O(nlogn) because of the sort needed to be done on the nums array before comparison and and space complexity of O(1)
The nums array is sorted first 
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort the nums array
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]   :
                return True
        return False 
