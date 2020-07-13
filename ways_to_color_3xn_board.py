class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        comb_using_3_color=24
        comb_using_2_color=12
        
        for i in range(2,A+1):
            t=comb_using_3_color
            comb_using_3_color=(11*comb_using_3_color+10*comb_using_2_color)%1000000007
            comb_using_2_color=(5*t+7*comb_using_2_color)%1000000007
        result=(comb_using_3_color+comb_using_2_color)%1000000007
        return result
