# Median of Two Sorted Arrays
def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l,r = 0, len(A) - 1

    while l <= r:
        mid = (l + r) // 2
        hmid = half - mid - 2
        Aleft = A[mid] if mid >= 0 else float("-infinity")
        Aright = A[mid+1] if (mid + 1) < len(A) else float("infinity")
        Bleft = B[hmid] if hmid >= 0 else float("-infinity")
        Bright = B[hmid+1] if (hmid+1) < len(B) else float("infinity")
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2 != 0:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = mid -1
        else:
            l = mid + 1

print(findMedianSortedArrays([1,2,3],[3,4,5]))