import sys
from typing import List


class MedianSortedArrays:

    @staticmethod
    def solve(nums1: List[int], nums2: List[int]) -> float:
        # O(m+n)
        merged = []
        head1 = None
        head2 = None
        while len(nums1) > 0 or len(nums2) > 0 or head1 is not None or head2 is not None:
            if head1 is None and len(nums1) > 0:
                head1 = nums1.pop(0)

            if head2 is None and len(nums2) > 0:
                head2 = nums2.pop(0)

            if head1 is not None and head2 is not None:
                if head1 < head2:
                    merged.append(head1)
                    head1 = None
                elif head1 > head2:
                    merged.append(head2)
                    head2 = None
                else:  # head1 == head2
                    merged.append(head1)
                    merged.append(head2)
                    head1 = None
                    head2 = None
            elif head1 is None:
                merged.append(head2)
                head2 = None
            elif head2 is None:
                merged.append(head1)
                head1 = None

        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]
