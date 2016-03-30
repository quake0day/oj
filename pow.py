class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n < 0:
            return 1 / self.Pow(x, -n)
        else:
            return self.Pow(x, n)
            


    def Pow(self, x, n):
        if n == 0:
            return 1
        
        v = self.Pow(x, n/2)
        
        if n % 2 == 0:
            return v * v
        else:
            return v * v *x