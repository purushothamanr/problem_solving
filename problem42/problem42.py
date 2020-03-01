class Solution:
    def trap(self, A):
	left =  0
	right = len(A) - 1
        leftmost = rightmost = 0
        res = 0
        while left < right:
                leftmost = max(leftmost, A[left])
                rightmost = max(rightmost, A[right])
                
                if leftmost < rightmost:
                    res += leftmost -A[left]
                    left += 1
                else:
                    res += rightmost - A[right]
                    right -= 1
        return res	

p1 = Solution()
print(p1.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

