from collections import defaultdict
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [(root, None, 0)]
        dic =defaultdict()
        while stack:
            node, parent, level = stack.pop()
            dic[node.val] = (parent, level)
            if node.left:
                stack.append((node.left, node, level+1))
            if node.right: 
                stack.append((node.right, node, level+1))
        return (dic[x][0] != dic[y][0] and dic[x][1] == dic[y][1])