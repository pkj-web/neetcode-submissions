class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A= nums1
        B= nums2

        total = len(A)+len(B)

        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A)-1

        while True:

            i = (left+right) // 2
            j = half - i - 2

            if i>=0:
                Aleft = A[i]
            else:
                Aleft = float("-infinity")

            if (i+1) < len(A):
                Aright = A[i+1]
            else:
                Aright = float("infinity")

            if j>=0:
                Bleft = B[j]
            else:
                Bleft = float("-infinity")

            if (j+1) < len(B):
                Bright = B[j+1]
            else:
                Bright = float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i -1

            else:
                left = i + 1

            

        