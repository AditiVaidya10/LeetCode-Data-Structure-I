class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        s = sum (mat, [])
        return mat if (len(s) % r) or (len(s)//r) != c else [s[i*c : (i+1)*c] for i in range (r)]
