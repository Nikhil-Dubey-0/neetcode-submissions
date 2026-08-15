class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<= nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        if nums1:
            while i<len(nums1):
                nums.append(nums1[i])
                i+=1
        if nums2:
            while j<len(nums2):
                nums.append(nums2[j])
                j+=1
        size = len(nums)
        if size % 2 != 0:
            return nums[(size//2)]
        else:
            return (nums[(size//2)] + nums[(size//2)-1]) / 2
        