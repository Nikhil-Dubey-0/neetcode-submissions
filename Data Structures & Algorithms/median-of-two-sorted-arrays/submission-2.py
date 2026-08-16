import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        total = (len1 + len2)

        if len1 <= len2:
            small = nums1
            big = nums2
        else:
            small = nums2
            big = nums1

        left = 0
        right = len(small)
        while left <= right:
            s_right = (left + right + 1) // 2  # 1st right element small

            b_right = ((total+1)//2) - (s_right) # 1st right in big

            small_left  = small[s_right-1] if s_right > 0 else -math.inf
            small_right = small[s_right]   if s_right < len(small) else math.inf

            big_left    = big[b_right-1]   if b_right > 0 else -math.inf
            big_right   = big[b_right]     if b_right < len(big) else math.inf

            if small_left <= big_right and big_left <= small_right:
                break
            elif small_left > big_right:
                right = s_right - 1
            else:
                left = s_right + 1
        
        if total % 2 == 0:
            return (max(small_left, big_left) + min(small_right, big_right)) / 2
        else:
            return max(small_left, big_left)