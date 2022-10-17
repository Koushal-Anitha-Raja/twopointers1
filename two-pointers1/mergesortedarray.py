class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #time complexity:o(m*n)
        #space complexity:o(1)
        #first pointer is at nums1 middle index
        first =m-1
        #second pointer is at nums2 last index 
        second=n-1
        #third pointer is at last index of nums1
        third=m+n-1
        
        #iterate until first or second pointer goes out of bound
        while (first>=0 and second>=0):
            #if the first value is min then move it to thirs and decrement it by one
            if nums1[first]<nums2[second]:
                nums1[third]=nums2[second]
                #then shift second by one 
                second-=1
            else:
                nums1[third]=nums1[first]
                #or else decrement the first pointer by one 
                first-=1
                #whatever happend decrement the third pointer
            third-=1
            
        if (second>=0):
            nums1[:second+1]=nums2[:second+1]
                