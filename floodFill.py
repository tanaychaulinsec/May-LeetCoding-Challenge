from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        q=deque()
        q.append((sr, sc))
        dir=[(-1,0),(0,1),(1,0),(0,-1)]
        if color != newColor:
            while q:
                r, c = q.popleft()
                image[r][c] = newColor
                for dx, dy in dir:
                    if 0 <= r+dx <len(image) and 0 <= c+dy < len(image[0]):
                        if image[r+dx][c+dy] == color:
                            q.append((r+dx, c+dy))
        return image