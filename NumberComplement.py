class Solution:
    def findComplement(self, num: int) -> int:
        res = ''
        for i in bin(num).replace("0b",""):
            if i == '0':
                res += '1' 
            else:
                res += '0' 

        return int(res, 2)