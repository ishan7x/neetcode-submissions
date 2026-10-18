class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        mSt = nSt = 0
        mEn = m - 1
        nEn = n - 1
        while (mSt <= mEn):
            mMid = (mSt + mEn) // 2
            if (matrix[mMid][0] <= target <= matrix[mMid][nEn]):
                # seach the row
                # print(matrix[mMid])
                while (nSt <= nEn):
                    nMid = (nSt + nEn) // 2
                    if (matrix[mMid][nMid] == target):
                        return True
                    elif (matrix[mMid][nMid] < target):
                        nSt = nMid + 1
                    else:
                        nEn = nMid - 1
                return False
            elif (matrix[mMid][nEn] < target):
                mSt += 1
            else:
                mEn -= 1
        return False


        