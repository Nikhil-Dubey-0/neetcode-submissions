class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:
            partition1 = (left + right+1) // 2
            partition2 = total_left - partition1

            # Boundary values around the partitions
            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1] if partition1 < m else float("inf")

            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2] if partition2 < n else float("inf")

            # Correct partition
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2

            # Took too many elements from nums1
            elif left1 > right2:
                right = partition1 - 1

            # Took too few elements from nums1
            else:
                left = partition1 + 1