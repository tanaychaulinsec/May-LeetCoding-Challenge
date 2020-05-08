class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        x1=coordinates[0][0]
        x2=coordinates[1][0]
        y1=coordinates[0][1]
        y2=coordinates[1][1]
        
        if x2==x1:
            for i in range(2,len(coordinates)):
                c=coordinates[i]
                if c[0]!=x2:
                    return False
            return True
        m=(y2-y1)/(x2-x1)
        for i in range(2,len(coordinates)):
            c=coordinates[i]
            slope=(c[1]-y1)/(c[0]-x1)
            if slope!=m:
                return False
        return True
        