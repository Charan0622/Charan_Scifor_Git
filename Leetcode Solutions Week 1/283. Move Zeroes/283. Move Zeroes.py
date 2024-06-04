class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Modify nums in-place.
        """
        # Initialize a pointer to keep track of the position where non-zero elements should be placed
        non_zero_index = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero, move it to the non-zero position and increment the pointer
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        # Fill the rest of the array with zeroes
        while non_zero_index < len(nums):
            nums[non_zero_index] = 0
            non_zero_index += 1
