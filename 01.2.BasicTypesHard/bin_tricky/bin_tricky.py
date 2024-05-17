from typing import Sequence


def find_median(nums1: Sequence[int], nums2: Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    # How that's work:
    len1, len2 = len(nums1), len(nums2)
    # Ensure nums1 is the smaller sequence
    if len1 > len2:
        nums1, nums2, len1, len2 = nums2, nums1, len2, len1

    # Initialize variables for binary search
    low, high, mid_length = 0, len1, (len1 + len2 + 1) // 2

    while low <= high:
        partition_nums1 = (low + high) // 2
        partition_nums2 = mid_length - partition_nums1

        if partition_nums1 < len1 and nums2[partition_nums2 - 1] > nums1[partition_nums1]:
            # Partition_nums1 is too small, increase it
            low = partition_nums1 + 1
        elif partition_nums1 > 0 and nums1[partition_nums1 - 1] > nums2[partition_nums2]:
            # Partition_nums1 is too big, decrease it
            high = partition_nums1 - 1
        else:
            # We've found the right partition
            if partition_nums1 == 0:
                max_left = nums2[partition_nums2 - 1]
            elif partition_nums2 == 0:
                max_left = nums1[partition_nums1 - 1]
            else:
                max_left = max(nums1[partition_nums1 - 1], nums2[partition_nums2 - 1])

            if (len1 + len2) % 2 == 1:
                # Total length of sequences is odd, median is the maximum value on the left of the partition
                return float(max_left)

            if partition_nums1 == len1:
                min_right = nums2[partition_nums2]
            elif partition_nums2 == len2:
                min_right = nums1[partition_nums1]
            else:
                min_right = min(nums1[partition_nums1], nums2[partition_nums2])

            # Total length of sequences is even, median is the average of the two values on either side of the partition
            return (max_left + min_right) / 2.0