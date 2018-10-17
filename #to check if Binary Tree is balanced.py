#to check if Binary Tree is balanced


class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 0


def Binary_Tree(arr,l,r):
	n = l + (r-l)/2
	if(l == r):
		root = Node(arr[n])
		#print("Node is %d" %root.data)
		return(root)
	elif(r>l):
		root = Node(arr[n])
		#print("Node is %d" %root.data)
		root.left = Binary_Tree(arr,l,n-1)
		root.right = Binary_Tree(arr,n+1,r)
		return root

def check_Balanced(root):	
	
	if(root.left):
		check_Balanced(root.left)
		#print(root.left.height)
		left_height = root.left.height
		root.height = left_height +1
		
	if(root.right):
		check_Balanced(root.right)
		#print(root.right.height)
		right_height = root.right.height
		potential_height = right_height +1
		if(root.height<potential_height):
			if (potential_height - root.height > 1):
				return False
			root.height = right_height +1
		elif(root.height>potential_height):
			if (root.height - potential_height  > 1):
				return False
	#print(root.data)
	return True
	
	
	
		
def traverse(root):
	if(root.left):
		traverse(root.left)
	print(root.data)
	if(root.right):
		traverse(root.right)



arr = [2,4,5,7,8,10,13,16,19]
n = len(arr)
root = Binary_Tree(arr,0,n-1)
#traverse(root)
ans = check_Balanced(root)
print(ans)








