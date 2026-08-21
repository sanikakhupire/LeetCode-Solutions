class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if (m*n) != (r*c):
            return mat

        temp = []
        for i in mat:
            temp.extend(i)

        ans = [0]*r
        i = 0
        j = 0
        while i < r:
            ans[i] = temp[j:j+c]
            i += 1
            j += c
        return ans
        