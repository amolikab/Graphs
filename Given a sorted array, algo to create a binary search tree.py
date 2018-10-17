#Given a sorted array, algo to create a binary search tree

class Node:
	def __init__(self,data):	
		self.data = data
		self.left = None
		self.right = None


def binary_tree(arr,l,r):
	n = l + (r-l)/2
	
	if (l == r):
		root = Node(arr[n])
		print("data is %d" %root.data)
		return root
		
	elif(r>l):
		#print("%d,%d" %(l,r))		
		root = Node(arr[n])
		#print("data is %d" %root.data)
		print("%d,%d" %(l,n-1))
		root.left = binary_tree(arr,l,n-1)
		print("%d,%d" %(n+1,r))
		root.right = binary_tree(arr,n+1,r)
		return root
	
def traverse(root):
	if(root.left):		
		traverse(root.left)
	print(root.data)
	if(root.right):
		traverse(root.right)

arr = [2,4,5,7,8,10,13,16,19]
n = len(arr)
print(arr)
ans = binary_tree(arr,0,n-1)
print(ans.data)
print(ans.left.data)
print(ans.right.data)


traverse(ans)
