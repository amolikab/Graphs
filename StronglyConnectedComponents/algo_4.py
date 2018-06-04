
def stack_of_edges(arr,x):
    i = 0
    edges = []
    while(i<k):
        if(arr[i][0] == x):
            #print(arr[i][1])
            edges.append(arr[i][1])
            i = i+1
        else:
            i = i+1
    if(len(edges)>0):
        return edges
    else:
        return -1           


def DFS(arr,s):
    #global current_label
    global t
    global q
    global scc
    global w
    w = w+1
    visited[s] = True
    leader[s] = q 
    
    print("current node is %d " %s)
    print(s)
    edges = stack_of_edges(arr,s)
    if(edges<0):
        print("there are no edges for %d" %s)        
    else:
        #print("edges of %d " %s)
        #print(edges)
        i = len(edges)
        while(i > 0):
            #print("num of edges %d"%i)
            #print("Consider edge %d" %edges[0])
            x = edges[0]
            if(visited[x] == False):
                DFS(arr,x)
                #print("Back to DFS of node %s "%s)
                del edges[0]
                i = i-1
            else:
                print("%d edge is explored" %x)                
                del edges[0]
                i = i-1
                
    t = t+1
    F[s] = t
    #print("Finishing time of %d is %d" %(s,t))
    #F[s] = current_label 
    #print(" current_label  is %d " %current_label)  
    #current_label = current_label -1
    #print(" current_label  is %d " %current_label)  
    
    
    
def DFS_loop(arr):
    global q
    global scc
    global w
    i=n
    p=0
    while(i>0):
        if(visited[i] == False):
            q = i
                       
            print("DFS has started with node %d" %i)
            DFS(arr,i)
            a = [i,w]
            scc.append(a)
            p=p+1
            w=0
            i = i-1
        else:
            i = i-1


def reverse(arr):
    i = 0
    while(i<k):
        Grev[i] = [arr[i][1],arr[i][0]]
        #arr[i][0],arr[i][1] = arr[i][1],arr[i][0]
        i = i+1
    
def rearrange( Grev,F):
    i = 0
    while(i<k):
        x = Grev[i][0]
        Grev[i][0] = F[x]
        y = Grev[i][1] 
        Grev[i][1] = F[y]
        G[i] = [Grev[i][1],Grev[i][0]]  
        i = i+1 
    #print(Grev) 
    #print(G)   
      
      
scc = []   
w = 0
n = 875714
#arr = [[1,2],[2,4],[1,3],[3,4]]
#array = [[1,4],[2,8],[3,6],[4,7],[5,2],[6,9],[7,1],[8,5],[8,6],[9,7],[9,3]]
with open("list.txt","r") as f:
    array = [map(int,line.split()) for line in f ]     
    
    
k = len(array)
Grev = [0]*k
G = [0]*k
visited = [False] * (n+1)
leader = [0] * (n+1)
F = [0] * (n+1) 
t = 0 
q = 0
#current_label = n

reverse(array)
print("DFS on the reverse graph")
#print(Grev)
DFS_loop(Grev)

print(F)

visited = [False] * (n+1)
scc = []


#rearrange(Grev,F)
#print("DFS on the original graph")
#print(G)
F = [0] * (n+1) 
t = 0
q = 0
#DFS_loop(G)

#print(leader)
#print(scc)


