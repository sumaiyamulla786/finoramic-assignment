class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def threeSumClosest(self, A, B):
    A.sort()
    res = A[0] + A[1] + A[2]
    for i in range(len(A)-2):
        j = i + 1
        k = len(A) - 1
        while(j < k):
            temp = A[i] + A[j] + A[k]
            if(abs(B - temp) < abs(B - res)):
                res = temp
            if(temp < B):
                j += 1
            else:
                k -= 1 
    return res