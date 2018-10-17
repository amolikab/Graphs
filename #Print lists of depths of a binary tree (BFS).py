#Print lists of depths of a binary tree (BFS)


class queue:
	def __init__(self,node):
		self.items = [node]
		
	def enqueue(self,data):
		self.items.append(data)
	
	def dequeue(self):
		return self.items.pop(0)
		
	def IsEmpty(self):
		if (len(self.items) == 0):
			return True
		else:
			return False
			
	def size():
		return len(self.items)
	
	def print_queue(self):
		for i in self.items:
			print(i.data)
	
	
class tree_Node:
	def __init__(self,data):	
		self.data = data
		self.left = None
		self.right = None


def binary_tree(arr,l,r): #to store contents of a sorted array in a binary search tree
	n = l + (r-l)/2
	
	if (l == r):
		root = tree_Node(arr[n])
		return root
		
	elif(r>l):
		root = tree_Node(arr[n])
		root.left = binary_tree(arr,l,n-1)
		root.right = binary_tree(arr,n+1,r)
		return root
	
def traverse_tree(root):
	if(root.left):		
		traverse_tree(root.left)
	print(root.data)
	if(root.right):
		traverse_tree(root.right)

def BFS(queue, dis_level):
	list = []
	next_level = 0
	empty = queue.IsEmpty()
	
	while (dis_level>=1 and (empty == False)):
		
		node = queue.dequeue()
		if (node.left):
			next_level = next_level +1
			queue.enqueue(node.left)
			#print(node.left.data)
			
		if (node.right):
			next_level = next_level +1
			queue.enqueue(node.right)
			#print(node.right.data)
		
		dis_level = dis_level -1
		list.append(node.data)
	
	print(list)
	empty1 = queue.IsEmpty()
	if (empty1):
		pass
	else:
		BFS(queue,next_level)
		
		
		
		
arr = [2,4,5,7,8,10,13,16,19]
n = len(arr)
root = binary_tree(arr,0,n-1)
#traverse_tree(root)
queue = queue(root)
BFS(queue,1)









