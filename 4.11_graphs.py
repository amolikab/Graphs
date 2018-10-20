#implement binary tree fcns like insert, delete and find

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		

def insert(node,data):
	#new_node = Node(data)
	#node = root
	while(node != None):
		if(node.data<data and node.right == None):
			node.right = Node(data)
			break
		elif(node.data<data):
			node = node.right
		elif(node.data>= data and node.left == None):
			node.left = Node(data)
			break
		elif(node.data>= data):
			node = node.left

def find(root,data):
			
	if(root.data == data):
		print("found the data,returning True")
		return True
			
	if(root.right):
		print("entering root.right")
		if(find(root.right,data)):
			print("data found in right sub tree of %d"%root.data)
			return True		
	
	if(root.left):
		if(find(root.left,data)):
			print("data found in left sub tree of %d"%root.data)
			return True
		else:
			print("data not found in left sub tree of %d"%root.data)
			
	
	print("data not found in left or right sub tree of %d"%root.data)
	return False
			

def find_and_delete_min(root):
	to_be_Deleted = root
	right_subtree = to_be_Deleted.right
	if (not right_subtree.right and not right_subtree.left):
		to_be_Deleted.right = None
		return right_subtree.data
	elif (right_subtree.right and not right_subtree.left):
		to_be_Deleted.right = right_subtree.right
		return right_subtree.data
	else:
		smallest = right_subtree.left
		while(smallest.left):
			right_subtree = right_subtree.left
			smallest = right_subtree.left
	
		ans = smallest.data
		if(smallest.right):
			right_subtree.left = smallest.right
		else:
			right_subtree.left = None
		return smallest.data
			
			
def delete(root,data):
	if(root.data == data):
		print("found the data,returning True")
		return True
			
	if(root.right):
		print("entering root.right with root %d" %root.data)
		if(delete(root.right,data)):
			print("to_be_Deleted is %d"%root.right.data)
			print("data found in right sub tree of %d"%root.data)
			to_be_Deleted  = root.right			
			if(not to_be_Deleted.left and not to_be_Deleted.right):
				root.right = None
			elif(to_be_Deleted.left and not to_be_Deleted.right):
				#has a left child
				root.right = to_be_Deleted.left
			elif(not to_be_Deleted.left and to_be_Deleted.right):
				#has a right child
				root.right = to_be_Deleted.right
			elif(to_be_Deleted.left and to_be_Deleted.right):
				#has both children
				value = find_and_delete_min(to_be_Deleted)
				to_be_Deleted.data = value
			
						
				
	if(root.left):
		if(delete(root.left,data)):
			print("data found in left sub tree of %d"%root.data)
			to_be_Deleted  = root.left
			print("to_be_Deleted is %d"%to_be_Deleted.data)
			if(not to_be_Deleted.left and not to_be_Deleted.right):
				root.right = None
			elif(to_be_Deleted.left and not to_be_Deleted.right):
				#has a left child
				root.left = to_be_Deleted.left
			elif(not to_be_Deleted.left and to_be_Deleted.right):
				#has a right child
				root.left = to_be_Deleted.right
			elif(to_be_Deleted.left and to_be_Deleted.right):
				#has both children
				value = find_and_delete_min(to_be_Deleted)
				to_be_Deleted.data = value
		
	
	print("data not found in left or right sub tree of %d"%root.data)
	#return False
	
			
def traverse(root):
	if(root.left):
		traverse(root.left)
	print(root.data)
	if(root.right):
		traverse(root.right)

	
	
node = Node(20)
insert(node,15)
insert(node,35)
insert(node,10)
insert(node,12)
insert(node,28)
insert(node,22)
insert(node,45)
traverse(node)
#ans = find(node,22)
#print(ans)
delete(node,28)
traverse(node)



	