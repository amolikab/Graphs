# TO check if a route exists b/w 2 nodes in a graph



def edge (G,start):
	n = len(G)
	edges = []
	
	for i in range(0,n):
		if (G[i][0] == start):
			edges.append(G[i][1])
	return edges


def DFS (G,start,end):
	visited[start] = True
	edges = edge(G,start)
	#print(edges)
	if (len(edges) != 0):
		for i in edges:
			if (i == end):
				#print("found end at %d" %i)
				path.append(i)
				return True
			else:
				if(DFS(G,i,end)):
					path.append(i)
					return True
				
	return False



n = 6
graph = [ [0,5], [0,1], [0,4], [1,4], [1,3], [3,2], [3,4] ]
visited = [False] * n
path = []
ans = DFS(graph,0,2)
print(ans)
print(path)