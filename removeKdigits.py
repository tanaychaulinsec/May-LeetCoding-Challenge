class Solution:
    def removeKdigits(num,k):
        r=k
	stack=[]
	for i in num:
	    while stack and r and stack[-1]>i:
	        stack.pop()
		r-=1
	    stack.append(i)
	res="".join(stack[0:len(num)-k]).lstrip("0")
	return res if len(res) else "0"
		