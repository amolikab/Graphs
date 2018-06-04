
def get_line(array, j):
    q = []
    i = 0
    z = array[j-1]
    #print(z)
    while(i<len(z)):
        q.append(map(int,z[i].split(',')))
        i = i+1  
    return q  

def get_edges(array,a,i): #result of get line ie 2d array
    for j in range(1,len(array)):
        if(search(array[j][0])== False):
            x = i,array[j][0],array[j][1]
            a.append(x) 
        #else:
            #print("no need to add in edges")  
            #print(array[j][0],array[j][1])    
    return a    

def search(q):
    global x    
    for z in range(0,len(x)):
        if(x[z] == q):
            return True
    return False

def edges_on_frontier(x): #2d list of all edges to check
    a = []
    r = [] 
    #q = [] 
    print("vertices to check the outgoing edges")
    print(x)
    for i in x:   #all the vertices in x
        #print("value of i is %d" %i)
        q = get_line(array,i)
        #print("q is")
        #print(q)
        a = get_edges(q,a,i)
    return a    

def min(a):
    min = 10000
    for i in range(0,len(a)):
        v = a[i][0]
        w = a[i][1]
        lvw = a[i][2]
        x = A[v] + lvw
        if(x<min):
            min = x
            r = i
    #print(A)
    print("Min dist of %d thru %d "%(a[r][1],a[r][0]))
    return r 


def Dij():
    while(len(x) < n): 
        a = edges_on_frontier(x)     # a list of all the edges going out of x  
        #print("edges of frontier")
        #print(a)
        p = min(a)
        #print("the length of A is %d" %len(A))
        v = a[p][0]
        w = a[p][1]
        lvw = a[p][2]
        A[w] = A[v] + lvw
        #print(a[p][1])
        x.append(a[p][1])
        #print (x)
        print("")
        #B[a[p][1]] = B[v].append(
    print(A)  
    print (x)      

array = []

#arr = [[1,0] [2,20] [3,40], [2,0] [3,10] [1,20],[3,0] [2,10] [1,40]]
#arr = [[1],[2,20],[3,40]]
with open("dijkstraData.txt","r") as f:
    array = [line.split() for line in f]
##########Code to get one line of the array######################    

###############################

      #dijkstraData  
        
##########################        
n = 200
x = [1] #vetices that have been explored max value: n
A = [1000] *(n+1) #A[n] holds shortest path of 1 from n
A[0] = 0
A[1] = 0
B = [[0],[1]]
Dij()
print("A[7] is %d" %A[7])
print("A[37] is %d" %A[37])
print("A[59] is %d" %A[59])
print("A[82] is %d" %A[82])
print("A[99] is %d" %A[99])
print("A[115] is %d" %A[115])
print("A[133] is %d" %A[133])
print("A[165] is %d" %A[165])
print("A[188] is %d" %A[188])
print("A[197] is %d" %A[197])




z = [3,8,5,9,1,6,7]
heap = create_heap(z)
z = extract_min(heap)
print("min of heap is ")
print(z)
print(heap)
z = extract_min(heap)
print("min of heap is ")
print(z)
print(heap)










