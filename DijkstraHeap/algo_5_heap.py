import math

def get_line(array,i):
    z = array[i-1]
    q = []
    for x in range(0,len(z)):        
        q.append(map(int,z[x].split(",")))
    return q    

def search(c):
    for j in x:
        if(c == j):
            return True
    return False
    
    
def get_edges(q,a,i):
    for j in range(0,len(q)):
        if(search(q[j][0]) == False):
            v = i
            w = q[j][0]
            lvw = A[v] + q[j][1]            
            c = v,w,lvw
            a.append(c)
    return a

def get_edges_on_frontier(x):
    a = []
    for i in x:
        q = get_line(array,i)
        a = get_edges(q,a,i)
    return a

def heapup(heap):
    index = len(heap) -1
    while (index > 0):
        parent = int(math.floor((index -1 )/2))
        if(heap[index][2] < heap[parent][2]):
            #print("current node is %d at position %d" %(heap[index],index))
            #print("parent node is %d at position %d" %(heap[parent],parent))
            heap[parent],heap[index] = heap[index],heap[parent] 
            index = parent
            #print("bubbled up")
            #print("current node is %d at position %d" %(heap[index],index))
            
        else:
            #print("No need to bubble")
            break
    #print(heap)         

def heap_down(heap):
    index = 0
    size = len(heap)    
    left_child = (index * 2) + 1
    right_child = (index * 2) + 2
    while(right_child < size):
        
        if(heap[index][2] > heap[left_child][2] & heap[index][2] > heap[right_child][2]):
            #swap with smallest among two
            print("inside first loop")
            if(heap[left_child][2]<= heap[right_child][2]):
                #swap with left child
                print("inside first swap left loop")
                heap[index],heap[left_child] = heap[left_child],heap[index] 
                index = left_child
            else:
                #swap with right child
                print("inside first swap rightloop")
                heap[index],heap[right_child] = heap[right_child],heap[index] 
                index = right_child    
        elif(heap[index][2] <= heap[left_child][2] & heap[index][2] <= heap[right_child][2]):
            #print("No need to bubble")
            print("inside second loop")
            break
        elif(heap[index][2] > heap[left_child][2] & heap[index][2] < heap[right_child][2] ):
            #swap with left child
            print("inside third loop")
            heap[index],heap[left_child] = heap[left_child],heap[index] 
            index = left_child
        elif (heap[index][2] < heap[left_child][2] & heap[index][2] > heap[right_child][2]):
            #swap with right child
            print("inside fourth loop")
            heap[index],heap[right_child] = heap[right_child],heap[index] 
            index = right_child
        else:
            print("right_child index")
            print(right_child)
            print("right_child")
            print(heap[right_child])
            print("left_child")
            print(heap[left_child])
            print("index")
            print(heap[index])
            print(size)
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2
        print(" new right_child index")
        print(right_child)
    if(left_child < size):    
        if (heap[index][2] > heap[left_child][2]):
            #swap with left child
            heap[index],heap[left_child] = heap[left_child],heap[index] 
            index = left_child
    #print(heap)    



def extract_min(heap):
    min_value = heap[0]
    last = len(heap) -1
    heap[0],heap[last] = heap[last],heap[0]
    del heap[last]
    heap_down(heap)
    
    return min_value   
    
def insert(heap,q):
    #size = len(heap)
    #print(size)
    heap.append(q)
    heapup(heap)
    
    
def create_heap(a):
    heap = []
    heap.append(a[0])
    for j in range(1,len(a)):
        insert(heap,a[j])
    return heap              

def Dij(array):
    global x
    global y
    #x.append(2)
    #A[2] = 20
    while(len(x) < n):
        a = get_edges_on_frontier(x)
        #print("get_edges_on_frontier(x)")
        #print(a)
        heap = create_heap(a)
        #print(heap)
        p = extract_min(heap)
        A[p[1]] = p[2]
        x.append(p[1])
    print(A)
    print(x)

n = 6
with open("list.txt","r") as f:
    array = [line.split() for line in f]

x =[]
y = []
for i in range(2,n+1):
    y.append(i)
x.append(1)
A = [1000] * (n+1)
A[1] = 0
A[0] = 0

    
Dij(array)






