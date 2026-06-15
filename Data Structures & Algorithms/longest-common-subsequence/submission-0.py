class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        Matrix = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(1, len(text1) + 1): 
            for j in range(1, len(text2) + 1): 
                if text1[i-1] == text2[j-1]: 
                    Matrix[i][j] = 1 + Matrix[i-1][j-1]
                else: 
                    Matrix[i][j] = max(Matrix[i-1][j], Matrix[i][j-1])
        
        return Matrix[len(text1)][len(text2)]