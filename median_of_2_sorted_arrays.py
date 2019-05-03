#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        k = 0
        nums3 = [0]*(l1+l2)
        while(i<l1 and j <l2):
            if(nums1[i]<=nums2[j]):
                nums3[k] = nums1[i]
                i+=1
            else:
                nums3[k] = nums2[j]
                j+=1
            k+=1

        while(i<l1):
            nums3[k] = nums1[i]
            i+=1
            k+=1

        while(j<l2):
            nums3[k] = nums2[j]
            j+=1
            k+=1
        l3 = l1 + l2
        if((l3)%2 == 0):
            return (nums3[l3/2] + nums3[l3/2-1])/2.0
        else:
            return nums3[l3/2]

s = Solution()

print(s.findMedianSortedArrays([1,3],[2]))
print(s.findMedianSortedArrays([1,2],[3,4]))

