class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            row = [1]
            for j in range(1, len(res[i])):
                row.append(res[i][j-1]+res[i][j])
            row.append(1)
            res.append(row)
        return res
